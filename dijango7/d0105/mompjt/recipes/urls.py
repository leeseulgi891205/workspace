from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('',views.recipes_main,name='recipes_main'),
    path('stage-1/',views.recipes_stage_1,name='recipes_stage_1'),
    path('stage-2/',views.recipes_stage_2,name='recipes_stage_2'),
    path('stage-3/',views.recipes_stage_3,name='recipes_stage_3'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    # ★ 26-01-02 추가: AI 이유식 레시피 생성 API
    path('api/generate-recipe/', views.generate_recipe, name='generate_recipe'),
]
