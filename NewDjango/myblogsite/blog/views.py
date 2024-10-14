from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm  

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Home View
def home_view(request):
    return render(request, 'home.html')

# Flights View
def flights_view(request):
    flights_data = [
        {"flight_number": "AA123", "destination": "New York", "departure": "10:00 AM"},
        {"flight_number": "BA456", "destination": "London", "departure": "1:00 PM"},
        {"flight_number": "CA789", "destination": "Tokyo", "departure": "3:30 PM"},
    ]
    return render(request, 'flights.html', {'flights': flights_data})

# Info View
def info_view(request):
    return render(request, 'info.html')  # Create a corresponding info.html template

# Check-In View
def checkin_view(request):
    return render(request, 'checkin.html')  # Create a corresponding checkin.html template

# Booking View
def booking_view(request):
    return render(request, 'booking.html')  # Create a corresponding booking.html template

# Logout View
def logout_view(request):
    return render(request, 'logout.html')

