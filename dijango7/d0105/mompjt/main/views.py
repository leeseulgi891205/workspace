# ═══════════════════════════════════════════════════════════════════════
# main/views.py
# 맘스로그 프로젝트 - 메인 페이지 및 통합 검색 뷰
# ═══════════════════════════════════════════════════════════════════════
# 작성일: 2025-12-29
# 기능:
#   1. index: 메인 페이지 렌더링 (배너, 인기글, 로그인 박스)
#   2. search: 통합 검색 (공지사항, 자유게시판, 벼룩시장 전체 검색)
# ═══════════════════════════════════════════════════════════════════════

import json
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from itertools import chain
from operator import attrgetter
# 게시판 모델 import (Notice, FreePost, FleaItem, HotDeal)  # 26-01-02 슬기 추가: HotDeal
from board.models import Notice, FreePost, FleaItem, HotDeal, ParentingInfo
from .models import GrowthRecord
from .forms import GrowthRecordForm

# ───────────────────────────────────────────────────────────────────────
# 메인 페이지
# ───────────────────────────────────────────────────────────────────────
# 26-01-02 슬기 수정: 실시간 인기글 실제 데이터 표시
def index(request):
    """
    맘스로그 메인 페이지
    - 배너 슬라이더 (이벤트/핫딜 게시판에서 동적 로드)
    - 실시간 인기글 표시 (조회수 기준 상위 14개)
    - 로그인/로그아웃 박스
    """
    # 배너용: HotDeal과 ParentingInfo에서 최신순 상위 5개씩 가져오기
    banner_posts = []
    
    # HotDeal 글 (이벤트/체험단) - 상위 3개
    hotdeals = HotDeal.objects.filter(category='event').order_by('-created_at')[:3]
    for post in hotdeals:
        post.post_type = 'hotdeal'
        post.post_url = f'/board/hotdeal/{post.pk}/'
        banner_posts.append(post)
    
    # ParentingInfo 글 - 상위 2개
    parentings = ParentingInfo.objects.all().order_by('-created_at')[:2]
    for post in parentings:
        post.post_type = 'parenting'
        post.post_url = f'/board/parenting/{post.pk}/'
        banner_posts.append(post)
    
    # 전체 게시판에서 조회수 높은 순으로 14개 가져오기
    free_posts = FreePost.objects.all()
    flea_items = FleaItem.objects.all()
    
    # 각 객체에 post_type 속성 추가
    for post in free_posts:
        post.post_type = 'free'
    for post in flea_items:
        post.post_type = 'flea'
    
    # 합치고 조회수 기준 정렬
    hot_posts = list(chain(free_posts, flea_items))
    hot_posts = sorted(hot_posts, key=lambda x: x.views, reverse=True)[:14]
    
    context = {
        'banner_posts': banner_posts,
        'hot_posts': hot_posts,
    }
    return render(request, 'main/index.html', context)


