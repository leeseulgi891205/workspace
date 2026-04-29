from django.urls import path, include
from . import views


app_name = ''
# 다른 app에 있는 url들을 포함시키기 위해 include 함수를 사용합니다.
urlpatterns = [
    path('', views.index, name='index'),
    
]
