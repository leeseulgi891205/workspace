# ========================================== Django에서 필요한 기능들 import ====================
# render: HTML 템플릿을 보여주는 함수
# redirect: 다른 URL로 이동시키는 함수 (예: 저장 후 목록 페이지로 이동)
# get_object_or_404: 데이터를 찾고 없으면 404 에러를 보여줌
from django.shortcuts import render,redirect,get_object_or_404

# timezone: 현재 시간을 구하는 함수 (서버 시간대에 맞춰줌)
from django.utils import timezone

# timedelta: 날짜 계산용 (예: 최근 7일, 30일 등)
from datetime import timedelta

# OperationalError: 데이터베이스 오류 처리용
from django.db.utils import OperationalError

# ========================================== 앱 내부 import ====================
# Board 모델: 게시판 데이터를 정의한 모델 (제목, 내용, 작성자 등)
from .models import Board

# ========================================== Django 로그인 보호 기능 ====================
# 🔧 수정: @login_required 데코레이터를 사용하려면 import 필수
# ❌ 원래: 이 import이 없어서 NameError 발생
# ✅ 변경: django.contrib.auth.decorators에서 login_required 임포트
# 역할: 함수 앞에 @login_required를 붙이면 로그인하지 않은 사용자는 접근 불가
from django.contrib.auth.decorators import login_required

# ========================================== API 응답 & HTTP 오류 처리 ====================
# JsonResponse: JSON 형식으로 데이터를 응답 (API에서 사용)
# HttpResponseBadRequest: "요청이 잘못됐습니다" 에러 표시
from django.http import JsonResponse, HttpResponseBadRequest

# ========================================== 외부 라이브러리 & 유틸 ====================
# requests: 외부 API(Overpass) 요청할 때 사용
import requests

# lru_cache: 함수 결과를 메모리에 저장해서 빠르게 실행 (자주 쓰는 데이터)
from functools import lru_cache

# time: 시간 계산 (캐시 만료 시간 체크)
import time

# Paginator: 게시글을 한 페이지 5개씩 나누는 기능 (페이지 네이션)
from django.core.paginator import Paginator

# ========================================== OpenAI API (챗봇용) ====================
# 🔧 추가: OpenAI GPT API를 사용해서 진짜 AI 챗봇 구현
# 설치: pip install openai
# 역할: 사용자 질문에 자연스러운 대화로 답변 (키워드 매칭이 아닌 진짜 AI)
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️ OpenAI 라이브러리가 설치되지 않았습니다. 'pip install openai' 실행")

# ========================================== Report 모델 import (다른 앱에서) ====================
# 역할: 신고 기능(reports)이 있으면 사용, 없으면 None으로 설정 (에러 방지)
try:
    from reports.models import Report
except Exception:
    Report = None


# ========================================== 홈 페이지 뷰 ====================
def home(request):
    """
    홈 페이지 함수
    - 최근 7일 신고 수, 30일 신고 수, 평균 위험도를 계산해서 보여줌
    """
    # 현재 시간 가져오기
    now = timezone.now()
    
    # 기본값 설정 (Report 모델이 없거나 오류가 나면 0으로 표시)
    last7 = 0
    last30 = 0
    avg_risk_7 = 0

    # Report 모델이 있으면 실행
    if Report is not None:
        try:
            # 지난 7일 동안의 신고 건수 세기
            last7 = Report.objects.filter(created_at__gte=now - timedelta(days=7)).count()
            
            # 지난 30일 동안의 신고 건수 세기
            last30 = Report.objects.filter(created_at__gte=now - timedelta(days=30)).count()
            
            # 지난 7일 신고들의 위험도 가져오기
            risks = list(Report.objects.filter(created_at__gte=now - timedelta(days=7)).values_list('risk', flat=True))
            
            # 위험도 평균 계산 (소수점 2자리까지)
            avg_risk_7 = round(sum(risks) / len(risks), 2) if risks else 0
        except OperationalError:
            # 데이터베이스 오류나면 기본값 유지
            last7 = last30 = 0
            avg_risk_7 = 0

    # home.html 템플릿에 데이터 전달하고 보여주기
    return render(request, 'pages/home.html', {'last7': last7, 'last30': last30, 'avg_risk_7': avg_risk_7})


# ========================================== 소개 페이지 뷰 ====================
def about(request):
    """
    소개 페이지 (about.html 템플릿만 보여줌)
    """
    return render(request, 'pages/about.html')


# ========================================== 한국 행정구역 조회 (Overpass API 연동) ====================
# 이 섹션은 지도에서 시/도, 시/군/구, 동 정보를 가져오는 기능

