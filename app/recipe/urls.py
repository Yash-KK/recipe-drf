from django.urls import path

from .views import (
    RecipeListAPI,
    ReviewDetailAPI,
    RecipeImageUploadView,

    TagListAPI,
    TagDetailAPI,

    IngredientListAPI,
    IngredientDetailAPI,

)

urlpatterns = [
    path('recipes/', RecipeListAPI.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', ReviewDetailAPI.as_view(), name='recipe-detail'),
    path(
        'recipes/<int:pk>/upload-image/',
        RecipeImageUploadView.as_view(),
        name='upload-image'
    ),
    path('tags/', TagListAPI.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailAPI.as_view(), name='tag-detail'),

    path('ingredients/', IngredientListAPI.as_view(), name='ingredient-list'),
    path(
        'ingredients/<int:pk>/',
        IngredientDetailAPI.as_view(),
        name='ingredient-detail'
    )
]
