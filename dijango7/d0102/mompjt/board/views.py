# ═══════════════════════════════════════════════════════════════════════
# board/views.py
# 맘스로그 프로젝트 - 게시판 뷰 (공지사항, 자유게시판, 벼룩시장)
# ═══════════════════════════════════════════════════════════════════════
# 작성일: 2025-12-29
# 기능:
#   [공지사항] notice_list, notice_detail, notice_write (관리자 전용)
#   [자유게시판] free_list, free_create
#   [벼룩시장] flea_list, flea_detail, flea_create, flea_edit, flea_delete
#   [벼룩시장 찜] flea_like_toggle (25-12-29 추가)
#   [벼룩시장 댓글] flea_comment_create, flea_comment_edit, flea_comment_delete (25-12-29 추가)
#   [벼룩시장 검색] flea_list에 통합 (제목, 내용, 작성자 검색)
# ═══════════════════════════════════════════════════════════════════════

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from .models import Notice, FreePost, FleaItem, FleaComment, Notification, FreePostReaction
from .forms import NoticeForm, FreePostForm, FleaItemForm, FleaCommentForm
from django.core.paginator import Paginator   # 25-12-29 혜은 추가
# 25-12-30 민혁 추가 펫 게시판 임포트
from .models import Notice, FreePost, FleaItem, FleaComment, Notification, PetPost
from django.db.models import F
from .models import PetPost, PetComment
from django.contrib.auth.decorators import login_required

# 1. 목록 보기
def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at') # 최신글 순서
    return render(request, 'board/notice_list.html', {'notices': notices})

# 2. 상세 보기
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    
    # 조회수 +1 증가
    notice.view_count += 1
    notice.save()
    
    return render(request, 'board/notice_detail.html', {'notice': notice})

# ★ 글쓰기 기능 추가
@login_required # 로그인은 필수
def notice_write(request):
    # 관리자가 아니면 메인으로 쫓아냄
    if not request.user.is_staff:
        return redirect('board:notice_list')

    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            # notice.writer = request.user  # (작성자 필드가 있다면 추가)
            notice.save()
            return redirect('board:notice_list')
    else:
        form = NoticeForm()
    
    return render(request, 'board/notice_write.html', {'form': form})


# ▼▼▼ [자유게시판] ▼▼▼ ============================================================
# 25-12-31 혜은 : 게시글 상세보기 추가

# 1. 자유게시판 목록 보기
def free_list(request):
    # 카테고리 파라미터 가져오기 (기본값: 'all')
    selected_category = request.GET.get('category', 'all')
    
    # 카테고리별 제목
    category_titles = {
        'all': '자유게시판 - 전체보기',
        'mom': '자유게시판 - 육아수다',
        'husband': '자유게시판 - 남편뒷담화',
        'family': '자유게시판 - 시댁/친정',
        'preg': '자유게시판 - 임신출산',
        'bamboo': '자유게시판 - 대나무숲',
    }
    category_title = category_titles.get(selected_category, '자유게시판')
    
    # 카테고리 필터링
    if selected_category == 'all':
        posts = FreePost.objects.all().order_by('-created_at')
    else:
        posts = FreePost.objects.filter(category=selected_category).order_by('-created_at')

    # 총 게시글 개수
    total_count = posts.count()

    # 한 페이지에 5개씩
    per_page = 5
    paginator = Paginator(posts, per_page)

    # 현재 페이지 번호 (?page=1, ?page=2 ...)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)

    # 현재 페이지 번호 (정수)
    current_page = page_obj.number

    # 이 페이지의 첫 번째 글 번호 (전체 기준)
    start_number = total_count - per_page * (current_page - 1)

    # 각 post 객체에 번호를 붙여준다
    for idx, post in enumerate(page_obj.object_list):
        post.number = start_number - idx

    # 페이지네이션: 5개씩만 표시
    total_pages = paginator.num_pages
    current_page = page_obj.number
    
    # 현재 페이지를 중심으로 5개 표시
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, start_page + 4)
    
    # start_page가 너무 뒤에 있으면 조정
    if end_page - start_page < 4:
        start_page = max(1, end_page - 4)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'total_count': total_count,
        'selected_category': selected_category,
        'category_title': category_title,
        'start_page': start_page,
        'end_page': end_page,
    }
    return render(request, 'board/free_list.html', context)

