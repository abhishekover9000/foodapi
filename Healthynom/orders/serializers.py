from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.Serializer):

    class Meta:
        model = Company
        fields = ('name',)

class MealSerializer(serializers.Serializer):
    class Meta:
        model = Meal
        fields = ('recipe', 'order')

class OrderSerializer(serializers.Serializer):
    meal_set = MealSerializer(read_only=False)

    class Meta:
        model= Order
        fields = ('boughtBy','transactionId','companyId','meal_set')


