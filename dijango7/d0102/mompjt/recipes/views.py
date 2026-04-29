import httpx
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.shortcuts import get_object_or_404

# =========================
# 1️⃣ 스크래핑 함수
# =========================
def scrape_recipes_by_kind(kind):
    """
    kind: 1=초기, 2=중기, 3=후기
    """
    url = f'https://www.babymoov.co.kr/board/list.php?bdId=cook&kind={kind}'

    response = httpx.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    recipe_list = []
    items = soup.select('#cook_list .cookcook .list li')

    for item in items:
        # 이미지
        img_tag = item.select_one('.thumbnail img')
        image = img_tag['src'] if img_tag else '/static/images/placeholder.png'
        
        # 외부 이미지 URL을 절대 경로로 변환
        if image and not image.startswith(('http://', 'https://', '/')):
            image = f'https://www.babymoov.co.kr{image}' if not image.startswith('/') else f'https://www.babymoov.co.kr{image}'
        elif image and image.startswith('/'):
            image = f'https://www.babymoov.co.kr{image}'

        # 제목
        title_tag = item.select_one('.txt strong')
        title = title_tag.get_text(strip=True) if title_tag else '제목 없음'

        # 링크 (javascript → articleId 추출)
        a_tag = item.select_one('.txt a')
        link = '#'
        if a_tag and 'href' in a_tag.attrs:
            js = a_tag['href']
            article_id = js.split(',')[1].strip()
            link = f'https://www.babymoov.co.kr/board/view.php?bdId=cook&articleId={article_id}'

        # ⭐ 통합 dict 구조
        recipe_list.append({
            'title': title,
            'image': image,
            'url': link,
            'is_external': True,
        })

    return recipe_list


# =========================
# 2️⃣ DB 레시피 → dict 변환
# =========================
def get_db_recipes():
    recipes = Recipe.objects.all().prefetch_related('steps')

    result = []
    for r in recipes:
        first_step = r.steps.first()

        result.append({
            'title': r.title,
            'image': (
                first_step.image.url
                if first_step and first_step.image
                else '/static/images/placeholder.png'
            ),
            'url': reverse('recipes:recipe_detail', args=[r.id]),
            'is_external': False,
        })

    return result


# =========================
# 3️⃣ 공통 리스트 뷰
# =========================
def recipes_list_view(request, kind):
    """
    kind: 1=초기, 2=중기, 3=후기
    """

    # 🔹 DB 레시피
    db_recipes = get_db_recipes()

    # 🔹 스크래핑 레시피
    scraped_recipes = scrape_recipes_by_kind(kind)

    # 🔹 통합
    all_recipes = db_recipes + scraped_recipes

    # 🔹 검색
    q = request.GET.get('q', '').strip()
    if q:
        all_recipes = [
            r for r in all_recipes if q.lower() in r['title'].lower()
        ]

    # 🔹 페이지네이션
    paginator = Paginator(all_recipes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes_main.html', {
        'page_obj': page_obj,
        'q': q,
        'kind': kind,
    })

def recipes_main(request):
    """
    전체 레시피 페이지 (초기 + 중기 + 후기 스크래핑 + DB)
    """
    db_recipes = get_db_recipes()

    scraped_recipes = (
        scrape_recipes_by_kind(1)
        + scrape_recipes_by_kind(2)
        + scrape_recipes_by_kind(3)
    )

    all_recipes = db_recipes + scraped_recipes

    # 검색
    q = request.GET.get('q', '').strip()
    if q:
        all_recipes = [
            r for r in all_recipes if q.lower() in r['title'].lower()
        ]

    paginator = Paginator(all_recipes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes_main.html', {
        'page_obj': page_obj,
        'q': q,
        'kind': 0,
    })

# =========================
# 4️⃣ stage별 뷰
# =========================
def recipes_stage_1(request):
    return recipes_list_view(request, kind=1)

def recipes_stage_2(request):
    return recipes_list_view(request, kind=2)

