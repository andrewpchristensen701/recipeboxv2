from .forms import CreateAuthorForm, CreateRecipeForm, LoginForm, CreatUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse
from recipeBox.models import Author, Recipe


def recipes(request, **kwargs):
    all_recipes = Recipe.objects.all()
    status = 'login' if not request.user.is_authenticated else 'logout'

    return render(request,
                  'index.html',
                  {'recipes': all_recipes,
                   'sign_in_button_label': status,
                   'sign_in_button_link': reverse(status)
                   })


def recipe(request, recipe_id):
    _recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe.html',
                  {
                      'recipe': _recipe
                  })


def author(request, author_name):
    _author = Author.objects.get(name=author_name)
    _recipes = Recipe.objects.filter(author=_author)
    return render(request, 'author.html',
                  {'author': _author,
                   'recipes': _recipes
                   })


@login_required()
def new_author(request, **kwargs):

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
    return render(request, "create_author.html", {'form': form})


@login_required()
def new_recipe(request):
    html = 'create_recipe.html'

    if request.method == 'POST':
        form = CreateRecipeForm(request.user, request.POST)

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


def signup_view(request):
    html = 'generic_form.html.j2'
    form = None

    if request.method == 'POST':
        form = CreatUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                name=data['name'],
                user=new_user
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))

    else:
        form = CreatUserForm()

    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    else:
        form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
