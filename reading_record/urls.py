from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.AccountRegistration.as_view(), name='register'),
    path('login/',views.MyLoginView.as_view(),name='Login'),
    path('',views.MyLogoutView.as_view(),name='Logout'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('show_records/',views.ShowRecordsView.as_view(),name='show_records'),
    path('record-create/', views.RecordCreateView.as_view(), name='record_create'),
    path('record-create/complete', views.RecordCreateCompleteView.as_view(), name='record_create_complete'),
    path('guest-login/', views.guest_login, name = 'guest_login'),
    
]