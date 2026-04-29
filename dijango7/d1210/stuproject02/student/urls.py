from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('<int:sno>/view/', views.view, name='view'),
]
