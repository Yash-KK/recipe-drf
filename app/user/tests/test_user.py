from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import User
from rest_framework.authtoken.models import Token


class UserAPITestCase(APITestCase):
    def test_register_user(self):
        url = reverse('user-create')
        data = {
            'name': 'testUser',
            'email': 'testUser@example.com',
            'password': 'checkpassword',
            'confirm_password': 'checkpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_user(self):
        user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        url = reverse('me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ObtainTokenAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword')

    def test_obtain_token(self):
        url = reverse('access-token')
        data = {
            'email': 'testUser@example.com',
            'password': 'checkpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