def recipes_stage_3(request):
    return recipes_list_view(request, kind=3)

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes:recipes_main')
    else:
        form = RecipeForm()

    return render(request, 'recipe_form.html', {
        'form': form,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
    })


# ═══════════════════════════════════════════════════════════════════════
# ★ 26-01-02 추가: AI 이유식 레시피 생성기
# ═══════════════════════════════════════════════════════════════════════
# 기능: 사용자가 냉장고 재료를 입력하면 AI가 월령별 맞춤 이유식 레시피 생성
# =================================================================== ====

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
from django.conf import settings
import json

@login_required(login_url='accounts:login')
@require_http_methods(["POST"])
def generate_recipe(request):
    """
    AI 이유식 레시피 생성
    
    요청 데이터:
    {
        'ingredients': '시금치, 두부, 당근',
        'baby_month': 6,
        'allergy': '계란' (선택사항)
    }
    """
    try:
        data = json.loads(request.body)
        ingredients = data.get('ingredients', '').strip()
        baby_month = data.get('baby_month', 6)
        allergies = data.get('allergies', '').strip()
        
        if not ingredients:
            return JsonResponse({'error': '재료를 입력해주세요.'}, status=400)
        
        # Google API 설정
        GOOGLE_API_KEY = getattr(settings, 'GOOGLE_API_KEY', '')
        if not GOOGLE_API_KEY:
            return JsonResponse({'error': 'AI 서비스가 준비되지 않았습니다.'}, status=500)
        
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # 월령별 단계 결정
        stage_map = {
            (4, 5): ('초기', '곡류, 채소, 과일 중심'),
            (6, 7): ('중기', '곡류, 채소, 과일, 육류 추가'),
            (8, 11): ('후기', '다양한 식재료, 두부, 계란'),
            (12, 24): ('완료기', '일반식에 가까운 식단'),
        }
        
        stage_name = '초기'
        stage_desc = '곡류, 채소, 과일 중심'
        
        for (min_m, max_m), (stage, desc) in stage_map.items():
            if min_m <= baby_month <= max_m:
                stage_name = stage
                stage_desc = desc
                break
        
        # 프롬프트 엔지니어링
        allergy_info = f"\n⚠️ 알레르기: {allergies}" if allergies else ""
        
        system_prompt = """당신은 소아과 의사 출신의 전문 영양사입니다. 
아기의 월령과 발달 단계에 맞는 건강한 이유식 레시피를 만듭니다.
답변은 다음 형식으로 작성하세요:

🍽️ [레시피명]
⏱️ 준비시간: X분
👶 월령: X개월 추천
🥘 재료:
  - 재료1: 양
  - 재료2: 양
📖 만드는 법:
  1. 단계1
  2. 단계2
💡 영양정보: 주요 영양소 설명
⚠️ 주의사항: 조리 시 유의점"""

        user_prompt = f"""우리 아기는 {baby_month}개월입니다. ({stage_name} 단계: {stage_desc})
냉장고에 있는 재료: {ingredients}{allergy_info}

이 재료들로 맛있고 영양가 있는 이유식 레시피 3가지를 만들어주세요.
월령에 맞는 식감과 영양을 고려해서 작성해주세요."""

        print(f"🤖 AI 레시피 생성 요청: {ingredients} (아기 {baby_month}개월)")
        
        # AI 모델 호출
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([system_prompt, user_prompt])
        recipe_content = response.text
        
        print(f"✅ AI 레시피 생성 완료")
        
        return JsonResponse({
            'success': True,
            'recipe': recipe_content,
            'stage': stage_name,
            'baby_month': baby_month,
            'ingredients': ingredients,
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': '요청 형식이 잘못되었습니다.'}, status=400)
    except Exception as e:
        print(f"❌ 레시피 생성 오류: {str(e)}")
        return JsonResponse({'error': f'레시피 생성 중 오류가 발생했습니다: {str(e)}'}, status=500)