# 2. 글쓰기 (로그인한 사람만 가능)
@login_required(login_url='accounts:login')
def free_create(request):
    if request.method == 'POST':
        form = FreePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 임시 저장
            post.author = request.user     # 작성자 = 현재 로그인한 사람
            
            # 대나무숲 카테고리는 자동 익명 처리
            if post.category == 'bamboo':
                post.is_anonymous = True
            # 다른 카테고리는 체크박스에 따라
            else:
                post.is_anonymous = request.POST.get('is_anonymous') == 'on'
            
            post.save()                    # 진짜 저장
            return redirect('board:free_list') # 저장 후 목록으로 이동
    else:
        form = FreePostForm()
    
    return render(request, 'board/free_write.html', {'form': form})

# 3. 상세 보기                                    ==== 25-12-31 혜은 추가 ====
def free_detail(request, pk):
    # 상세에 보여줄 글 하나
    post = get_object_or_404(FreePost, pk=pk)

    # 조회수 +1 (FreePost에 views 필드가 있을 때)
    if hasattr(post, 'views'):
        post.views += 1
        post.save(update_fields=['views'])

    # ▼▼▼ 아래부터: 상세 페이지 하단에 보여줄 "자유게시판 목록" ▼▼▼
    
    # 카테고리 파라미터 가져오기
    selected_category = request.GET.get('category', 'all')

    # 카테고리 필터링
    if selected_category == 'all':
        qs = FreePost.objects.all().order_by('-created_at')
    else:
        qs = FreePost.objects.filter(category=selected_category).order_by('-created_at')

    # 총 게시글 개수
    total_count = qs.count()

    # 한 페이지에 5개씩
    per_page = 5
    paginator = Paginator(qs, per_page)

    # 목록에서 넘어온 page 값 사용 (없으면 1페이지)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 번호 계산 (전체 기준 번호) -> item.number 로 사용
    start_number = total_count - per_page * (page_obj.number - 1)
    for idx, item in enumerate(page_obj.object_list):
        item.number = start_number - idx

    # 페이지네이션: 5개씩만 표시
    total_pages = paginator.num_pages
    current_page = page_obj.number
    
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, start_page + 4)
    
    if end_page - start_page < 4:
        start_page = max(1, end_page - 4)

    context = {
        'post': post,           # 상세 글
        'posts': page_obj,      # 하단 목록에서 for item in posts
        'page_obj': page_obj,   # 하단 페이지 번호
        'total_count': total_count,
        'selected_category': selected_category,
        'start_page': start_page,
        'end_page': end_page,
    }
    return render(request, 'board/free_detail.html', context)

# 4. 수정하기                                   ==== 25-12-31 혜은 추가 ====
@login_required(login_url='accounts:login')
def free_update(request, pk):
    post = get_object_or_404(FreePost, pk=pk)

    # 작성자 또는 관리자만 수정 가능
    if request.user != post.author and not request.user.is_staff:
        return redirect('board:free_detail', pk=pk)

    if request.method == 'POST':
        form = FreePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board:free_detail', pk=pk)
    else:
        form = FreePostForm(instance=post)

    return render(request, 'board/free_write.html', {
        'form': form,
        'post': post,
        'is_edit': True,   # 수정 모드 표시용
    })

# 5. 삭제하기                                   ==== 25-12-31 혜은 추가 ====
@login_required(login_url='accounts:login')
def free_delete(request, pk):
    post = get_object_or_404(FreePost, pk=pk)

    # 작성자 또는 관리자만 삭제 가능
    if request.user != post.author and not request.user.is_staff:
        return redirect('board:free_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('board:free_list')

    # GET으로 들어오면 그냥 상세로 돌려보냄
    return redirect('board:free_detail', pk=pk)


# 6. 감정 리액션 추가/제거 (AJAX)              ==== 26-01-02 추가 ====
def free_reaction_toggle(request, pk):
    """
    AJAX로 감정 리액션을 토글합니다.
    POST 요청: reaction_type=empathy|courage|cheer|support|thanks
    """
    # 로그인 확인
    if not request.user.is_authenticated:
        return JsonResponse({'error': '로그인 필요'}, status=401)
    
    # POST 요청 확인
    if request.method != 'POST':
        return JsonResponse({'error': 'POST 요청만 허용'}, status=400)
    
    post = get_object_or_404(FreePost, pk=pk)
    reaction_type = request.POST.get('reaction_type', '').strip()
    
    # 유효한 리액션 타입 확인
    valid_types = ['empathy', 'courage', 'cheer', 'support', 'thanks']
    if reaction_type not in valid_types:
        return JsonResponse({'error': '유효하지 않은 리액션 타입'}, status=400)
    
    # 필드명 매핑
    field_map = {
        'empathy': 'reaction_empathy',
        'courage': 'reaction_courage',
        'cheer': 'reaction_cheer',
        'support': 'reaction_support',
        'thanks': 'reaction_thanks',
    }
    field_name = field_map[reaction_type]
    
    # 기존 리액션 확인
    reaction, created = FreePostReaction.objects.get_or_create(
        post=post,
        user=request.user,
        reaction_type=reaction_type
    )
    
    # 이미 있으면 제거 (토글)
    if not created:
        reaction.delete()
        # 카운트 감소
        setattr(post, field_name, max(0, getattr(post, field_name) - 1))
        is_active = False
    else:
        # 새로 추가되면 카운트 증가
        setattr(post, field_name, getattr(post, field_name) + 1)
        is_active = True
    
    post.save()
    
    # 현재 리액션 카운트 반환
    return JsonResponse({
        'success': True,
        'is_active': is_active,
        'counts': {
            'empathy': post.reaction_empathy,
            'courage': post.reaction_courage,
            'cheer': post.reaction_cheer,
            'support': post.reaction_support,
            'thanks': post.reaction_thanks,
        }
    })
# =============================================================================

# 25-12-30 민혁 추가-----------------------------------------
# ▼▼▼ [반려동물 게시판 뷰] ▼▼▼
def pet_list(request):
    posts = PetPost.objects.all().order_by('-created_at')

    return render(request, 'board/pet_list.html', {
        'posts': posts
    })
    
# 25-12-30 민혁 추가-----------------------------------------    
# ▼▼▼ [반려동물 게시판 글쓰기] ▼▼▼
@login_required(login_url='accounts:login')
def pet_write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        PetPost.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            image=request.FILES.get('image'),  # 🔥 핵심
            author=request.user
        )

        return redirect('board:pet_list')

    return render(request, 'board/pet_write.html')
# ▼▼▼ [반려동물 게시판 상세보기] ▼▼▼
def pet_detail(request, pk):
    post = get_object_or_404(PetPost, pk=pk)

    # 조회수 증가 (F() 사용 → 동시성 안전)
    PetPost.objects.filter(pk=pk).update(views=F('views') + 1)
    post.refresh_from_db()

    return render(request, 'board/pet_detail.html', {
        'post': post
    })
