from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class Nutrition(object):
    def __init__(self, ingredient, protein, calories, fat):
        self.ingredient = ingredient
        self.protein = protein
        self.calories = calories
        self.fat = fat


# computes nutrition using the nutrition api(needs work)
class NutritionView(APIView):
    conversion = {
        'lbs': 453.592,
        'oz':28.3495,
        'floz':28.3495
    }
    apiKey = "Ejxbm3FIhIFtATLIozMMBT4sR0QNKiWrwt7TUChQ"
    def get(self, request, pk, format=None):
        recipe = get_object_or_404(Recipe, id=pk)
        recipeIngredients = get_list_or_404(RecipeIngredient, recipe=recipe)

        return Response(serializer.data)


# computes price of recipe based on inventory
class ComputePrice(APIView):
    def get(self, request, pk, format=None):
        print(pk)
        recipe = get_object_or_404(Recipe, id=pk)
        recipeIngredients = get_list_or_404(RecipeIngredient, recipe=recipe)
        total = 0
        responsedict = {}
        for ingredient in recipeIngredients:
            print(ingredient)
            i = get_object_or_404(Ingredient, id=ingredient.ingredient.id)
            inventory = get_object_or_404(Inventory, ingredient=i)
            tempcost = ingredient.amount * i.inventory.price
            responsedict[ingredient.ingredient_name] = '$' + str(tempcost)
            total = total + tempcost
        responsedict['cost per meal'] = '$'+ str(total)
        return Response(responsedict)

# display, creation, editing of inventory instances
class InventoryView(APIView):
    def get(self, format=None):
        ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredient, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = IngredientSerializer(data=request.data)
        if data.is_valid():
            data = data.create(validated_data= data.data)
            serializer = IngredientSerializer(data)
            return Response(serializer.data)
        else:
            return Response(data.errors)

# destroys recipe instance
class DestroyRecipe(generics.RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# handles display, creation, and editing of recipes
class RecipeView(APIView):
    def get(self, format=None):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)
    def post(self, request):
        # ingredients = request.data.pop('ingredients')
        # print(request.data)
        data = RecipeSerializer(data=request.data)
        print(data.is_valid())
        if data.is_valid():
            model = data.create(validated_data = data.data)
            serializer = RecipeSerializer(model)
            return Response(serializer.data)
        else:
            return Response(data.errors)


# handles deletion and display of recipe ingredients
class RecipeIngredientView(APIView):
    def get(self, request, pk, kp, format=None):
        # print(pk,kp)
        # print('this')
        recipe = Recipe.objects.get(id=pk)
        queryset = RecipeIngredient.objects.filter(recipe=recipe)
        ingredient = get_object_or_404(RecipeIngredient, id=kp)
        serializer = RecipeIngredientSerializer(ingredient)
        return Response(serializer.data)
    def delete(self, request, pk, kp):
        recipe = Recipe.objects.get(id=pk)
        queryset = RecipeIngredient.objects.filter(recipe=recipe)
        ingredient = get_object_or_404(RecipeIngredient, id=kp)
        ingredient.delete()
        return Response(status=200)

class SearchView(APIView):
    def get(self, request):
        print(request.GET['q'])
        search = request.GET['q']
        list = Ingredient.objects.filter(name__contains=search)
        serializer = IngredientSerializer(list, many=True)
        return Response(serializer.data)

class DestroyIngredient(generics.RetrieveDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer



class SupplierView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)


class DestroySupplier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class DestroyRecipeIngredient(generics.RetrieveDestroyAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer