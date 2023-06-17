from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.AccountRegistration.as_view(), name='register'),
    # path('login/',views.Login,name='Login'),
    path('',views.Logout,name='Logout'),
    # path('home/',views.home,name='home'),
    path('show_records/',views.show_records,name='show_records'),
    path('record-create/', views.RecordCreateView.as_view(), name='record_create'),
    path('record-create/complete', views.RecordCreateCompleteView.as_view(), name='record_create_complete'),
    path('guest-login/', views.guest_login, name = 'guest_login'),
    path('login/',views.MyLoginView.as_view(),name='Login'),
    path('home/',views.HomeView.as_view(),name='home'),
]