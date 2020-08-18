from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm, SignupForm

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


@login_required
def add_author(request):
    if request.method == "POST":
        author_form = AddAuthorForm(request.POST)
        author_form.save()
        return HttpResponseRedirect(reverse("homepage"))
    author_form = AddAuthorForm()
    return render(request, "generic_form.html", {"page_title": "AUTHOR FORM", "author_form": author_form})


@login_required
def add_recipe(request):
    if request.method == "POST":
        recipe_form = AddRecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_data = recipe_form.cleaned_data
            new_recipe = Recipe.objects.create(
                title=recipe_data.get('title'),
                author=request.user.author,
                description=recipe_data.get('description'),
                time_required=recipe_data.get('time_required'),
                instructions=recipe_data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("recipe_detail", args=[new_recipe.id]))
    recipe_form = AddRecipeForm()
    return render(request, "recipe_form.html", {"page_title": "RECIPE FORM", "recipe_form": recipe_form})


# superusername: reggy / password: djangoway
def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_data = login_form.cleaned_data
            user = authenticate(request, username=login_data.get("username"), password=login_data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    login_form = LoginForm()
    return render(request, "login_form.html", {"page_title": "LOGIN FORM", "login_form": login_form})


# Username: regular1 / password: testing1
def signup_view(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_data = signup_form.cleaned_data
            new_user = User.objects.create_user(username=signup_data.get("username"), password=signup_data.get("password"))
            Author.objects.create(name=signup_data.get("username", user=new_user))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    signup_form = SignupForm()
    return render(request, "signup_form.html", {"page_title": "SIGNUP FORM", "signup_form": signup_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
