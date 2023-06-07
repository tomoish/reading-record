from django.contrib import admin

from .models import Account, Record

admin.site.register(Account)
admin.site.register(Record)