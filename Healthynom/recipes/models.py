from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    steps = models.TextField()
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantityInGrams = models.PositiveIntegerField()
    def __str__(self):
        return self.ingredient.name

class Inventory(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    costPerGram = models.FloatField()
    remainingQuantity = models.PositiveIntegerField()
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    ndbid = models.PositiveIntegerField()
    def __str__(self):
        return self.ingredient.name

