from django.contrib import admin
from .models import Recipe, Category  # замените на ваши модели

admin.site.register(Recipe)
admin.site.register(Category)