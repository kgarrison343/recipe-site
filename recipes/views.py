from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

from .models import Recipe, Category

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

class CategoryView(generic.ListView):
    template_name = 'recipes/categories.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()

def recipes_for_category(request, category_id):
    recipe_list = Recipe.objects.filter(categories__exact=category_id)
    template = loader.get_template('recipes/index.html')
    context = {
        'recipe_list': recipe_list
    }
    return HttpResponse(template.render(context, request))
    
class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def toggle_on_the_menu(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    is_on = "on_the_menu" in request.POST
    
    recipe.on_the_menu = is_on
    recipe.save()

    return HttpResponseRedirect(reverse('recipes:detail', args=(recipe.id,)))
