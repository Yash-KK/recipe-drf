from django.test import TestCase
from core.models import Recipe, User


class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )
        self.recipe = Recipe.objects.create(
            user=self.user,
            title='Test Recipe',
            description='Test description',
            time_minutes=30,
            price=9.99,
            link='https://example.com'
        )

    def test_recipe_user(self):
        self.assertEqual(self.recipe.user, self.user)

    def test_recipe_fields(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.description, 'Test description')
        self.assertEqual(self.recipe.time_minutes, 30)
        self.assertEqual(self.recipe.price, 9.99)
        self.assertEqual(self.recipe.link, 'https://example.com')
