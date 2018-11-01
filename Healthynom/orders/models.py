from django.db import models
from django.contrib.auth.models import AbstractUser
from recipes.models import Recipe
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL)


class Order(models.Model):
    boughtBy = models.ForeignKey(User, on_delete=models.SET_NULL)
    transactionId = models.PositiveIntegerField(blank=True)
    companyId = models.ForeignKey(Company, on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now=True)


class Meal(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