# ───────────────────────────────────────────────────────────────────────
# 성장 기록 그래프 (Chart.js) - 월령별 발달 지표
# 26-01-04 슬기 재작성: 키/몸무게 → 월령별 발달지표로 전환
# ───────────────────────────────────────────────────────────────────────
@login_required(login_url='accounts:login')
def growth_chart(request):
    """
    월령별 발달 지표를 라인 그래프 + 평균 밴드로 표시
    - 신체발달, 인지발달, 언어발달, 사회성발달 4가지 영역
    - ParentingInfo 모델에서 category별 최신 점수 추출
    """
    
    # ParentingInfo에서 사용자의 발달 기록 가져오기
    developments = ParentingInfo.objects.filter(author=request.user).order_by('month_age')
    
    if not developments.exists():
        context = {'developments': None}
        return render(request, 'main/growth_chart.html', context)
    
    # 월령 추출 (1~12개월)
    months = []
    physical_scores = []
    cognitive_scores = []
    language_scores = []
    social_scores = []
    
    # 카테고리별로 최신 데이터만 추출
    for month in range(1, 13):
        dev_data = {}
        
        # 신체발달 (월령별 최신 1개만)
        physical = developments.filter(month_age=month, category='신체발달').order_by('-created_at').first()
        if physical:
            dev_data['physical'] = int(physical.physical_score) if physical.physical_score else 50
        
        # 인지발달
        cognitive = developments.filter(month_age=month, category='인지발달').order_by('-created_at').first()
        if cognitive:
            dev_data['cognitive'] = int(cognitive.cognitive_score) if cognitive.cognitive_score else 50
        
        # 언어발달
        language = developments.filter(month_age=month, category='언어발달').order_by('-created_at').first()
        if language:
            dev_data['language'] = int(language.language_score) if language.language_score else 50
        
        # 사회성발달
        social = developments.filter(month_age=month, category='사회성발달').order_by('-created_at').first()
        if social:
            dev_data['social'] = int(social.social_score) if social.social_score else 50
        
        # 최소 1개 이상의 발달 데이터가 있으면 포함
        if dev_data:
            months.append(month)
            physical_scores.append(dev_data.get('physical', 50))
            cognitive_scores.append(dev_data.get('cognitive', 50))
            language_scores.append(dev_data.get('language', 50))
            social_scores.append(dev_data.get('social', 50))
    
    # 전국 평균값 (대한소아과학회 기준)
    avg_months = list(range(1, 13))
    avg_physical = [42, 48, 54, 60, 66, 72, 76, 80, 84, 88, 92, 96]
    avg_cognitive = [40, 46, 52, 58, 64, 70, 74, 78, 82, 86, 90, 94]
    avg_language = [35, 42, 49, 56, 63, 70, 76, 82, 88, 92, 96, 100]
    avg_social = [38, 45, 52, 59, 66, 73, 79, 85, 91, 94, 97, 100]
    
    context = {
        'developments': developments if developments.exists() else None,
        'months_json': json.dumps(months, ensure_ascii=False),
        'physical_json': json.dumps(physical_scores),
        'cognitive_json': json.dumps(cognitive_scores),
        'language_json': json.dumps(language_scores),
        'social_json': json.dumps(social_scores),
        'avg_months_json': json.dumps(avg_months, ensure_ascii=False),
        'avg_physical_json': json.dumps(avg_physical),
        'avg_cognitive_json': json.dumps(avg_cognitive),
        'avg_language_json': json.dumps(avg_language),
        'avg_social_json': json.dumps(avg_social),
    }
    return render(request, 'main/growth_chart.html', context)

# ───────────────────────────────────────────────────────────────────────
# 통합 검색 (공지사항 + 자유게시판 + 벼룩시장 + 핫딜공유)
# 25-12-29 슬기 수정: 공지사항 검색 추가
# 26-01-02 슬기 수정: 핫딜공유 검색 추가
# ───────────────────────────────────────────────────────────────────────
def search(request):
    """
    전체 게시판 통합 검색
    - 공지사항: 제목, 내용 검색
    - 자유게시판: 제목, 내용 검색
    - 벼룩시장: 제목, 설명 검색
    - 핫딜공유: 제목, 내용 검색
    - 결과는 최신순으로 정렬하여 반환
    """
    query = request.GET.get('q', '')
    posts = []

    if query:
        # 1. 공지사항 검색 (제목, 내용)
        notice_results = Notice.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        # 꼬리표 달기 (템플릿에서 게시판 구분용)
        for post in notice_results:
            post.board_type = 'notice'

        # 2. 자유게시판 검색 (제목, 내용)
        free_results = FreePost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        for post in free_results:
            post.board_type = 'free'

        # 3. 벼룩시장 검색 (제목, 설명)
        flea_results = FleaItem.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        for post in flea_results:
            post.board_type = 'flea'

        # 4. 핫딜공유 검색 (제목, 내용)  # 26-01-02 슬기 추가
        hotdeal_results = HotDeal.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        for post in hotdeal_results:
            post.board_type = 'hotdeal'

        # 5. 결과 합치기
        posts = list(chain(notice_results, free_results, flea_results, hotdeal_results))

        # 6. 최신순 정렬 (created_at 기준)
        posts.sort(key=attrgetter('created_at'), reverse=True)

    context = {
        'posts': posts,
        'q': query,
    }
    return render(request, 'main/search_result.html', context)