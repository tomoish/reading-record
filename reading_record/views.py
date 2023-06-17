from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
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

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(request, username=ID, password=Pass)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("アカウントが有効ではありません")
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'reading_record/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    return render(request, 'reading_record/index.html')

#ホーム
# @login_required
# def home(request):
#     params = {'UserID':request.user}
#     return render(request, 'reading_record/home.html', context=params)

def show_records(request):
    record_list = Record.objects.all()
    params = {'UserID':request.user, 'record_list': record_list}
    return render(request, 'reading_record/show_records.html',context=params)


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

class RecordCreateCompleteView(TemplateView):
    template_name = 'reading_record/record_create_complete.html'


def guest_login(request):
    user = User.objects.get(username='guest')
    login(request, user)
    return HttpResponseRedirect(reverse('home'))
