from django.shortcuts import render

from recipe_app.models import Author, Recipe
from recipe_app.forms import AuthorForm, RecipeForm

# Create your views here.


def simple_list(request):
    recipe_names = Recipe.objects.all()
    return render(request, "index.html", {"page_title": "RECIPE TITLES", "recipes": recipe_names})


def recipe_detail(request, recipe_id):
    chosen_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"page_title": "RECIPE DETAILS", "selected_recipe": chosen_recipe})


def author_detail(request, author_id):
    chosen_author = Author.objects.filter(id=author_id).first()
    allrecipes_byauthor = Recipe.objects.filter(author=chosen_author)
    return render(request, "author_detail.html", {"page_title": "AUTHOR DETAILS", "selected_author": chosen_author, "author_recipes": allrecipes_byauthor})


def author_form_view(request):
    author_form = AuthorForm()
    return render(request, "author_form.html", {"author_form": author_form})


def recipe_form_view(request):
    recipe_form = RecipeForm()
    return render(request, "recipe_form.html", {"recipe_form": recipe_form})
