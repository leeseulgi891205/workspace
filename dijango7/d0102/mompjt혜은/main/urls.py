from django.urls import path
from . import views
from board import views as board_views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('growth/', views.growth_chart, name='growth_chart'),
    # path('free/<int:pk>/like/', board_views.free_like_toggle, name='free_like'),  # (혜은 26-01-02 추가)
]
