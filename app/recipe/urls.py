from django.urls import path

from .views import (
    RecipeListAPI,
    ReviewDetailAPI,

    TagListAPI,
    TagDetailAPI
)

urlpatterns = [
    path('recipes/', RecipeListAPI.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', ReviewDetailAPI.as_view(), name='recipe-detail'),

    path('tags/', TagListAPI.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailAPI.as_view(), name='tag-detail')
]
