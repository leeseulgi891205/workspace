from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('write/', views.write, name='write'),
]
