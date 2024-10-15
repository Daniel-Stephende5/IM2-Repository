from django.contrib import admin  # Import the admin module
from django.urls import path
from .views import signup_view, login_view, home_view, flights_view, info_view, checkin_view, booking_view,logout_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('signup/', signup_view, name='signup'),  # Signup URL
    path('login/', login_view, name='login'),  # Login URL
    path('', home_view, name='home'),  # Home URL
    path('flights/', flights_view, name='flights'),  # Flights URL
    path('info/', info_view, name='info'),  # Info URL
    path('checkin/', checkin_view, name='checkin'),  # Check-in URL
    path('booking/', booking_view, name='booking'),  # Booking URL
    path('logout/', logout_view, name='logout'),  # Booking URL
    path('contact/', contact_view, name='contact'),
    
]
