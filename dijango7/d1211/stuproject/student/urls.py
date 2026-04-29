
from django.urls import path, include
from . import views

app_name = 'student'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('view/<int:sno>/', views.view, name='view'),
    path('update/<int:sno>/', views.update, name='update'),
    path('delete/<int:sno>/', views.delete, name='delete'),
]
