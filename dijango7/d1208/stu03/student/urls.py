
from django.urls import path, include
from . import views

app_name = 'student'

# url을 student 앱으로 연결
urlpatterns = [
    
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),
    path('view/', views.view, name='view'),
]
