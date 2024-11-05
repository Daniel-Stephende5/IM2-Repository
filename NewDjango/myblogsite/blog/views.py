from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, ContactForm
from .forms import ContactForm
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
            # Log form errors to the console for debugging
            print(form.errors)
            messages.error(request, 'Please follow the required instructions for password.')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
 
 
# Login View
def login_view(request):
    # Clear messages from the previous request to avoid showing signup errors
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
                messages.error(request, "Invalid username or password.")  # Use messages to show errors
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
 
# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')  # Message after logout
    return redirect('login')  # Redirect to login after logout
 
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
        return render(request, 'infologin.html')  # Ensure you create info.html
    else:
        return render(request, 'info.html')

# Check-In View
def checkin_view(request):
    if request.user.is_authenticated:
        return render(request, 'checkinlogin.html')  # Ensure you create checkin.html
    else:
        return render(request, 'checkin.html')
# Booking View
def booking_view(request):
    if request.user.is_authenticated:
        return render(request, 'bookinglogin.html')  # Ensure you create booking.html
    else:
        return render(request, 'booking.html')
# Contact View
def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you could save it to the database or send an email)
            CustomerLog.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            success=True
            # For now, just render the form with a success message
            return render(request, 'customersupport.html', {'form': CustomerLogForm(), 'success': success})
     
    else:
        form = CustomerLogForm()
    return render(request, 'customersupport.html', {'form': form})



def customer_logs_view(request):
    logs = CustomerLog.objects.all()
    return render(request,'customerlogs.html',  {'logs': logs})