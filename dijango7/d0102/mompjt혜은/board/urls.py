# ═══════════════════════════════════════════════════════════════════════
# board/urls.py
# 맘스로그 프로젝트 - 게시판 URL 라우팅
# ═══════════════════════════════════════════════════════════════════════
# 작성일: 2025-12-29
# URL 패턴:
#   [공지사항] /board/notice/, /board/notice/<pk>/, /board/notice/write/
#   [자유게시판] /board/free/, /board/free/write/
#   [벼룩시장] /board/flea/, /board/flea/<pk>/, /board/flea/create/, edit, delete
#   [벼룩시장 찜] /board/flea/<pk>/like/ (25-12-29 추가)
#   [벼룩시장 댓글] /board/flea/<pk>/comment/, edit, delete (25-12-29 추가)
#   [벼룩시장 상태] /board/flea/<pk>/status/ (25-12-29 추가 - AJAX)
#   [알림] /board/notification/, /board/notification/<pk>/read/ (25-12-29 추가)
# ═══════════════════════════════════════════════════════════════════════

from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    # 1. 목록 보기
    path('notice/', views.notice_list, name='notice_list'),
    
    # 2. 글쓰기 (★ 이 줄이 없어서 에러가 난 것입니다! 꼭 추가해주세요)
    path('notice/write/', views.notice_write, name='notice_write'),
    
    # 3. 상세 보기
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    
    # ▼▼▼ [자유게시판] ▼▼▼
    path('free/', views.free_list, name='free_list'),  # 목록
    path('free/write/', views.free_create, name='free_create'),  # 글쓰기
    path('free/<int:pk>/', views.free_detail, name='free_detail'),   # 🔥상세보기  # (혜은 25-12-31 추가)
    path('free/<int:pk>/edit/', views.free_update, name='free_update'),  # 수정    # (혜은 25-12-31 추가)
    path('free/<int:pk>/delete/', views.free_delete, name='free_delete'),  # 삭제  # (혜은 25-12-31 추가)
    # path('free/<int:pk>/like/', views.free_like_toggle, name='free_like'),  # 좋아요  # (혜은 26-01-02 추가)
    
    # ▼▼▼ [벼룩시장] ▼▼▼
    path('flea/', views.flea_list, name='flea_list'),
    path('flea/write/', views.flea_create, name='flea_create'),
    path('flea/<int:pk>/', views.flea_detail, name='flea_detail'),
    path('flea/<int:pk>/comment/', views.flea_comment_create, name='flea_comment_create'),
    path('flea/<int:pk>/comment/<int:comment_id>/edit/', views.flea_comment_edit, name='flea_comment_edit'),
    path('flea/<int:pk>/comment/<int:comment_id>/delete/', views.flea_comment_delete, name='flea_comment_delete'),
    path('flea/<int:pk>/like/', views.flea_like_toggle, name='flea_like_toggle'),
    path('flea/<int:pk>/edit/', views.flea_edit, name='flea_edit'),
    path('flea/<int:pk>/delete/', views.flea_delete, name='flea_delete'),
    path('flea/<int:pk>/status/', views.flea_status_update, name='flea_status_update'),  # 25-12-29 추가
    
    # ▼▼▼ [알림] ▼▼▼
    path('notification/', views.notification_list, name='notification_list'),
    path('notification/<int:notification_id>/read/', views.notification_mark_as_read, name='notification_mark_as_read'),
    path('notification/mark-all-read/', views.notification_mark_all_read, name='notification_mark_all_read'),
    
    #25-12-30 민혁 추가-----------------------------------------------------------------------
    # ▼▼▼ [반려동물 게시판URL] ▼▼▼
    path('pet/', views.pet_list, name='pet_list'),
    path('pet/write/', views.pet_write, name='pet_write'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pet/<int:pk>/edit/', views.pet_edit, name='pet_edit'),  
    path('pet/<int:pk>/delete/', views.pet_delete, name='pet_delete'), 
    
    #25-12-31 민혁 추가-----------------------------------------------------------------------
    # ▼▼▼ [반려동물 게시판댓글URL] ▼▼▼
    path('pet/<int:pk>/comment/create/',views.pet_comment_create,name='pet_comment_create'),
    path('pet/<int:pk>/comment/<int:comment_id>/delete/',views.pet_comment_delete,name='pet_comment_delete'),
    path('pet/<int:pk>/comment/<int:comment_id>/edit/', views.pet_comment_edit, name='pet_comment_edit'),
]
