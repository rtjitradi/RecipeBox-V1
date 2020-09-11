from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Author model:
Name (CharField)
Bio (TextField)

Recipe Model:
Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)

Note: Follow PEP8 naming conventions with your models and field names. An easy way to check is by looking at examples of code in Django's docs --> https://docs.djangoproject.com/en/3.0/topics/db/models/#quick-example (Links to an external site.)Links to an external site.
"""


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=90)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Favorites(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    favorited_by = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe}"
