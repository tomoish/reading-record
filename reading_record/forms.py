from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

import requests

from .models import Account, Record

# create form class
class AccountForm(forms.ModelForm):
    # input password: 非表示
    password = forms.CharField(widget=forms.PasswordInput(),label="password")

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {'username':"username",'email':"mail"}
        help_texts = {
            'username': None,
        }

class AddAccountForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ('last_name','first_name',)
        labels = {'last_name':"last name",'first_name':"first name",}

class RecordForm(forms.ModelForm):
    class Meta():
        model = Record
        fields = ('book_title','isbn','date','first_page','final_page','impression',)
        labels = {'user':'user', 'book_title':'book_title','isbn':'isbn (optional)','date':'date','first_page':'first_page','final_page':'final_page','impression':'impression',}
        widgets = {
            'date': forms.NumberInput(attrs={
                "type": "date"
            })
        }

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        record_object = super().save(commit=False)

        # openBD api
        if record_object.isbn is not None:

            endpoint = "https://api.openbd.jp/v1/get"
            
            headers= {
                
            }
            params={
                "isbn":record_object.isbn
            }
            
            result = requests.get(endpoint, headers=headers, params=params)
            
            res = result.json()
            if res is not None and res[0] is not None:
                record_object.thumbnail_url = res[0]["summary"]["cover"]
                    
        if self.user:
            record_object.user = self.user
        if commit:
            record_object.save()
        return record_object
    
class LoginForm(AuthenticationForm):
    pass