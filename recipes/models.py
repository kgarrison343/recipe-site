from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.recipe_name

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_num = models.IntegerField(default=1)
    step_text = models.CharField(max_length=500)
    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