# 캐시 저장소 (메모리에 저장해서 자주 요청하는 데이터를 빠르게 제공)
_cache_store = {}
# 캐시 유효시간: 1시간 (3600초)
_CACHE_TTL_SEC = 60 * 60

def _cache_get(key):
    """
    캐시에서 데이터 가져오기
    - key: 찾을 데이터의 이름
    - 반환: 캐시된 데이터 또는 None
    """
    item = _cache_store.get(key)
    if not item:
        return None
    
    # 데이터 저장 시간과 현재 시간 비교
    ts, value = item
    # 1시간 이상 지났으면 캐시 삭제하고 None 반환 (새로 가져오게 함)
    if time.time() - ts > _CACHE_TTL_SEC:
        _cache_store.pop(key, None)
        return None
    
    # 캐시 시간이 유효하면 데이터 반환
    return value


def _cache_set(key, value):
    """
    캐시에 데이터 저장하기
    - key: 데이터의 이름
    - value: 저장할 데이터
    """
    _cache_store[key] = (time.time(), value)


# Overpass API 주소 (지도 데이터 조회)
OVERPASS_URL = "https://overpass-api.de/api/interpreter"


def _overpass(query):
    """
    Overpass API로 한국 행정구역 데이터 요청하기
    - query: 요청할 쿼리 (어떤 데이터를 원하는지)
    - 반환: JSON 데이터 또는 오류 시 빈 리스트
    """
    try:
        # Overpass 서버에 요청 보내기
        r = requests.post(OVERPASS_URL, data={"data": query}, timeout=25)
        # 요청 성공했는지 확인
        r.raise_for_status()
        # JSON 형식으로 변환해서 반환
        return r.json()
    except Exception as e:
        # 오류가 나면 빈 데이터 반환 (앱이 깨지지 않도록)
        return {"elements": []}


def _list_sido():
    """
    한국의 모든 시/도 목록 가져오기 (서울, 경기, 부산 등)
    """
    # 캐시에 이미 있는지 확인
    key = "sido:list"
    cached = _cache_get(key)
    if cached is not None:
        return cached
    
    # Overpass 쿼리 (대한민국의 admin_level=4인 행정구역 = 시/도)
    q = (
        "[out:json][timeout:25];"
        "rel[boundary=administrative][admin_level=2][name=\"대한민국\"];"
        "map_to_area->.kr;"
        "rel(area.kr)[boundary=administrative][admin_level=4][name];"
        "out tags;"
    )
    
    # API 요청해서 데이터 받기
    j = _overpass(q)
    
    # 시/도 이름만 추출해서 정렬
    names = sorted({(e.get('tags') or {}).get('name') for e in j.get('elements', []) if (e.get('tags') or {}).get('name')})
    
    # 캐시에 저장 (다음에는 빠르게 제공)
    _cache_set(key, names)
    
    return names


def _list_sigungu(sido_name: str):
    """
    특정 시/도의 시/군/구 목록 가져오기
    - sido_name: 시/도 이름 (예: "서울특별시")
    """
    key = f"sigungu:{sido_name}"
    cached = _cache_get(key)
    if cached is not None:
        return cached
    
    # Overpass 쿼리
    q = (
        "[out:json][timeout:25];"
        f"rel[boundary=administrative][admin_level=4][name=\"{sido_name}\"];"
        "map_to_area->.a;"
        "rel(area.a)[boundary=administrative][admin_level=6][name];"
        "out tags;"
    )
    j = _overpass(q)
    names = sorted({(e.get('tags') or {}).get('name') for e in j.get('elements', []) if (e.get('tags') or {}).get('name')})
    _cache_set(key, names)
    return names


def _list_dong(sido_name: str, sigungu_name: str):
    """
    특정 시/도와 시/군/구의 동 목록 가져오기
    - sido_name: 시/도 이름 (예: "서울특별시")
    - sigungu_name: 시/군/구 이름 (예: "강남구")
    """
    key = f"dong:{sido_name}:{sigungu_name}"
    cached = _cache_get(key)
    if cached is not None:
        return cached
    
    # Overpass 쿼리
    q = (
        "[out:json][timeout:25];"
        f"rel[boundary=administrative][admin_level=4][name=\"{sido_name}\"];"
        "map_to_area->.sido;"
        f"rel(area.sido)[boundary=administrative][admin_level=6][name=\"{sigungu_name}\"];"
        "map_to_area->.sgg;"
        "rel(area.sgg)[boundary=administrative][admin_level~\"8|9|10\"][name];"
        "out tags;"
    )
    j = _overpass(q)
    names = sorted({(e.get('tags') or {}).get('name') for e in j.get('elements', []) if (e.get('tags') or {}).get('name')})
    _cache_set(key, names)
    return names


def kr_admin(request):
    """
    한국 행정구역 API 엔드포인트
    - GET /pages/api/kr-admin/?level=sido -> 시/도 목록
    - GET /pages/api/kr-admin/?sido=서울특별시 -> 강남구, 서초구 등 시/군/구 목록
    - GET /pages/api/kr-admin/?sido=서울특별시&sigungu=강남구 -> 강남구의 동 목록
    """
    # URL에서 파라미터 받기
    level = request.GET.get('level')
    sido = request.GET.get('sido')
    sigungu = request.GET.get('sigungu')

    # 파라미터가 없으면 시/도 목록 반환
    if level == 'sido' or (not sido and not sigungu):
        return JsonResponse({"level": "sido", "items": _list_sido()})

    # 시/도만 있으면 시/군/구 목록 반환
    if sido and not sigungu:
        items = _list_sigungu(sido)
        return JsonResponse({"level": "sigungu", "sido": sido, "items": items})

    # 시/도와 시/군/구 있으면 동 목록 반환
    if sido and sigungu:
        items = _list_dong(sido, sigungu)
        return JsonResponse({"level": "dong", "sido": sido, "sigungu": sigungu, "items": items})

    # 잘못된 요청은 에러 반환
    return HttpResponseBadRequest("Invalid parameters")


