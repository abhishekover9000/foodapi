from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name',)

class InventorySerializer(serializers.ModelSerializer):
    supplied_by = SupplierSerializer(read_only=False)

    class Meta:
        model = Inventory
        fields = ('costPerGram',
                  'remainingQuantity',
                  'ndbid',
                  'supplied_by')



class IngredientSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'inventory')

    def create(self, validated_data):
        print(validated_data)
        inventory_data = validated_data.pop('inventory')
        pk = validated_data.pop('id')
        print(pk)
        ingredient, created = Ingredient.objects.update_or_create(id=pk, defaults={**validated_data})
        print('created ingredient : ' + str(created))
        print(Ingredient)
        spid = inventory_data.pop('supplied_by')
        spid = spid['name']
        supplier = get_object_or_404(Supplier, name=spid)
        print(ingredient.id)
        inventory, created = Inventory.objects.update_or_create(ingredient=ingredient,
                                                                defaults={**inventory_data, 'supplied_by':supplier})
        return ingredient


class RecipeIngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = RecipeIngredient
        fields = ('id', 'ingredient', 'recipe', 'quantityInGrams')

    def create(self, validated_data):
        print(validated_data)
        ingredientID = validated_data.pop('ingredient')
        ingredient = get_object_or_404(Ingredient, id=ingredientID)
        recipeId = validated_data.pop('recipe')
        recipe = get_object_or_404(Recipe, id=recipeId)
        if 'id' in validated_data:
            ingredientID = validated_data.pop('id')
            recipeingredient, created = RecipeIngredient.objects.update_or_create(id=ingredientID,
                                                                                  defaults={
                                                                                      'recipe':recipe,
                                                                                      'ingredient':ingredient,
                                                                                      **validated_data
                                                                                  })
            return recipeingredient
        else:
            recipeingredient = RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, **validated_data)
            return recipeingredient



class RecipeSerializer(serializers.ModelSerializer):
    recipeingredient_set = RecipeIngredientSerializer(many=True, required=False)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'steps', 'recipeingredient_set')