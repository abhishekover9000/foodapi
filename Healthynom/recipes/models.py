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
    portions = models.PositiveSmallIntegerField()
    people = models.PositiveSmallIntegerField()
    prepTime = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name


class Inventory(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    costPerGram = models.FloatField()
    remainingQuantity = models.PositiveIntegerField()
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return self.ingredient.name

class RecipeIngredient(models.Model):
    CHOICES = (
        ('lbs', 'pounds'),
        ('oz', 'ounces'),
        ('floz', 'fluid ounces'),
        ('g', 'grams'),
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    ndbid = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    measurement = models.CharField(choices=CHOICES, max_length=4)

    def __str__(self):
        return self.ingredient.name
