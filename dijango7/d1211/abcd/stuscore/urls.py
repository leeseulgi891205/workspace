from django.urls import path
from . import views

app_name = 'stuscore'

urlpatterns = [
    # /stuscore/write/ 주소 → views.write 함수
    path('write/', views.write, name='write'),

    # /stuscore/list/ 주소 → views.list 함수
    path('list/', views.list, name='list'),
]