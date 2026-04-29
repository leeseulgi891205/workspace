from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/kr-admin/', views.kr_admin, name='kr_admin'),
    
    # 게시판 ==========================================혜은
    path('board/', views.board_list, name='board_list'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),

    # 게시글 작성 ==========================================혜은
    path('create/', views.board_create, name='board_create'),
    
    # 챗봇 ==========================================혜은
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/api/', views.chatbot_api, name='chatbot_api'),
]
