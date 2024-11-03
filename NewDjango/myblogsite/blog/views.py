from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, ContactForm
from django.contrib import messages
 
 
 
# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user
            login(request, user)  # Logs in the user immediately
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            # Print the errors to the console for debugging
            print(form.errors)  # Add this line to see form errors in the terminal
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
    return render(request, 'homelogin.html')
 
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
    return render(request, 'info.html')  # Ensure you create info.html
 
# Check-In View
def checkin_view(request):
    return render(request, 'checkin.html')  # Ensure you create checkin.html
 
# Booking View
def booking_view(request):
    return render(request, 'booking.html')  # Ensure you create booking.html
 
# Contact View
def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you could save it to the database or send an email)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
 
            # For now, just render the form with a success message
            messages.success(request, 'Your message has been sent successfully!')  # Success message
            return render(request, 'customersupport.html', {'form': ContactForm(), 'success': True})
    return render(request, 'customersupport.html', {'form': form})