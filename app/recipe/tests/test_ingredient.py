from rest_framework.test import (
    APITestCase,
    APIRequestFactory,
    force_authenticate
)
from django.urls import reverse
from rest_framework import status
from core.models import Ingredient, User
from recipe.serializer import IngredientSerializer
from recipe.views import IngredientListAPI, IngredientDetailAPI


class IngredientListAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )
        self.ingredient1 = Ingredient.objects.create(
            user=self.user,
            name='Ingredient 1'
        )
        self.ingredient2 = Ingredient.objects.create(
            user=self.user,
            name='Ingredient 2'
        )

    def test_list_ingredients(self):
        request = self.factory.get('/ingredients/')
        force_authenticate(request, user=self.user)
        view = IngredientListAPI.as_view()
        response = view(request)

        ingredients = Ingredient.objects.filter(user=self.user)
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for ingredient in serializer.data:
            self.assertIn(ingredient, response.data)


class IngredientDetailAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )
        self.ingredient = Ingredient.objects.create(
            user=self.user,
            name='Ingredient 1'
        )
        self.url = reverse(
            'ingredient-detail',
            kwargs={'pk': self.ingredient.pk}
        )

    def test_retrieve_ingredient(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        view = IngredientDetailAPI.as_view()
        response = view(request, pk=self.ingredient.pk)
        serializer = IngredientSerializer(self.ingredient)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_ingredient(self):
        data = {'name': 'Updated Ingredient'}
        request = self.factory.put(self.url, data)
        force_authenticate(request, user=self.user)
        view = IngredientDetailAPI.as_view()
        response = view(request, pk=self.ingredient.pk)
        self.ingredient.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.ingredient.name, 'Updated Ingredient')

    def test_delete_ingredient(self):
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        view = IngredientDetailAPI.as_view()
        response = view(request, pk=self.ingredient.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Ingredient.objects.filter(
            pk=self.ingredient.pk).exists()
        )
