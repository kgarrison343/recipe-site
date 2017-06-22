from django.contrib import admin
from .models import Recipe, Step, Ingredient

class StepInline(admin.TabularInline):
    model = Step
    extra = 2
    classes = ['collapse']

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2
    classes = ['collapse']

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['recipe_name', 'recipe_url', 'recipe_description', 'on_the_menu']}),]
    inlines = [IngredientInline, StepInline]
    
# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
