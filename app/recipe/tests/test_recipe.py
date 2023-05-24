from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate
from core.models import Recipe, User
from recipe.views import RecipeListAPI


class RecipeListAPITestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )

    def test_list_recipes(self):
        Recipe.objects.create(
            user=self.user,
            title='Recipe 1',
            description='Description 1',
            time_minutes=30,
            price=9.99,
            link='https://example.com'
        )

        Recipe.objects.create(
            user=self.user,
            title='Recipe 2',
            description='Description 2',
            time_minutes=45,
            price=12.99,
            link='https://example.com'
        )

        request = self.factory.get('/recipe-list/')
        force_authenticate(request, user=self.user)

        view = RecipeListAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_recipe(self):
        data = {
            'title': 'New Recipe',
            'time_minutes': 60,
            'price': 19.99,
            'link': 'https://example.com'
        }

        request = self.factory.post('/recipes/', data)
        force_authenticate(request, user=self.user)

        view = RecipeListAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.first().title, 'New Recipe')
