from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    book_title = models.CharField(max_length=100)
    date = models.DateField()
    first_page = models.IntegerField()
    final_page = models.IntegerField()
    impression = models.TextField(max_length=200)
    posted_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.book_title
    

