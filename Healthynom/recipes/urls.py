from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('compute1/', ComputePrice.as_view()),
    path('inventory/', InventoryView.as_view()),
    path('inventory/<int:pk>', DestroyIngredient.as_view()),
    path('recipes/<int:pk>', DestroyRecipe.as_view()),
    path('recipes/<int:pk>/ingredients/<int:kp>', RecipeIngredientView.as_view()),
    path('recipes/<int:pk>/cost', ComputePrice.as_view()),
    path('recipes/<int:pk>/nutrition', NutritionView.as_view()),
    path('inventory/search', SearchView.as_view()),
    path('recipes/', RecipeView.as_view()),
    path('supplier/', SupplierView.as_view()),
    path('supplier/<int:pk>', DestroySupplier.as_view())
]