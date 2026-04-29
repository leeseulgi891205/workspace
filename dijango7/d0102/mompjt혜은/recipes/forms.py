from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeStep

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title']

class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ['order', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': '조리 단계 설명'}),
        }

RecipeStepFormSet = inlineformset_factory(
    Recipe, RecipeStep, form=RecipeStepForm,
    extra=1, can_delete=True
)
