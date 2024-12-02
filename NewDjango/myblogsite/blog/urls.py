from django.urls import path
from . import views
from .views import booking_create
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('flights/', views.flights_view, name='flights'),
    path('info/', views.info_view, name='info'),
    path('checkin/', views.checkin_view, name='checkin'),
    path('checkin/', views.checkin_form, name='checkin'), 
    path('booking/', views.booking_create, name='booking'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('customerlogs/', views.customer_logs_view, name ='customerlogs'),
    path('heyadmin/', views.heyadmin_view, name ='heyadmin'),
]
