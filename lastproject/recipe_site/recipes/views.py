from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Category
from .forms import RecipeForm

import random

from django.shortcuts import render

def home(request):
    return render(request, 'recipes/index.html')

def index(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, 'recipes/index.html', {'recipes': random_recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.user != recipe.author:
        return redirect('recipe_detail', pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

def login_view(request):
    from django.contrib.auth.views import LoginView
    return LoginView.as_view(template_name='recipes/login.html')(request)

def logout_view(request):
    logout(request)
    return redirect('index')