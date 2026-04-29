# board/urls.py
from django.urls import path
from . import views

# 앱 이름 설정 (나중에 html에서 링크 걸 때 헷갈리지 않게 해줍니다)
app_name = 'board'

urlpatterns = [
    # 주소가 빈 칸('')이면 views.main 함수를 실행해라
    # 이름은 'main'이라고 부르겠다
    path('', views.main, name='main'),
]