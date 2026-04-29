# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # 1. 메인 페이지 (대문)
    path('', views.main, name='main'),
    
    # 2. 공지사항 리스트 페이지 (새로 추가!)
    path('notice/', views.notice_list, name='notice_list'),
]