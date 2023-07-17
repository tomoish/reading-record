from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AccountForm, AddAccountForm, RecordForm, LoginForm
from .models import Account, Record


class IndexView(TemplateView):
    template_name = 'reading_record/index.html'

class MyLoginView(LoginView):
    template_name = 'reading_record/login.html'
    form_class = LoginForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'reading_record/home.html'
    login_url = 'login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserID'] = self.request.user
        return context

class MyLogoutView(LogoutView):
    template_name = 'reading_record/index.html'

class ShowRecordsView(LoginRequiredMixin, ListView):
    template_name = 'reading_record/show_records.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_list = Record.objects.all().order_by('date').reverse()
        context['UserID'] = self.request.user
        context['record_list'] = record_list
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            record_list = Record.objects.filter(
                book_title__icontains=query).order_by('date').reverse()
        else:
            record_list = Record.objects.all().order_by('date').reverse()
        return record_list
        # return super().get_queryset()

class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        'AccountCreate':False,
        'account_form': AccountForm(),
        'add_account_form': AddAccountForm(),
        }

    def get(self,request):
        self.params['account_form'] = AccountForm()
        self.params['add_account_form'] = AddAccountForm()
        self.params['AccountCreate'] = False
        return render(request,'reading_record/register.html',context=self.params)

    def post(self,request):
        self.params['account_form'] = AccountForm(data=request.POST)
        self.params['add_account_form'] = AddAccountForm(data=request.POST)


        if self.params['account_form'].is_valid() and self.params['add_account_form'].is_valid():
            account = self.params['account_form'].save()
            account.set_password(account.password)
            account.save()

            add_account = self.params['add_account_form'].save(commit=False)
            add_account.user = account

            add_account.save()

            self.params['AccountCreate'] = True

        else:
            print(self.params['account_form'].errors)

        return render(request,'reading_record/register.html',context=self.params)
    
class RecordCreateView(CreateView):
    template_name = 'reading_record/record_create.html'
    form_class = RecordForm
    success_url = reverse_lazy('record_create_complete')

    def get_form_kwargs(self):
        kwgs = super().get_form_kwargs()
        kwgs['user'] = self.request.user
        return kwgs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserID'] = self.request.user
        return context
    
class RecordCreateCompleteView(TemplateView):
    template_name = 'reading_record/record_create_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserID'] = self.request.user
        return context

class GuestLoginView(View):
    def get(self,request):
        user = User.objects.get(username='guest')
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse('home'))

