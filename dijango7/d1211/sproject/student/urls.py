
from django.urls import path
from . import views

app_name  = ''
urlpatterns = [
    
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),
    path('view/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('update_process/<int:id>/', views.update_process, name='update_process'),
]
