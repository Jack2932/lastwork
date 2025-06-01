from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="Ингредиенты, разделённые запятыми", blank=True)
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Время приготовления, мин.")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    categories = models.ManyToManyField(Category, through='RecipeCategory')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'category')