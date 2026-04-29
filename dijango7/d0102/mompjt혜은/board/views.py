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
from .models import Notice, FreePost, FleaItem, FleaComment, Notification
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
    # ✅ 선택된 카테고리
    selected_category = request.GET.get('category', 'all')

    # ✅ 카테고리 제목용
    CATEGORY_TITLES = {
        'all': '자유게시판',
        'mom': '육아수다',
        'husband': '남편뒷담화',
        'family': '시댁/친정',
        'preg': '임신출산',
    }

    # ✅ 기본 쿼리
    qs = FreePost.objects.all().order_by('-created_at')

    # ✅ 카테고리 필터
    if selected_category != 'all':
        qs = qs.filter(category=selected_category)

    total_count = qs.count()

    # ✅ 페이지네이션 (한 페이지 7개)
    per_page = 7
    paginator = Paginator(qs, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # ✅ 게시글 번호 계산 (전체 기준)
    start_number = total_count - per_page * (page_obj.number - 1)
    for idx, post in enumerate(page_obj.object_list):
        post.number = start_number - idx

    # ✅ 페이지 번호 5개만 보이게 계산
    current = page_obj.number
    total_pages = paginator.num_pages

    start_page = max(current - 2, 1)
    end_page = min(start_page + 4, total_pages)

    if end_page - start_page < 4:
        start_page = max(end_page - 4, 1)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'total_count': total_count,
        'selected_category': selected_category,
        'category_title': CATEGORY_TITLES.get(selected_category, '자유게시판'),
        'start_page': start_page,
        'end_page': end_page,
        'total_pages': total_pages,
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
            post.save()                    # 진짜 저장
            return redirect('board:free_list') # 저장 후 목록으로 이동
    else:
        form = FreePostForm()
    
    return render(request, 'board/free_write.html', {'form': form})

# 3. 상세 보기                                    ==== 25-12-31 혜은 추가 ====
def free_detail(request, pk):
    post = get_object_or_404(FreePost, pk=pk)

    # ✅ 현재 카테고리 (GET 우선, 없으면 글의 카테고리)
    selected_category = request.GET.get('category', post.category or 'all')

    # 🔽 (이미 네가 구현한) 하단 목록용 queryset
    qs = FreePost.objects.all().order_by('-created_at')
    if selected_category != 'all':
        qs = qs.filter(category=selected_category)

    paginator = Paginator(qs, 7)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    total_count = qs.count()

    # 번호 계산
    start_number = total_count - (page_obj.number - 1) * 7
    for idx, item in enumerate(page_obj.object_list):
        item.number = start_number - idx

    context = {
        'post': post,
        'posts': page_obj,
        'page_obj': page_obj,
        'total_count': total_count,
        'selected_category': selected_category,  # ✅ 핵심
    }

    return render(request, 'board/free_detail.html', context)

# 4. 수정하기                                   ==== 25-01-02 혜은 추가 ====
@login_required(login_url='accounts:login')
def free_update(request, pk):
    post = get_object_or_404(FreePost, pk=pk)

    # 작성자 또는 관리자만 수정 가능
    if request.user != post.author and not request.user.is_staff:
        return redirect('board:free_detail', pk=pk)

    if request.method == 'POST':
        form = FreePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board:free_detail', pk=pk)
    else:
        form = FreePostForm(instance=post)

    return render(request, 'board/free_update.html', {
        'form': form,
        'post': post,
    })
@login_required
def free_delete(request, pk):
    post = get_object_or_404(FreePost, pk=pk)

    # 작성자만 삭제 가능
    if request.user != post.author:
        return redirect('board:free_list')

    if request.method == 'POST':
        post.delete()
        return redirect('board:free_list')

    return redirect('board:free_detail', pk=pk)

# # 6. 좋아요
# @login_required
# def free_like_toggle(request, pk):
#     post = get_object_or_404(FreePost, pk=pk)

#     # Like 모델/필드 구조에 따라 아래 로직은 바뀔 수 있어요.
#     # 예: ManyToManyField(users)로 좋아요를 관리하는 경우:
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)

#     return redirect('free_detail', pk=pk)  # 상세 페이지 url name에 맞게 수정

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
                    actor=request.user,  # 댓글 작성자
                    flea_item=item,
                    flea_comment=comment,
                    message=f"{comment.nickname}님이 댓글을 남겼습니다."
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
    return render(request, 'board/notification_list.html', {'notifications': notifications})

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
