# ═══════════════════════════════════════════════════════════════════════
# recipes/views.py
# 맘스로그 프로젝트 - 요리레시피 게시판 뷰
# ═══════════════════════════════════════════════════════════════════════
# 작성일: 2026-01-06
# ═══════════════════════════════════════════════════════════════════════

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Count
from .models import RecipePost, RecipeImage, RecipeComment
from .forms import RecipePostForm, RecipeCommentForm
from board.models import Notification


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 목록
# ═══════════════════════════════════════════════════════════════════════
def recipe_list(request):
    """
    요리레시피 목록 (카테고리 필터, 검색, 페이지네이션)
    """
    category = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').strip()
    # 커뮤니티형 필터 칩
    quick = request.GET.get('quick')  # '15'이면 15분 완성
    kid = request.GET.get('kid')      # '1'이면 아이도 먹는
    low = request.GET.get('low')      # '1'이면 재료 적은
    
    # 기본 쿼리
    posts = RecipePost.objects.all().select_related('author').prefetch_related('images')
    
    # 카테고리 필터 (생활형 명명 일부 매핑)
    if category and category != 'all':
        # 'main'은 현재 모델에 없으므로 한끼 해결 느낌을 'korean' 중심으로 표시
        if category == 'main':
            posts = posts.filter(category__in=['korean', 'western'])
        elif category == 'simple':
            posts = posts.filter(category='simple')
        else:
            posts = posts.filter(category=category)
    
    # 검색 필터
    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(content__icontains=search_query)

    # 필터 칩 적용 (모델 확장 전까지 카테고리로 대체)
    if quick == '15':
        posts = posts.filter(category__in=['simple'])
    if kid == '1':
        posts = posts.filter(category='baby')
    if low == '1':
        posts = posts.filter(category__in=['simple', 'diet'])
    
    posts = posts.order_by('-created_at')
    
    # 페이지네이션
    paginator = Paginator(posts, 12)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    context = {
        'page_obj': page_obj,
        'category': category,
        'search_query': search_query,
        'total_count': posts.count(),
        'quick': quick,
        'kid': kid,
        'low': low,
    }
    return render(request, 'recipes/recipe_list.html', context)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 상세
# ═══════════════════════════════════════════════════════════════════════
def recipe_detail(request, pk):
    """
    요리레시피 상세 (조회수 증가, 댓글 목록)
    """
    post = get_object_or_404(RecipePost, pk=pk)
    
    # 조회수 증가
    post.views += 1
    post.save(update_fields=['views'])
    
    # 댓글 목록
    comments = post.comments.all().select_related('author')
    
    # 이미지 목록
    images = post.images.all().order_by('order')

    # 댓글 폼 플레이스홀더 부여 (템플릿에서 직접 attrs 호출 방지)
    comment_form = RecipeCommentForm()
    comment_form.fields['content'].widget.attrs.update({
        'placeholder': '오늘 레시피 어땠는지, 식탁의 순간을 들려주세요 :)'
    })
    
    context = {
        'post': post,
        'comments': comments,
        'images': images,
        'comment_form': comment_form,
    }
    return render(request, 'recipes/recipe_detail.html', context)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 작성
# ═══════════════════════════════════════════════════════════════════════
@login_required(login_url='accounts:login')
def recipe_create(request):
    """
    요리레시피 작성 (이미지 최대 10개 업로드)
    """
    if request.method == 'POST':
        form = RecipePostForm(request.POST)
        images = request.FILES.getlist('images')
        
        if form.is_valid():
            # 이미지 개수 확인
            if len(images) > 10:
                form.add_error(None, '이미지는 최대 10개까지 업로드할 수 있습니다.')
            else:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                
                # 이미지 저장
                for idx, image_file in enumerate(images):
                    RecipeImage.objects.create(
                        post=post,
                        image=image_file,
                        order=idx + 1
                    )
                
                return redirect('recipes:recipe_detail', pk=post.pk)
    else:
        form = RecipePostForm()
    
    context = {
        'form': form,
        'mode': 'create',
    }
    return render(request, 'recipes/recipe_form.html', context)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 수정
# ═══════════════════════════════════════════════════════════════════════
@login_required(login_url='accounts:login')
def recipe_update(request, pk):
    """
    요리레시피 수정
    """
    post = get_object_or_404(RecipePost, pk=pk)
    
    # 작성자 확인
    if post.author != request.user:
        return redirect('recipes:recipe_detail', pk=pk)
    
    if request.method == 'POST':
        form = RecipePostForm(request.POST, instance=post)
        images = request.FILES.getlist('images')
        
        if form.is_valid():
            # 기존 이미지 개수
            existing_images_count = post.images.count()
            
            # 삭제할 이미지 ID 목록
            delete_image_ids = request.POST.getlist('delete_images')
            if delete_image_ids:
                post.images.filter(id__in=delete_image_ids).delete()
                existing_images_count -= len(delete_image_ids)
            
            # 새 이미지 개수 확인
            if existing_images_count + len(images) > 10:
                form.add_error(None, f'이미지는 최대 10개까지 업로드할 수 있습니다. (현재: {existing_images_count}개)')
            else:
                post = form.save()
                
                # 새 이미지 저장
                current_max_order = post.images.aggregate(max_order=Count('order'))['max_order'] or 0
                for idx, image_file in enumerate(images):
                    RecipeImage.objects.create(
                        post=post,
                        image=image_file,
                        order=current_max_order + idx + 1
                    )
                
                return redirect('recipes:recipe_detail', pk=post.pk)
    else:
        form = RecipePostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
        'mode': 'update',
        'images': post.images.all().order_by('order'),
    }
    return render(request, 'recipes/recipe_form.html', context)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 삭제
# ═══════════════════════════════════════════════════════════════════════
@login_required(login_url='accounts:login')
def recipe_delete(request, pk):
    """
    요리레시피 삭제
    """
    post = get_object_or_404(RecipePost, pk=pk)
    
    # 작성자 확인
    if post.author != request.user:
        return redirect('recipes:recipe_detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        return redirect('recipes:recipe_list')
    
    return redirect('recipes:recipe_detail', pk=pk)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 댓글 작성
# ═══════════════════════════════════════════════════════════════════════
@login_required(login_url='accounts:login')
@require_http_methods(["POST"])
def comment_create(request, pk):
    """
    요리레시피 댓글 작성
    """
    post = get_object_or_404(RecipePost, pk=pk)
    form = RecipeCommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        
        # 알림 생성 (작성자에게)
        if post.author != request.user:
            try:
                notification_message = f"{request.user.userprofile.nickname}님이 '{post.title}' 레시피에 댓글을 남겼습니다."
            except:
                notification_message = f"{request.user.username}님이 '{post.title}' 레시피에 댓글을 남겼습니다."
            
            Notification.objects.create(
                user=post.author,
                recipe_post=post,
                message=notification_message
            )
    
    return redirect('recipes:recipe_detail', pk=pk)


# ═══════════════════════════════════════════════════════════════════════
# 요리레시피 댓글 삭제
# ═══════════════════════════════════════════════════════════════════════
@login_required(login_url='accounts:login')
@require_http_methods(["POST"])
def comment_delete(request, pk, comment_id):
    """
    요리레시피 댓글 삭제
    """
    comment = get_object_or_404(RecipeComment, pk=comment_id)
    
    # 작성자 확인
    if comment.author == request.user:
        comment.delete()
    
    return redirect('recipes:recipe_detail', pk=pk)
