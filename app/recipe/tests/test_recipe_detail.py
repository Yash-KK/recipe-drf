from decimal import Decimal
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from recipe.views import ReviewDetailAPI
from core.models import Recipe, User


class ReviewDetailAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )
        self.recipe = Recipe.objects.create(
            user=self.user,
            title='Test Recipe',
            time_minutes=10,
            price=9.99,
            link='http://example.com',
            description='Test Description'
        )

    def test_get_recipe_detail(self):
        url = f'/recipes/{self.recipe.pk}/'
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)

        view = ReviewDetailAPI.as_view()
        response = view(request, pk=self.recipe.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.recipe.title)

    def test_update_recipe(self):
        url = f'/recipes/{self.recipe.pk}/'
        data = {
            'user': self.user,
            'title': 'Updated Recipe',
            'time_minutes': 15,
            'price': '19.99',
            'link': 'http://example.com/updated',
        }
        request = self.factory.put(url, data)
        force_authenticate(request, user=self.user)

        view = ReviewDetailAPI.as_view()
        response = view(request, pk=self.recipe.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

        updated_recipe = Recipe.objects.get(pk=self.recipe.pk)
        self.assertEqual(updated_recipe.title, data['title'])
        self.assertEqual(updated_recipe.time_minutes, data['time_minutes'])
        self.assertEqual(updated_recipe.price, Decimal(data['price']))
        self.assertEqual(updated_recipe.link, data['link'])

    def test_delete_recipe(self):
        url = f'/recipes/{self.recipe.pk}/'
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)

        view = ReviewDetailAPI.as_view()
        response = view(request, pk=self.recipe.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipe.objects.filter(pk=self.recipe.pk).exists())
