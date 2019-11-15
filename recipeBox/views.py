from django.shortcuts import render
from recipeBox.models import Author, Recipe


def recipes(request, **kwargs):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': all_recipes})


def recipe(request, recipe_id):
    _recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe.html', {'recipe': _recipe})


def author(request, author_name):
    _author = Author.objects.get(name=author_name)
    _recipes = Recipe.objects.filter(author=_author)
    return render(request, 'author.html', {'author': _author, 'recipes': _recipes})