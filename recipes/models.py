from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    on_the_menu = models.BooleanField(default=False)
    recipe_url = models.URLField(blank=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.recipe_name

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_text = models.TextField()
    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
