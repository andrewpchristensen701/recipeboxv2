from django.db import models
from django.contrib.auth.models import User


# noinspection PyMissingOrEmptyDocstring
class Author(models.Model):
    name = models.CharField(max_length=90)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    favorites = models.ManyToManyField('Recipe',
                                    symmetrical=False,
                                    blank=True,
                                    related_name='favorites')

    def __str__(self):
        return self.name


# noinspection PyMissingOrEmptyDocstring
class Recipe(models.Model):
    title = models.CharField(max_length=90)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=90)
    time_required = models.CharField(max_length=90)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.author.name}'
