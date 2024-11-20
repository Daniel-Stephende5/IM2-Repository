from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Base Post and Comment models for blog-like structure
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} on {self.post.title}'

# Login model for user accounts with email field
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

# Booking model to handle user bookings with relationships
class Booking(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    date = models.DateTimeField()
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Booking by {self.login.username} on {self.date}'

# Customer Support model for handling user inquiries
class CustomerSupport(models.Model):
    login = models.ForeignKey(Login, on_delete=models.SET_NULL, null=True)
    inquiry = models.TextField()
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Inquiry by {self.login.username if self.login else "Guest"}'

# Feedback model to store user feedback
class FeedbackForm(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.login.username}'

class CheckIn(models.Model):
    booking_reference = models.CharField(max_length=100)  # No primary key explicitly set
    checkin_time = models.DateField()

    def __str__(self):
        return f"CheckIn for {self.booking_reference}"

# User model for simplicity in some parts of the project
class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

# Flight model to represent flight details
class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_number

# Logout model to log when users log out
class Logout(models.Model):
    login = models.OneToOneField(Login, on_delete=models.CASCADE)
    logout_time = models.DateTimeField()

    def __str__(self):
        return f'Logout for {self.login.username} at {self.logout_time}'

# Signup model to keep track of user signup dates
class Signup(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Signup for {self.login.username} on {self.signup_date}'

# CustomerLog model to track customer inquiries
class CustomerLog(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('support', 'Support'),
        ('sales', 'Sales'),
        ('other', 'Other'),
    ]
 
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
 
    def __str__(self):
        return f"{self.email} - {self.subject}"
