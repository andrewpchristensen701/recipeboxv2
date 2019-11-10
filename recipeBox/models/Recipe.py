from django.db import models
from .Author import Author


class Recipe(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField()
    time_required = models.CharField()
    instructions = models.TextField()
