from django.db import models


# noinspection PyMissingOrEmptyDocstring
class Author(models.Model):
    name = models.CharField()
    bio = models.TextField()
