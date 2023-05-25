from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate
from recipe.views import TagListAPI, TagDetailAPI
from core.models import Tag, User


class TagAPITestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email='testUser@example.com',
            password='checkpassword'
        )

        self.tag1 = Tag.objects.create(user=self.user, name='Tag 1')
        self.tag2 = Tag.objects.create(user=self.user, name='Tag 2')

    def test_list_tags(self):
        request = self.factory.get('/tags/')
        force_authenticate(request, user=self.user)
        view = TagListAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_tag(self):
        request = self.factory.get(f'/tags/{self.tag1.pk}/')
        force_authenticate(request, user=self.user)
        view = TagDetailAPI.as_view()
        response = view(request, pk=self.tag1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tag 1')

    def test_update_tag(self):
        data = {'name': 'Updated Tag'}
        request = self.factory.put(
            f'/tags/{self.tag1.pk}/',
            data,
            content_type='application/json'
        )
        force_authenticate(request, user=self.user)
        view = TagDetailAPI.as_view()
        response = view(request, pk=self.tag1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Tag')

    def test_delete_tag(self):
        request = self.factory.delete(f'/tags/{self.tag1.pk}/')
        force_authenticate(request, user=self.user)
        view = TagDetailAPI.as_view()
        response = view(request, pk=self.tag1.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tag.objects.filter(pk=self.tag1.pk).exists())
