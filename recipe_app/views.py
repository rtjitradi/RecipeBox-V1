from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm

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


def add_author(request):
    if request.method == "POST":
        author_form = AddAuthorForm(request.POST)
        if author_form.is_valid():
            author_data = author_form.cleaned_data
            Author.objects.create(
                name=author_data.get('name'),
                bio=author_data.get('bio'),
            )
    author_form = AddAuthorForm()
    return render(request, "author_form.html", {"author_form": author_form})


def add_recipe(request):
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_data = recipe_form.cleaned_data
            Recipe.objects.create(
                title=recipe_data.get('title'),
                author=recipe_data.get('author'),
                description=recipe_data.get('description'),
                time_required=recipe_data.get('time_required'),
                instructions=recipe_data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))
    recipe_form = AddRecipeForm()
    return render(request, "recipe_form.html", {"recipe_form": recipe_form})
