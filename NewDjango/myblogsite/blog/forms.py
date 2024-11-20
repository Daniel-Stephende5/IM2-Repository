from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Booking
from .models import CustomerLog
from .models import CheckIn
 
 


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    
    # Phone field that allows only numbers (and optional + or spaces)
    phone = forms.CharField(
        max_length=15, 
        required=False,
        widget=forms.NumberInput(attrs={'type': 'tel'})  # Set input type to 'tel' for phone number
    )
    
    subject = forms.ChoiceField(choices=[
        ('general1', 'General Inquiry'), 
        ('general2', 'General Inquiry'), 
        ('general3', 'General Inquiry')
    ])
    
    message = forms.CharField(widget=forms.Textarea)

    # Custom validation to allow only digits (optional validation)
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        
        # Remove spaces or special characters if needed
        phone = phone.replace(" ", "").replace("-", "").replace("+", "")
        
        if not phone.isdigit():  # Check if all characters are digits
            raise forms.ValidationError("Phone number must contain only digits.")
        
        return phone
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'seat_number']

class CustomerLogForm(forms.ModelForm):
    class Meta:
        model = CustomerLog
        fields = ['email', 'phone', 'subject', 'message']
        
class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['booking_reference', 'checkin_time']
        widgets = {
            'checkin_time': forms.DateInput(attrs={'type': 'date'}),
        }