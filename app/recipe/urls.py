from django.urls import path

from .views import (
    RecipeListAPI,
    ReviewDetailAPI
)

urlpatterns = [
    path('recipes/', RecipeListAPI.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', ReviewDetailAPI.as_view(), name='recipe-detail')
]
