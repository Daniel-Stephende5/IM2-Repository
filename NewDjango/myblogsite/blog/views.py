from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, ContactForm, CustomerLogForm
from django.contrib import messages
from .models import CustomerLog

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user
            login(request, user)  # Logs in the user immediately
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to home after signup
        else:
            print(form.errors)
            messages.error(request, 'Please follow the required instructions for password.')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    messages.get_messages(request).used = True
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Officially logged in')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Home View
def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'homelogin.html')
    else:
        return render(request, 'home.html')

# Flights View
def flights_view(request):
    flights_data = [
        {"flight_number": "AA123", "destination": "New York", "departure": "10:00 AM"},
        {"flight_number": "BA456", "destination": "London", "departure": "1:00 PM"},
        {"flight_number": "CA789", "destination": "Tokyo", "departure": "3:30 PM"},
    ]
    if request.user.is_authenticated:
        return render(request, 'flightslogin.html', {'flights': flights_data})
    else:
        return render(request, 'flights.html', {'flights': flights_data})

# Info View
def info_view(request):
    if request.user.is_authenticated:
        return render(request, 'infologin.html')
    else:
        return render(request, 'info.html')

# Check-In View
def checkin_view(request):
    if request.user.is_authenticated:
        return render(request, 'checkinlogin.html')
    else:
        return render(request, 'checkin.html')

# Booking View
def booking_view(request):
    if request.user.is_authenticated:
        return render(request, 'bookinglogin.html')
    else:
        return render(request, 'booking.html')

# Contact View
def contact_view(request):
    if request.method == 'POST':
        form = CustomerLogForm(request.POST)  # Using CustomerLogForm directly for consistency
        if form.is_valid():
            form.save()  # Saves directly using the form's model
            messages.success(request, "Your message was successfully sent!")
            return redirect('customerlogs')
        else:
            messages.error(request, "There was an error with your submission, please check again.")
    else:
        form = CustomerLogForm()
    return render(request, 'customersupportlogin.html', {'form': form})

# Customer Logs View
def customer_logs_view(request):
    logs = CustomerLog.objects.all()
    return render(request, 'customerlogs.html', {'logs': logs})
