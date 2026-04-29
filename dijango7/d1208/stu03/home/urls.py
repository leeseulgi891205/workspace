
from django.urls import path
from . import views

app_name = ''
# url을 student 앱으로 연결
urlpatterns = [
    path('', views.index, name='index'),
]