# 25-12-30 민혁 추가-----------------------------------------
@login_required(login_url='accounts:login')
def pet_edit(request, pk):
    """
    반려동물 게시판 글 수정 (작성자만 가능)
    """
    post = get_object_or_404(PetPost, pk=pk)

    if request.user != post.author:
        return redirect('board:pet_detail', pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('board:pet_detail', pk=pk)
    
    if request.FILES.get('image'):
        post.image = request.FILES.get('image')
        post.save()
        

    return render(request, 'board/pet_edit.html', {'post': post})

#25-12-31 민혁 추가-----------------------------------------
#▼▼▼ [반려동물 게시판 삭제] ▼▼▼
@login_required(login_url='accounts:login')
def pet_delete(request, pk):
    post = get_object_or_404(PetPost, pk=pk)

    if request.user != post.author:
        return redirect('board:pet_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('board:pet_list')

    # GET 요청은 상세보기로 돌려보냄
    return redirect('board:pet_detail', pk=pk)

# ─────────────────────────────────────────
# 반려동물 게시판 댓글 작성
# ─────────────────────────────────────────
@login_required(login_url='accounts:login')
def pet_comment_create(request, pk):
    post = get_object_or_404(PetPost, pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')

        comment = PetComment.objects.create(
            post=post,
            author=request.user,
            content=content,
            parent_id=parent_id if parent_id else None
        )
        
        # ✅ 글 작성자에게 댓글 알림 생성
        if post.author != request.user:
            Notification.objects.create(
                user=post.author,
                pet_post=post,
                message=f"{request.user.nickname}님이 댓글을 남겼습니다.",
                is_read=False
            )

    return redirect('board:pet_detail', pk=pk)

# ─────────────────────────────────────────
# 반려동물 게시판 댓글 삭제 (POST 전용)
# ─────────────────────────────────────────
@login_required(login_url='accounts:login')
def pet_comment_delete(request, pk, comment_id):
    post = get_object_or_404(PetPost, pk=pk)
    comment = get_object_or_404(PetComment, pk=comment_id, post=post)

    # 작성자만 삭제 가능
    if request.user != comment.author:
        return redirect('board:pet_detail', pk=pk)

    if request.method == 'POST':
        comment.delete()

    return redirect('board:pet_detail', pk=pk)
# ─────────────────────────────────────────
# 반려동물 게시판 댓글 수정 (POST 전용)
# ─────────────────────────────────────────
@login_required(login_url='accounts:login')
def pet_comment_edit(request, pk, comment_id):
    post = get_object_or_404(PetPost, pk=pk)
    comment = get_object_or_404(PetComment, pk=comment_id, post=post)

    # 작성자만 수정 가능
    if request.user != comment.author:
        return redirect('board:pet_detail', pk=pk)

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content:
            comment.content = content
            comment.save()

    return redirect('board:pet_detail', pk=pk)
    
#25-12-31 민혁 추가-----------------------------------------

# ▼▼▼ [벼룩시장] ▼▼▼
# 25-12-29 슬기 수정: 검색 기능 추가 (제목, 내용, 작성자명, 닉네임 검색)
def flea_list(request):
    # 검색 기능
    search_query = request.GET.get('search', '').strip()
    
    # 전체 아이템 가져오기
    all_items = FleaItem.objects.select_related('author').prefetch_related('liked_by').all()
    
    # 검색어가 있으면 필터링
    if search_query:
        items = all_items.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(author__username__icontains=search_query) |
            Q(author__nickname__icontains=search_query)
        )
        # 디버깅: 검색 결과 출력
        print(f"[검색] 검색어: '{search_query}', 전체: {all_items.count()}건, 검색결과: {items.count()}건")
        for item in items[:5]:  # 최대 5개만 출력
            print(f"  - {item.title} (작성자: {item.author.nickname or item.author.username})")
    else:
        items = all_items
    
    # 25-12-29 슬기 수정: 로그인한 사용자의 찜 목록 조회
    liked_items = None
    if request.user.is_authenticated:
        liked_items = FleaItem.objects.filter(liked_by=request.user).select_related('author')

    return render(request, 'board/flea_list.html', {
        'items': items,
        'liked_items': liked_items,
        'search_query': search_query,
    })

# 25-12-29 슬기 수정: 댓글 목록 추가, 댓글 폼 전달
def flea_detail(request, pk):
    item = get_object_or_404(FleaItem.objects.select_related('author'), pk=pk)
    comments = item.comments.select_related('author')
    form = FleaCommentForm()

    return render(request, 'board/flea_detail.html', {
        'item': item,
        'comments': comments,
        'comment_form': form,
    })

@login_required(login_url='accounts:login')
# 25-12-29 슬기 수정: 찜하기/취소 토글 기능 구현
def flea_like_toggle(request, pk):
    item = get_object_or_404(FleaItem, pk=pk)

    if request.user in item.liked_by.all():
        item.liked_by.remove(request.user)
    else:
        item.liked_by.add(request.user)

    return redirect('board:flea_detail', pk=pk)

@login_required(login_url='accounts:login')
# 25-12-29 슬기 수정: 댓글 작성 (닉네임 자동 설정, 비밀글 비밀번호 검증)
def flea_comment_create(request, pk):
    item = get_object_or_404(FleaItem, pk=pk)

    if request.method == 'POST':
        form = FleaCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.flea_item = item
            comment.nickname = getattr(request.user, 'nickname', None) or request.user.username
            comment.save()
            
            # 25-12-29 슬기 수정: 게시글 작성자에게 알림 생성
            if request.user != item.author:  # 자신의 글에는 알림 없음
                Notification.objects.create(
                    user=item.author,  # 글 작성자에게 알림
                    flea_item=item,
                    message=f"{comment.nickname}님이 댓글을 남겼습니다.",
                    is_read=False
                )
        else:
            comments = item.comments.select_related('author')
            return render(request, 'board/flea_detail.html', {
                'item': item,
                'comments': comments,
                'comment_form': form,
            })

    return redirect('board:flea_detail', pk=pk)

@login_required(login_url='accounts:login')
def flea_create(request):
    if request.method == 'POST':
        form = FleaItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('board:flea_list')
    else:
        form = FleaItemForm()

    return render(request, 'board/flea_write.html', {'form': form})

@login_required(login_url='accounts:login')
def flea_edit(request, pk):
    item = get_object_or_404(FleaItem, pk=pk)
    
    # 작성자만 수정 가능
    if request.user != item.author:
        return redirect('board:flea_detail', pk=pk)
    
    if request.method == 'POST':
        form = FleaItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('board:flea_detail', pk=pk)
    else:
        form = FleaItemForm(instance=item)
    
    return render(request, 'board/flea_write.html', {'form': form, 'item': item})

@login_required(login_url='accounts:login')
def flea_delete(request, pk):
    item = get_object_or_404(FleaItem, pk=pk)
    
    # 작성자만 삭제 가능
    if request.user != item.author:
        return redirect('board:flea_detail', pk=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('board:flea_list')
    
    return render(request, 'board/flea_delete.html', {'item': item})

@login_required(login_url='accounts:login')
# 25-12-29 슬기 수정: 댓글 수정 (작성자만 가능, 닉네임 유지)
def flea_comment_edit(request, pk, comment_id):
    item = get_object_or_404(FleaItem, pk=pk)
    comment = get_object_or_404(FleaComment, pk=comment_id, flea_item=item)

    if request.user != comment.author and not request.user.is_staff:
        return redirect('board:flea_detail', pk=pk)

    if request.method == 'POST':
        form = FleaCommentForm(request.POST, instance=comment)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.nickname = getattr(request.user, 'nickname', None) or request.user.username
            updated.save()
            return redirect('board:flea_detail', pk=pk)
    else:
        form = FleaCommentForm(instance=comment)

    return render(request, 'board/flea_comment_form.html', {
        'form': form,
        'item': item,
        'comment': comment,
        'mode': 'edit',
    })

@login_required(login_url='accounts:login')
# 25-12-29 슬기 수정: 댓글 삭제 (작성자만 가능)
def flea_comment_delete(request, pk, comment_id):
    item = get_object_or_404(FleaItem, pk=pk)
    comment = get_object_or_404(FleaComment, pk=comment_id, flea_item=item)

    if request.user != comment.author and not request.user.is_staff:
        return redirect('board:flea_detail', pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('board:flea_detail', pk=pk)

    return render(request, 'board/flea_comment_delete.html', {
        'item': item,
        'comment': comment,
    })

# 25-12-29 슬기 수정: AJAX 상태 변경 (드롭다운 메뉴 선택)
@login_required(login_url='accounts:login')
def flea_status_update(request, pk):
    item = get_object_or_404(FleaItem, pk=pk)
    
    # 작성자만 상태 변경 가능
    if request.user != item.author:
        return JsonResponse({'success': False, 'error': '작성자만 변경 가능합니다.'}, status=403)
    
    if request.method == 'POST':
        # POST 데이터에서 새로운 상태 받기
        new_status = request.POST.get('status', item.status)
        
        # 유효한 상태 확인
        valid_statuses = ['selling', 'reserved', 'sold']
        if new_status not in valid_statuses:
            return JsonResponse({'success': False, 'error': '유효하지 않은 상태입니다.'}, status=400)
        
        item.status = new_status
        item.save()
        
        # 상태명 맵핑
        status_labels = {
            'selling': '판매중',
            'reserved': '예약중',
            'sold': '판매완료'
        }
        
        return JsonResponse({
            'success': True,
            'new_status': new_status,
            'status_label': status_labels[new_status]
        })
    
    return JsonResponse({'success': False, 'error': 'POST 요청만 가능합니다.'}, status=400)

# 25-12-29 슬기 수정: 알림 목록 조회
@login_required(login_url='accounts:login')
def notification_list(request):
    notifications = request.user.notifications.all().order_by('-created_at')
    
    # 각 알림에 대해 post 타입에 맞는 URL 생성
    notifications_with_url = []
    for notification in notifications:
        notifications_with_url.append({
            'notification': notification,
            'target_url': notification.get_post_url()
        })
    
    return render(request, 'board/notification_list.html', {'notifications_with_url': notifications_with_url})

# 25-12-29 슬기 수정: 알림 읽음 처리 (AJAX)
@login_required(login_url='accounts:login')
def notification_mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id, user=request.user)
    
    if request.method == 'POST':
        notification.is_read = True
        notification.save()
        
        # 읽지 않은 알림 개수 반환
        unread_count = request.user.notifications.filter(is_read=False).count()
        
        return JsonResponse({
            'success': True,
            'unread_count': unread_count
        })
    
    return JsonResponse({'success': False, 'error': 'POST 요청만 가능합니다.'}, status=400)

# 25-12-29 슬기 수정: 모든 알림 읽음 처리 (AJAX)
@login_required(login_url='accounts:login')
def notification_mark_all_read(request):
    if request.method == 'POST':
        request.user.notifications.filter(is_read=False).update(is_read=True)
        
        return JsonResponse({
            'success': True,
            'unread_count': 0
        })
    
    return JsonResponse({'success': False, 'error': 'POST 요청만 가능합니다.'}, status=400)


# ▼▼▼ [핫딜공유 게시판] ▼▼▼ ============================================================

# 1. 핫딜 목록
def hotdeal_list(request):
    from .models import HotDeal
    category = request.GET.get('category', 'all')
    
    if category and category != 'all':
        posts = HotDeal.objects.filter(category=category).order_by('-created_at')
    else:
        posts = HotDeal.objects.all().order_by('-created_at')
    
    # 페이지네이션
    per_page = 10
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    total_count = posts.count()
    current_page = page_obj.number
    start_number = total_count - per_page * (current_page - 1)
    
    for idx, post in enumerate(page_obj.object_list):
        post.number = start_number - idx
    
    context = {
        'posts': page_obj,
        'category': category,
    }
    return render(request, 'board/hotdeal_list.html', context)


# 2. 핫딜 작성
@login_required(login_url='accounts:login')
def hotdeal_create(request):
    from .models import HotDeal
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category', 'all')
        link = request.POST.get('link', '')
        price = request.POST.get('price', '')
        
        HotDeal.objects.create(
            title=title,
            content=content,
            category=category,
            link=link,
            price=price,
            author=request.user
        )
        return redirect('board:hotdeal_list')
    
    return render(request, 'board/hotdeal_form.html')


# 3. 핫딜 상세보기
def hotdeal_detail(request, pk):
    from .models import HotDeal
    post = get_object_or_404(HotDeal, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'board/hotdeal_detail.html', {'post': post})


# 4. 핫딜 수정
@login_required(login_url='accounts:login')
def hotdeal_update(request, pk):
    from .models import HotDeal
    post = get_object_or_404(HotDeal, pk=pk)
    
    if post.author != request.user:
        return redirect('board:hotdeal_detail', pk=pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category = request.POST.get('category', 'all')
        post.link = request.POST.get('link', '')
        post.price = request.POST.get('price', '')
        post.save()
        return redirect('board:hotdeal_detail', pk=pk)
    
    return render(request, 'board/hotdeal_form.html', {'post': post})


# 5. 핫딜 삭제
@login_required(login_url='accounts:login')
def hotdeal_delete(request, pk):
    from .models import HotDeal
    post = get_object_or_404(HotDeal, pk=pk)
    
    if post.author != request.user:
        return redirect('board:hotdeal_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('board:hotdeal_list')
    
    return render(request, 'board/hotdeal_detail.html', {'post': post})


# ───────────────────────────────────────────────────────────────────────
# [육아정보] 게시판 뷰 함수들
# 26-01-02 슬기 추가: 육아정보 게시판 전체 기능 (목록, 작성, 상세, 수정, 삭제)
# ───────────────────────────────────────────────────────────────────────
def parenting_list(request):
    from .models import ParentingInfo
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        posts = ParentingInfo.objects.all()
    else:
        posts = ParentingInfo.objects.filter(category=category)
    
    # 페이지네이션
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    # 번호 계산
    start_number = (posts.number - 1) * paginator.per_page + 1
    for idx, post in enumerate(posts):
        post.number = start_number + idx
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'board/parenting_list.html', context)


@login_required(login_url='accounts:login')
def parenting_create(request):
    from .models import ParentingInfo
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        
        # 월령별 발달 데이터 처리
        month_age = request.POST.get('month_age')
        physical_score = request.POST.get('physical_score')
        cognitive_score = request.POST.get('cognitive_score')
        language_score = request.POST.get('language_score')
        social_score = request.POST.get('social_score')
        
        ParentingInfo.objects.create(
            title=title,
            content=content,
            category=category,
            author=request.user,
            month_age=int(month_age) if month_age else None,
            physical_score=int(physical_score) if physical_score else None,
            cognitive_score=int(cognitive_score) if cognitive_score else None,
            language_score=int(language_score) if language_score else None,
            social_score=int(social_score) if social_score else None,
        )
        return redirect('board:parenting_list')
    
    return render(request, 'board/parenting_form.html')


def parenting_detail(request, pk):
    from .models import ParentingInfo
    post = get_object_or_404(ParentingInfo, pk=pk)
    post.views += 1
    post.save()
    return render(request, 'board/parenting_detail.html', {'post': post})


@login_required
def parenting_update(request, pk):
    from .models import ParentingInfo
    post = get_object_or_404(ParentingInfo, pk=pk)
    
    if post.author != request.user:
        return redirect('board:parenting_detail', pk=pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category = request.POST.get('category')
        
        # 월령별 발달 데이터 업데이트
        month_age = request.POST.get('month_age')
        physical_score = request.POST.get('physical_score')
        cognitive_score = request.POST.get('cognitive_score')
        language_score = request.POST.get('language_score')
        social_score = request.POST.get('social_score')
        
        post.month_age = int(month_age) if month_age else None
        post.physical_score = int(physical_score) if physical_score else None
        post.cognitive_score = int(cognitive_score) if cognitive_score else None
        post.language_score = int(language_score) if language_score else None
        post.social_score = int(social_score) if social_score else None
        
        post.save()
        return redirect('board:parenting_detail', pk=pk)
    
    return render(request, 'board/parenting_form.html', {'post': post})


@login_required
def parenting_delete(request, pk):
    from .models import ParentingInfo
    post = get_object_or_404(ParentingInfo, pk=pk)
    
    if post.author != request.user:
        return redirect('board:parenting_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('board:parenting_list')
    
    return redirect('board:parenting_detail', pk=pk)


# 26-01-02 슬기 추가: 월령별 발달 차트 (사용자별 분리 + 평균치 표시)
@login_required(login_url='accounts:login')
def development_chart(request):
    import json
    from django.db.models import Avg
    from .models import ParentingInfo
    
    # 현재 로그인한 사용자의 월령별 발달 데이터만 가져오기 (월령 오름차순)
    developments = ParentingInfo.objects.filter(
        author=request.user,
        category='development',
        month_age__isnull=False
    ).order_by('month_age')
    
    # 차트용 데이터 준비 (사용자 데이터)
    months = [dev.month_age for dev in developments]
    physical = [dev.physical_score or 0 for dev in developments]
    cognitive = [dev.cognitive_score or 0 for dev in developments]
    language = [dev.language_score or 0 for dev in developments]
    social = [dev.social_score or 0 for dev in developments]
    
    # 전체 사용자의 월령별 평균 데이터 계산
    all_months = ParentingInfo.objects.filter(
        category='development',
        month_age__isnull=False
    ).values('month_age').distinct().order_by('month_age')
    
    avg_months = []
    avg_physical = []
    avg_cognitive = []
    avg_language = []
    avg_social = []
    
    for month_data in all_months:
        month = month_data['month_age']
        avg_data = ParentingInfo.objects.filter(
            category='development',
            month_age=month
        ).aggregate(
            avg_physical=Avg('physical_score'),
            avg_cognitive=Avg('cognitive_score'),
            avg_language=Avg('language_score'),
            avg_social=Avg('social_score')
        )
        
        avg_months.append(month)
        avg_physical.append(round(avg_data['avg_physical'] or 0, 1))
        avg_cognitive.append(round(avg_data['avg_cognitive'] or 0, 1))
        avg_language.append(round(avg_data['avg_language'] or 0, 1))
        avg_social.append(round(avg_data['avg_social'] or 0, 1))
    
    context = {
        'developments': developments,
        'months_json': json.dumps(months),
        'physical_json': json.dumps(physical),
        'cognitive_json': json.dumps(cognitive),
        'language_json': json.dumps(language),
        'social_json': json.dumps(social),
        # 평균 데이터 추가
        'avg_months_json': json.dumps(avg_months),
        'avg_physical_json': json.dumps(avg_physical),
        'avg_cognitive_json': json.dumps(avg_cognitive),
        'avg_language_json': json.dumps(avg_language),
        'avg_social_json': json.dumps(avg_social),
    }
    return render(request, 'board/development_chart.html', context)

# ★ 엄마 마음 케어 일기장 (26-01-02 추가)
import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.GOOGLE_API_KEY)

@login_required
def diary_list(request):
    """엄마 마음 케어 일기장 리스트"""
    from .models import MomDiary, DiaryEntry
    
    diary, created = MomDiary.objects.get_or_create(user=request.user)
    entries = diary.entries.all()
    
    # 필터링
    mood_filter = request.GET.get('mood', '')
    search_query = request.GET.get('q', '')
    
    if mood_filter:
        entries = entries.filter(mood=mood_filter)
    if search_query:
        entries = entries.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    
    context = {
        'diary': diary,
        'entries': entries,
        'mood_filter': mood_filter,
        'search_query': search_query,
        'mood_choices': DiaryEntry.MOOD_CHOICES,
    }
    return render(request, 'board/diary_list.html', context)


@login_required
def diary_create(request):
    """새 일기 작성"""
    from .models import MomDiary, DiaryEntry
    
    diary, created = MomDiary.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        mood = request.POST.get('mood', 'peaceful')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        is_secret = request.POST.get('is_secret', False) == 'on'
        tags = request.POST.get('tags', '')
        
        entry = DiaryEntry.objects.create(
            diary=diary,
            mood=mood,
            title=title,
            content=content,
            is_secret=is_secret,
            tags=tags
        )
        
        # AI 케어 응답 생성
        generate_ai_care_response(entry)
        
        return redirect('board:diary_detail', pk=entry.pk)
    
    context = {
        'diary': diary,
        'mood_choices': DiaryEntry.MOOD_CHOICES,
    }
    return render(request, 'board/diary_create.html', context)


@login_required
def diary_detail(request, pk):
    """일기 상세 페이지"""
    from .models import DiaryEntry
    
    entry = get_object_or_404(DiaryEntry, pk=pk, diary__user=request.user)
    
    context = {
        'entry': entry,
        'mood_label': dict(DiaryEntry.MOOD_CHOICES).get(entry.mood, ''),
    }
    return render(request, 'board/diary_detail.html', context)


@login_required
def diary_edit(request, pk):
    """일기 수정"""
    from .models import DiaryEntry
    
    entry = get_object_or_404(DiaryEntry, pk=pk, diary__user=request.user)
    
    if request.method == 'POST':
        entry.mood = request.POST.get('mood', entry.mood)
        entry.title = request.POST.get('title', entry.title)
        entry.content = request.POST.get('content', entry.content)
        entry.is_secret = request.POST.get('is_secret', False) == 'on'
        entry.tags = request.POST.get('tags', entry.tags)
        entry.save()
        
        # AI 응답 재생성 여부
        if request.POST.get('regenerate_ai'):
            generate_ai_care_response(entry)
        
        return redirect('board:diary_detail', pk=entry.pk)
    
    context = {
        'entry': entry,
        'mood_choices': DiaryEntry.MOOD_CHOICES,
    }
    return render(request, 'board/diary_edit.html', context)


@login_required
def diary_delete(request, pk):
    """일기 삭제"""
    from .models import DiaryEntry
    
    if request.method == 'POST':
        entry = get_object_or_404(DiaryEntry, pk=pk, diary__user=request.user)
        entry.delete()
        return redirect('board:diary_list')
    
    return redirect('board:diary_list')


def generate_ai_care_response(entry):
    """
    Gemini API를 사용해 공감과 조언을 담은 AI 응답 생성
    """
    try:
        from .models import DiaryEntry
        
        mood_label = dict(DiaryEntry.MOOD_CHOICES).get(entry.mood, '')
        
        prompt = f"""당신은 따뜻하고 경험 많은 육아 전문가이자 감정 상담가입니다.
한 명의 엄마가 일기에 적은 감정과 일상을 읽고, 깊은 공감과 실질적인 조언을 해주세요.

【엄마의 현재 기분】: {mood_label}

【엄마가 적은 내용】:
{entry.content}

【요청사항】:
1. 먼저 엄마의 감정을 깊게 이해하고 공감해주세요 (2-3문장)
2. 엄마가 겪는 상황이 얼마나 어려운지 인정해주세요
3. 구체적이고 실천 가능한 조언을 3가지 제시하세요
4. 마지막으로 힘내라는 따뜻한 격려 말씀을 해주세요

【톤】: 친한 선배 엄마처럼 따뜻하고 다정하게

답변은 한국어로, 3-4단락으로 구성해주세요."""

        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        
        if response.text:
            entry.ai_care_response = response.text
            entry.ai_response_generated = True
            entry.save()
            return True
    
    except Exception as e:
        print(f"AI 응답 생성 오류: {str(e)}")
        return False
    
    return False