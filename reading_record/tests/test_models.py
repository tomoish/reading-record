import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from reading_record.models import Account, Record

class AccountModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )

    def test_is_empty(self):
        saved_accounts = Account.objects.all()
        self.assertEqual(saved_accounts.count(), 0)

    def test_is_count_one(self):
        account = Account(user=self.user, last_name='last_name', first_name='first_name')
        account.save()
        saved_accounts = Account.objects.all()
        self.assertEqual(saved_accounts.count(), 1)


    def test_saving_and_retrieving_post(self):
        account = Account()
        username='test_user'
        last_name = 'test_last_name_to_retrieve'
        first_name = 'test_first_name_to_retrieve'
        account.user = self.user
        account.last_name = last_name
        account.first_name = first_name
        account.save()

        saved_accounts = Account.objects.all()
        actual_account = saved_accounts[0]

        self.assertEqual(actual_account.user.username, username)
        self.assertEqual(actual_account.last_name, last_name)
        self.assertEqual(actual_account.first_name, first_name)


class RecordModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
        )
        self.dt_now = datetime.datetime.now()

    def test_is_empty(self):
        saved_records = Record.objects.all()
        self.assertEqual(saved_records.count(), 0)

    def test_is_count_one(self):
        record = Record(user=self.user, date=self.dt_now.date(), book_title='title', first_page=0, final_page=100, impression='test_impression')
        record.save()
        saved_records = Record.objects.all()
        self.assertEqual(saved_records.count(), 1)


    def test_saving_and_retrieving_post(self):
        record = Record()
        username='test_user'
        date_test = datetime.datetime(2023, 4, 1).date()
        book_title = 'test_title_to_retrieve'
        isbn = '9784150413330'
        thumbnail_url = 'https://cover.openbd.jp/9784150413330.jpg'
        first_page = 100
        final_page = 200
        impression = 'test_impression_to_retrieve'
        record.user = self.user
        record.date = date_test
        record.book_title = book_title
        record.isbn = isbn
        record.thumbnail_url = thumbnail_url
        record.first_page = first_page
        record.final_page = final_page
        record.impression = impression
        record.save()

        saved_records = Record.objects.all()
        actual_record = saved_records[0]

        self.assertEqual(actual_record.user.username, username)
        self.assertEqual(actual_record.date, date_test)
        self.assertEqual(actual_record.book_title, book_title)
        self.assertEqual(actual_record.isbn, isbn)
        self.assertEqual(actual_record.thumbnail_url, thumbnail_url)
        self.assertEqual(actual_record.first_page, first_page)
        self.assertEqual(actual_record.final_page, final_page)
        self.assertEqual(actual_record.impression, impression)
