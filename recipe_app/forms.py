from django import forms
from recipe_app.models import Author, Recipe


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=80)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=150)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=90)
    instructions = forms.CharField(widget=forms.Textarea)
