from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from reading_record import views
from reading_record.models import Account, Record

class TestUrls(TestCase):

    def test_index_url(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, views.IndexView)

    def test_register_url(self):
        view = resolve('/register/')
        self.assertEqual(view.func.view_class, views.AccountRegistration)

    def test_record_create_url(self):
        view = resolve('/record-create/')
        self.assertEqual(view.func.view_class, views.RecordCreateView)

    def test_login_url(self):
        view = resolve('/login/')
        self.assertEqual(view.func.view_class, views.MyLoginView)

    def test_home_url(self):
        view = resolve('/home/')
        self.assertEqual(view.func.view_class, views.HomeView)

    def test_guest_login_url(self):
        view = resolve('/guest-login/')
        self.assertEqual(view.func.view_class, views.GuestLoginView)