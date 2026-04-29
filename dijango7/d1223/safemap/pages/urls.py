from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/kr-admin/', views.kr_admin, name='kr_admin'),
    # 슬기가 추가했고 25-12-23일에 추가
    path('korea-map/', views.korea_map, name='korea_map'),
    # 혜은 =========================================
    path('board/', views.board_list, name='board_list'),
    # 혜은 =========================================
]
