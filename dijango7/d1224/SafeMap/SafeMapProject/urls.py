from django.contrib import admin
from django.urls import path
from main import views  # main 앱의 views를 가져옵니다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), # 주소 없이 들어오면 index 함수 실행
]