from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.http import HttpRequest
from django.contrib.auth.models import User

from reading_record.forms import RecordForm, AccountForm, AddAccountForm
from reading_record.models import Record

class AccountModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )

    def test_account_form(self):
        form_data = {
            'username': 'test_name',
            'email': 'test@test.com',
            'password': 'test_password'
        }
        account_form = AccountForm(form_data)
        self.assertTrue(account_form.is_valid())

    def test_add_account_form(self):
        form_data = {
            'last_name': 'last_name',
            'first_name': 'first_name'
        }
        account_form = AddAccountForm(form_data)
        self.assertTrue(account_form.is_valid())
