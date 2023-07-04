import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from reading_record import views
from reading_record.models import Account, Record
from django.contrib.auth.models import User
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )

        self.guest_user = get_user_model().objects.create(
            username='guest',
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

    def test_login_get(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_redirect_get(self):
        self.client.force_login(self.user, backend='django.contrib.auth.backends.ModelBackend')
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 301)

    def test_login(self):        
        self.client.force_login(self.user, backend='django.contrib.auth.backends.ModelBackend')
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.user.username)

    def test_show_records(self):        
        self.client.force_login(self.user, backend='django.contrib.auth.backends.ModelBackend')
        response = self.client.get('/show_records/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.user.username)

    def test_guest_login(self):
        self.client.force_login(self.guest_user, backend='django.contrib.auth.backends.ModelBackend')
        response = self.client.get('/guest-login/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_reading_records(self):
        self.client.force_login(self.user, backend='django.contrib.auth.backends.ModelBackend')
        data = {
            'user': self.user,
            'book_title': 'test_book_title',
            'isbn': '9784150413330',
            'date': timezone.now,
            'first_page': 12,
            'final_page': 210,
            'impression': 'test_impression',
        }
        response = self.client.post('/record-create/', data=data)
        self.assertEqual(response.status_code, 200)