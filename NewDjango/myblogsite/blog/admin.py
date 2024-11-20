from django.contrib import admin
from .models import Post, Comment, Login, Booking, CustomerSupport, Flight, Logout, Signup, FeedbackForm


# Customizing the Post admin display
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

# Customizing the Comment admin display
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author', 'text')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

# Registering the Login model
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

# Registering the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('login', 'flight', 'date', 'seat_number')
    search_fields = ('login__username', 'flight__flight_number')
    list_filter = ('date',)
    date_hierarchy = 'date'

# Registering the CustomerSupport model
@admin.register(CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ('login', 'inquiry', 'response')
    search_fields = ('login__username', 'inquiry')
    list_filter = ('login',)



# Registering the Flight model
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'destination')
    search_fields = ('flight_number', 'destination')

# Registering the Logout model
@admin.register(Logout)
class LogoutAdmin(admin.ModelAdmin):
    list_display = ('login', 'logout_time')
    search_fields = ('login__username',)
    date_hierarchy = 'logout_time'

# Registering the Signup model
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('login', 'signup_date')
    search_fields = ('login__username',)
    date_hierarchy = 'signup_date'

# Registering the FeedbackForm model
@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ('login', 'created_at')
    search_fields = ('login__username', 'feedback')
    date_hierarchy = 'created_at'

# Registering additional models
# Feel free to add further customization or unregister any default admin behaviors if needed.