# ========================================== 게시판 목록 뷰 ====================
# 혜은 [게시글 페이지 번호]=========================================
def board_list(request):
    """
    게시판 목록 페이지 보여주기
    - 모든 게시글을 최신순으로 보여줌
    - 한 페이지에 5개씩 표시 (페이지네이션)
    """
    # 모든 게시글 가져오기, 최신글이 위에 오도록 정렬 (-id: id 역순)
    board_qs = Board.objects.all().order_by('-id')

    # Paginator: 게시글을 5개씩 나누기
    paginator = Paginator(board_qs, 5)  # ✅ 한 페이지 5개
    
    # URL에서 현재 페이지 번호 받기 (없으면 1페이지)
    page_number = request.GET.get('page', 1)  # 요청 페이지 번호
    
    # 현재 페이지의 게시글 가져오기 (안전하게 - 없는 페이지면 마지막 페이지)
    page_obj = paginator.get_page(page_number)
    
    # ✅ 전체 게시글 수 세기
    total_count = board_qs.count()

    # ✅ 페이지 번호를 5개씩 묶기 (1~5페이지, 6~10페이지 등)
    group_size = 5
    current = page_obj.number  # 현재 페이지 번호
    start_page = ((current - 1) // group_size) * group_size + 1  # 묶음의 시작 페이지
    end_page = min(start_page + group_size - 1, paginator.num_pages)  # 묶음의 끝 페이지

    # 보여줄 페이지 번호 범위 (예: 1~5)
    page_range = range(start_page, end_page + 1)

    # board_list.html 템플릿에 데이터 전달하기
    return render(request, 'board_list.html', {
        'page_obj': page_obj,  # 현재 페이지의 게시글들
        'page_range': page_range,  # ✅ 템플릿에서 사용할 페이지 번호들
        'start_page': start_page,  # 첫 번째 페이지 번호
        'end_page': end_page,  # 마지막 페이지 번호
        'total_count': total_count,  # ✅ 전체 게시글 수
    })
# 혜은 [게시글 페이지 번호]=========================================


# ========================================== 게시글 작성 뷰 ====================
# 혜은 251223=[게시글작성]========================================
# 🔧 @login_required: 로그인하지 않은 사용자는 이 페이지 접근 불가
# 역할: 로그인 페이지로 자동 리다이렉트
@login_required
def board_create(request):
    """
    게시글 작성 페이지
    - GET: 게시글 작성 폼 보여주기 (board_create.html)
    - POST: 게시글 저장하기
    """
    # POST 요청 (폼 제출할 때)
    if request.method == 'POST':
        # 폼에서 입력받은 제목과 내용
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # 🔧 수정: 게시글을 한 번만 생성하고 author를 함께 저장
        # ❌ 원래: board = Board()를 만들고 save()한 후, 또 Board.objects.create()로 다시 만들어서
        #         게시글이 2개 생기고, 두 번째 create()에는 author를 빠뜨려서 작성자가 안 보임
        # ✅ 변경: Board.objects.create()로 한 번만 만들면서 author=request.user를 함께 저장
        
        # Board 모델에 데이터 저장하기
        Board.objects.create(
            title=title,  # 입력받은 제목
            content=content,  # 입력받은 내용
            author=request.user  # 🔧 수정: 로그인한 사용자를 작성자로 저장
        )

        # 저장 완료 후 게시판 목록 페이지로 이동
        return redirect('pages:board_list')

    # GET 요청 (페이지 접속했을 때) - 작성 폼 보여주기
    return render(request, 'board_create.html')
# 혜은 251223=========================================


# ========================================== 게시글 상세 페이지 뷰 ====================
# 혜은 1223======게시글 상세페이지 뷰 ==========================
def board_detail(request, pk):
    """
    게시글 상세 페이지 보여주기
    - pk: 게시글의 고유 ID (1번, 2번 게시글 등)
    """
    # 해당 ID의 게시글 찾기 (없으면 404 에러 표시)
    board = get_object_or_404(Board, pk=pk)

    # board_detail.html 템플릿에 해당 게시글 데이터 전달
    return render(request, 'reports/board_detail.html', {'board': board})
# 혜은 1223======게시글 상세페이지 뷰 ==========================


# ========================================== 챗봇 기능 ====================
import json
from django.views.decorators.csrf import csrf_exempt

def chatbot(request):
    """
    챗봇 페이지 보여주기
    - 사용자와 AI가 대화할 수 있는 채팅 인터페이스
    """
    return render(request, 'pages/chatbot.html')


@csrf_exempt  # API 요청이므로 CSRF 토큰 검증 제외 (보안상 실제 운영에서는 주의 필요)
def chatbot_api(request):
    """
    챗봇 AI 응답 API
    - 사용자 메시지를 받아서 AI 응답 생성
    - POST /pages/chatbot/api/ {"message": "안녕하세요"}
    """
    if request.method != 'POST':
        return JsonResponse({'error': '잘못된 요청입니다'}, status=400)
    
    try:
        # 요청에서 사용자 메시지 받기
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': '메시지를 입력해주세요'}, status=400)
        
        # 🤖 AI 응답 생성 (현재는 간단한 규칙 기반, 나중에 OpenAI API로 교체 가능)
        ai_response = generate_ai_response(user_message)
        
        # JSON 형식으로 응답 반환
        return JsonResponse({
            'success': True,
            'response': ai_response,
            'timestamp': timezone.now().isoformat()
        })
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON 형식이 올바르지 않습니다'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def generate_ai_response(user_message):
    """
    🤖 OpenAI GPT API를 사용한 AI 응답 생성
    
    ✅ 수정 완료: 규칙 기반 → 진짜 AI로 업그레이드
    
    동작 원리:
    1. OpenAI API 키가 있는지 확인
    2. GPT-4 모델에 사용자 메시지 전송
    3. AI가 자연스러운 대화로 답변 생성
    4. 응답을 한국어로 반환
    
    필수 준비물:
    1. OpenAI API 키 (https://platform.openai.com/api-keys)
    2. pip install openai
    3. 환경변수 설정: set OPENAI_API_KEY=sk-...
    """
    from django.conf import settings
    
    # ========================================== OpenAI API 사용 가능 여부 체크 ====================
    # OpenAI 라이브러리가 설치되어 있는지 확인
    if not OPENAI_AVAILABLE:
        # 라이브러리가 없으면 규칙 기반으로 폴백 (기본 응답)
        return "🔧 OpenAI 라이브러리가 설치되지 않았습니다.\n\n설치 방법:\n1. 터미널을 엽니다\n2. pip install openai 실행\n3. 서버를 재시작합니다"
    
    # API 키가 설정되어 있는지 확인
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        # API 키가 없으면 안내 메시지
        return """🔑 OpenAI API 키가 설정되지 않았습니다.

설정 방법:
1. https://platform.openai.com/api-keys 에서 API 키 발급
2. 터미널에서 환경변수 설정:
   Windows: set OPENAI_API_KEY=sk-your-key-here
   Mac/Linux: export OPENAI_API_KEY=sk-your-key-here
3. 서버 재시작

또는 config/settings.py에서 직접 설정 가능합니다."""
    
    try:
        # ========================================== OpenAI 클라이언트 생성 ====================
        # 🔧 수정: JavaScript 코드와 동일한 방식으로 OpenAI 클라이언트 생성
        # JavaScript: const client = new OpenAI();
        # Python: client = OpenAI(api_key=...)
        client = OpenAI(api_key=api_key)
        
        # ========================================== AI에게 역할 부여 (System Prompt) ====================
        # AI가 어떤 역할을 할지 정의하는 중요한 부분
        system_prompt = """당신은 SafeMap 서비스의 친절한 AI 챗봇입니다.

SafeMap은 사건·사고 제보 및 안전 정보를 공유하는 커뮤니티 서비스입니다.

주요 기능:
- 🗺️ 지도: 지역별 사건사고 조회 (시/도 → 시/군/구 → 동 단계로 검색)
- 📍 신고하기: 위치 선택 + 카테고리(교통사고/폭력/화재/분실/기타) + 위험도(1~5) 입력
- 📝 게시판: 커뮤니티 게시글 작성/조회 (로그인 필수)
- 🔐 로그인/회원가입: 우측 상단 메뉴

답변 스타일:
- 친절하고 명확하게
- 이모지 적절히 사용
- 필요시 단계별로 설명
- 한국어로만 답변"""
        
        # ========================================== AI 응답 생성 ====================
        # 🔧 수정: JavaScript의 client.responses.create()와 유사한 방식
        # JavaScript: const response = await client.responses.create({...})
        # Python: response = client.chat.completions.create(...)
        response = client.chat.completions.create(
            model="gpt-4",  # 🔧 모델 선택: gpt-4 (더 똑똑) 또는 gpt-3.5-turbo (빠르고 저렴)
            messages=[
                # AI의 역할 정의
                {"role": "system", "content": system_prompt},
                # 사용자의 질문
                {"role": "user", "content": user_message}
            ],
            max_tokens=800,  # 최대 응답 길이 (토큰 수)
            temperature=0.7,  # 창의성 수준 (0~1, 높을수록 다양한 답변)
        )
        
        # ========================================== AI 응답 추출 및 반환 ====================
        # 🔧 JavaScript: console.log(response.output_text)
        # 🔧 Python: response.choices[0].message.content
        ai_message = response.choices[0].message.content
        
        # AI 응답 반환
        return ai_message
        
    except Exception as e:
        # ========================================== 오류 처리 ====================
        # API 호출 실패 시 사용자에게 친절한 오류 메시지
        error_message = str(e)
        
        # API 키 오류
        if "api_key" in error_message.lower():
            return "🔑 OpenAI API 키가 올바르지 않습니다. API 키를 확인해주세요."
        
        # 할당량 초과
        elif "quota" in error_message.lower():
            return "💳 OpenAI API 할당량이 초과되었습니다. 결제 정보를 확인해주세요."
        
        # 네트워크 오류
        elif "connection" in error_message.lower() or "timeout" in error_message.lower():
            return "🌐 OpenAI 서버와 연결할 수 없습니다. 인터넷 연결을 확인해주세요."
        
        # 기타 오류
        else:
            return f"❌ AI 응답 생성 중 오류가 발생했습니다:\n{error_message}\n\n잠시 후 다시 시도해주세요."


# ========================================== 규칙 기반 폴백 함수 (백업용) ====================
# 🔧 OpenAI API가 작동하지 않을 때를 대비한 백업 함수
# 필요하면 chatbot_api() 함수에서 이 함수를 호출하도록 변경 가능
def generate_ai_response_fallback(user_message):
    """
    규칙 기반 응답 생성 (OpenAI API 백업용)
    - OpenAI API가 작동하지 않을 때 사용
    - 키워드 매칭으로 간단한 응답 제공
    """
    message_lower = user_message.lower()
    
    if any(word in message_lower for word in ['안녕', 'hi', 'hello']):
        return "안녕하세요! 😊 SafeMap 챗봇입니다. 무엇을 도와드릴까요?"
    elif any(word in message_lower for word in ['기능', '뭐', '무엇']):
        return "저는 SafeMap의 사용법을 안내해드립니다. '신고 방법', '게시판 사용법', '지도 사용법' 등을 물어보세요!"
    elif any(word in message_lower for word in ['신고', '제보']):
        return "🚨 신고하기: 상단 메뉴 → 신고하기 → 지도에서 위치 선택 → 카테고리와 위험도 입력 → 제출"
    elif any(word in message_lower for word in ['게시판', '글']):
        return "📝 게시판: 상단 메뉴 → 게시판 → 글 작성 버튼 (로그인 필수)"
    elif any(word in message_lower for word in ['지도']):
        return "🗺️ 지도: 상단 메뉴 → 지도 → 시/도 선택 → 시/군/구 선택 → 동 선택"
    else:
        return f"'{user_message}'에 대해 잘 모르겠어요. 😅\n'기능', '신고 방법', '게시판', '지도'를 물어보세요!"
