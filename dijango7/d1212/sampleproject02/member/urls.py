from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
    path('write/', views.join, name='write'),
    path('list/', views.list, name='list'),
    path('excel/', views.excel_download, name='excel_download'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('detail/<str:id>/', views.detail, name='detail'),
    path('find_id/', views.find_id, name='find_id'),
    path('find_pw/', views.find_pw, name='find_pw'),
]
