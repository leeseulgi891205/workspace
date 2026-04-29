from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
    path('check_id/', views.check_id, name='check_id'),
    path('list/', views.member_list, name='list'),
    path('view/<str:id>/', views.member_view, name='view'),
]
