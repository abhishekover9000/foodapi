from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.


class ComputePrice(APIView):
    def get(self, request, pk, format=None):
        print(pk)
        recipe = get_object_or_404(Recipe, id=pk)
        recipeIngredients = get_list_or_404(RecipeIngredient, recipe=recipe)
        total = 0
        for ingredient in recipeIngredients:
            print(ingredient)
            i = get_object_or_404(Ingredient, id=ingredient.ingredient.id)
            inventory = get_object_or_404(Inventory, ingredient=i)
            total = total + (ingredient.quantityInGrams*inventory.costPerGram)
        return Response({"cost per meal" : total})



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

class DestroyRecipe(generics.RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeView(APIView):
    def get(self, format=None):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)
    def post(self, request):
        if 'steps' in request.data:
            data = RecipeSerializer(data=request.data)
            if data.is_valid():
                recipeobject = data.create(validated_data = data.data)
                serializer = RecipeSerializer(recipeobject)
                return Response(serializer.data)
            else:
                return Response(data.errors)
        elif 'quantityInGrams' in request.data:
            data = RecipeIngredientSerializer(data=request.data)
            if data.is_valid():
                data = data.create(validated_data = data.data)
                serializer = RecipeIngredientSerializer(data)
                return Response(serializer.data)
            else:
                return Response(data.errors)
        else:
            return Response(404)

class DestroyIngredient(generics.RetrieveDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer



class SupplierView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class DestroySupplier(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer