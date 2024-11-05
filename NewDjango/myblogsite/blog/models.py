from django.db import models
 
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
    
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Booking(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)  # One Mandatory to Many Optional (Login to Bookings)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)  # Many Mandatory to One Mandatory (Bookings to Flights)
    date = models.DateTimeField()
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Booking by {self.login.username} on {self.date}'

class CustomerSupport(models.Model):
    login = models.ForeignKey(Login, on_delete=models.SET_NULL, null=True)  # Optional Many to One (CustomerSupport to Login)
    inquiry = models.TextField()
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Inquiry by {self.login.username if self.login else "Guest"}'

class FeedbackForm(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)  # One to Many (Login to FeedbackForm)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.login.username}'

class CheckIn(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)  # One Mandatory to Many Mandatory (Login to CheckIn)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'CheckIn for {self.login.username} - Status: {self.status}'

class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_number

class Logout(models.Model):
    login = models.OneToOneField(Login, on_delete=models.CASCADE)  # One-to-One (Login to Logout)
    logout_time = models.DateTimeField()

    def __str__(self):
        return f'Logout for {self.login.username} at {self.logout_time}'

class Signup(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)  # Many to One (Login to Signup)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Signup for {self.login.username} on {self.signup_date}'

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
    # Automatically sets the time when a log is created

    def __str__(self):
        return f"{self.email} - {self.subject}"