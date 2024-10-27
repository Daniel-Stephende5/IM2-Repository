from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('flights/', views.flights_view, name='flights'),
    path('info/', views.info_view, name='info'),
    path('checkin/', views.checkin_view, name='checkin'),
    path('booking/', views.booking_view, name='booking'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    # Ensure you actually have this function in views.py
    # path('insertsignup/', views.insertsignup, name='insertsignup'),  
]
