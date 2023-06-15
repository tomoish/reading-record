from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from reading_record import views
from reading_record.models import Account, Record

class TestUrls(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )

        self.account = Account.objects.create(
            user = self.user,
            first_name = 'test_first_name',
            last_name = 'test_last_name'
        )

    def test_index_url(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, views.IndexView)

    def test_register_url(self):
        view = resolve('/register/')
        self.assertEqual(view.func.view_class, views.AccountRegistration)

    def test_record_create_url(self):
        self.client.force_login(self.user)
        view = resolve('/record-create/')
        self.assertEqual(view.func.view_class, views.RecordCreateView)

    