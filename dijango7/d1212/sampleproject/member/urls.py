from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
