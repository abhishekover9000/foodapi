from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404


class NutrientSerializer(serializers.Serializer):
    ingredient = serializers.CharField(max_length=300)
    protein = serializers.FloatField()
    calories = serializers.FloatField()
    fat = serializers.FloatField()


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name',)

class InventorySerializer(serializers.ModelSerializer):
    supplied_by = SupplierSerializer(read_only=False)

    class Meta:
        model = Inventory
        fields = ('price', 'measurement', 'amount', 'supplied_by')



class IngredientSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(read_only=False)
    name=serializers.CharField(required=False)
    ndbid = serializers.IntegerField(required=False)
    class Meta:
        model = Ingredient
        fields = ('name', 'ndbid', 'inventory')

    def create(self, validated_data):
        print(validated_data)
        inventory_data = validated_data.pop('inventory')
        ndbid = validated_data.pop('ndbid')
        print(ndbid)
        ingredient, created = Ingredient.objects.update_or_create(ndbid=ndbid, defaults={**validated_data})
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
    ingredient = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'recipe', 'ingredient_name', 'ndbid', 'amount', 'measurement')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, required=False, source='recipeingredient_set')
    recipeName = serializers.CharField(source='name')
    recipeInstructions = serializers.CharField(source='steps')
    class Meta:
        model = Recipe
        fields = ('id', 'recipeName', 'recipeInstructions', 'ingredients', 'portions', 'people', 'prepTime')

    def create(self, validated_data):
        print(validated_data)
        r, created = Recipe.objects.update_or_create(name=validated_data['recipeName'],
                                                     defaults={
                                                         'name': validated_data['recipeName'],
                                                         'steps': validated_data['recipeInstructions'],
                                                         'portions':validated_data['portions'],
                                                         'people':validated_data['people'],
                                                         'prepTime':validated_data['prepTime']
                                                     })
        i = validated_data.pop('ingredients')
        print(i)
        for ingredient in i:
            print(ingredient)
            apiIngredient, created = Ingredient.objects.get_or_create(name = ingredient['ingredient_name'],defaults={
                'name':ingredient['ingredient_name'],
                'ndbid':ingredient['ndbid']
            })
            ii, created = RecipeIngredient.objects.update_or_create(recipe=r, ndbid=ingredient['ndbid'], defaults={
                'ingredient':apiIngredient,
                'recipe':r,
                'ingredient_name':ingredient['ingredient_name'],
                'ndbid':ingredient['ndbid'],
                'amount':ingredient['amount']/r.portions,
                'measurement':ingredient['measurement']
            })
        return r
