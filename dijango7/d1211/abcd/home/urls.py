from django.urls import path         # path 함수 불러오기
from . import views                  # 같은 폴더(home) 안의 views.py 불러오기

# app_name은 이 앱을 부를 때 쓰는 이름 (템플릿에서 {% url 'home:index' %} 이런 식으로 사용)
app_name = 'home'

# 이 앱 안에서만 쓰는 "작은 안내판"
urlpatterns = [
    # 주소: '/' (루트) → views.index 함수 실행 → index.html 보여주기
    path('', views.index, name='index'),
]