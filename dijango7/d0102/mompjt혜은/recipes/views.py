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