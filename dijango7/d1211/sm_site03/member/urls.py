from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('write/', views.write,name='write'),
    path('list/', views.list,name='list'),
    path('login/', views.login,name='login'),
    path('view/<str:id>/', views.view,name='view'),
    path('update/<str:id>/', views.update,name='update'),
    path('delete/<str:id>/', views.delete,name='delete'),
]
