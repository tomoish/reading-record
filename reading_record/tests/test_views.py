import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from reading_record import views
from reading_record.models import Account, Record


class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )

        self.account = Account.objects.create(
            user = self.user,
            first_name = 'test_first_name',
            last_name = 'test_last_name'
        )

    def test_register_account(self):
        data = {
            'username': 'test_username',
            'email': 'test@gmail.com',
            'password': 'test_password',
            'first_name': 'first_name',
            'last_name': 'last_name',
        }
        response = self.client.post('/register/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):        
        self.client.force_login(self.user)
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.user.username)

    def test_show_records(self):        
        self.client.force_login(self.user)
        response = self.client.get('/show_records/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.user.username)
    