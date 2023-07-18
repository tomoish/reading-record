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
    path('detail/<int:pk>/',views.RecordDetail.as_view(),name='detail'),
    path('guest-login/', views.GuestLoginView.as_view(), name = 'guest_login'),
    path('update/<int:pk>/',views.RecordUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.RecordDeleteView.as_view(),name='delete'),
]