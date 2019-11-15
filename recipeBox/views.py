from django.shortcuts import render, HttpResponseRedirect, reverse
from recipeBox.models import Author, Recipe
from .forms import CreateAuthorForm, CreateRecipeForm
from django.contrib.auth.models import User


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


def new_author(request, **kwargs):
    html = "create_author.html"

    if request.method == "POST":
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create(
                username=data['name'],
            )
            Author.objects.create(
                name=data['name'],
                user=new_user,
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = CreateAuthorForm()
    return render(request, html, {'form': form})


def new_recipe(request):
    html = 'create_recipe.html'

    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                time_required=data['time_required'],
                description=data['description']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = CreateRecipeForm()
    return render(request, html, {'form': form})

