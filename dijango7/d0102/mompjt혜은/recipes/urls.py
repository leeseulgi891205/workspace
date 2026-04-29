from django.urls import path
from . import views

app_name = 'recipes'  # <--- 이 줄이 꼭 있어야 합니다!

urlpatterns = [
    path('',views.recipes_main,name='recipes_main'),
    path('stage-1/',views.recipes_stage_1,name='recipes_stage_1'),
    path('stage-2/',views.recipes_stage_2,name='recipes_stage_2'),
    path('stage-3/',views.recipes_stage_3,name='recipes_stage_3'),
    path('create/', views.recipe_create, name='recipe_create'),    # 글쓰기 페이지
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),  # 상세 페이지
]
