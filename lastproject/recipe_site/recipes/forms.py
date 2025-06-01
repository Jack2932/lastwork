from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }