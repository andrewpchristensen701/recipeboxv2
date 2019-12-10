"""recipeBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipeBox import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipes, name="homepage"),
    path('author/<str:author_name>', views.author, name="author"),
    path('recipe/<int:recipe_id>', views.recipe),
    path('newAuthor/', views.new_author, name="create author"),
    path('newRecipe/', views.new_recipe, name="create recipe"),
    path('newUser/', views.signup_view, name='create user'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('editrecipe/<int:recipe_id>', views.edit_recipe, name="edit"),
    path('favorite/<int:id>/', views.favoriterecipe),
    path('unfavorite/<int:id>/', views.unfavoriterecipe),
]
