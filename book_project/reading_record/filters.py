import django_filters
from .models import Account, Record
from django.forms.widgets import Select

class  RecordModelFilter(django_filters.FilterSet):
    profile = django_filters.NumberFilter(method="get_profile_record")

    class Meta:
        model = Record
        fields = ('book_title','date','first_page','final_page','impression',)


