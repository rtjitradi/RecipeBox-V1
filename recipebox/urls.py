"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from recipe_app import views

urlpatterns = [
    path('', views.simple_list, name="homepage"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('author/<int:author_id>/', views.author_detail, name="author_detail"),
    path('newauthor/', views.add_author, name="newauthor"),
    path('newrecipe/', views.add_recipe, name="newrecipe"),
    path('editrecipe/<int:recipe_id>/', views.edit_recipe, name="editrecipe"),
    path('addfavorite/<int:recipe_id>/', views.add_favorite, name="addfavorite"),
    path('removefavorite/<int:recipe_id>/',
         views.remove_favorite, name="removefavorite"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('signup/', views.signup_view, name="signup_view"),
    path('admin/', admin.site.urls),
]
