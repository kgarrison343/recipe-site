from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.order_by("-pub_date")

class MenuView(generic.ListView):
    template_name = 'recipes/menu.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.filter(on_the_menu__exact=1).order_by("-pub_date")
    
class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def toggle_on_the_menu(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    is_on = "on_the_menu" in request.POST
    
    recipe.on_the_menu = is_on
    recipe.save()

    return HttpResponseRedirect(reverse('recipes:detail', args=(recipe.id,)))
