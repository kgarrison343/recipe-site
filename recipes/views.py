from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Recipe

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
