import json

from django.contrib.auth.models import User
from django.test import TestCase
from oauth2_provider.models import Application
from register_bot.models import *
from rest_framework import status
from rest_framework.test import APIClient


class RegisterUserTestCase(TestCase):

    def setUp(self):
        user = User(username='api_test')
        user.set_password('cyPNjhx9aNADjF4Z')
        user.save()
        application = Application.objects.create(user=user, authorization_grant_type='password', client_type='confidential', name='api_test')

        client = APIClient()

        data = {'grant_type': application.authorization_grant_type, 'username': user.username, 'password': 'cyPNjhx9aNADjF4Z', 'client_id': application.client_id, 'client_secret':  application.client_secret}

        response = client.post('/api/oauth2/access_token/', data)

        result = json.loads(response.content)
        self.access_token = result['access_token']
        self.user = user


    def test_register_user(self):
        client = APIClient()
        client.force_authenticate(user=self.user, token=self.access_token)

        correct_result = {}
        bad_result = {"errors": {"email": ["Enter a valid email address."]}}

        data = {'name': 'Foo', 'email': 'test@gmail.com', 'phone': '987654321', 'origin': 'bot'}

        response = client.post('/api/register_user/', data, format='json')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, correct_result)

        bad_data = {'name': 'Foo', 'email': 'bad email', 'phone': '987654321', 'origin': 'bot'}

        bad_response = client.post('/api/register_user/', bad_data, format='json')
        result = json.loads(bad_response.content)
        self.assertEqual(bad_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result, bad_result)
