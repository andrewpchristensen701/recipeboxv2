from django import forms
from recipeBox.models import Author


class CreateAuthorForm(forms.Form):
    name = forms.CharField(max_length=90)
    bio = forms.CharField(widget=forms.Textarea)


class CreateRecipeForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=90)
    description = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
