from django.db import models
from django.conf import settings

class Recipe(models.Model): # 글 제목 & 작성자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class RecipeStep(models.Model): # 단계별 설명 + 이미지, 순서
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()  # 단계 순서
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_steps/', blank=True, null=True)

    class Meta:
        ordering = ['order']
