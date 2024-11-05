from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Booking
from .models import CustomerLog
 

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
    phone = forms.CharField(max_length=15, required=False)
    subject = forms.ChoiceField(choices=[('general1', 'General Inquiry'), ('general2', 'General Inquiry'), ('general3', 'General Inquiry')])
    message = forms.CharField(widget=forms.Textarea)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'seat_number']

class CustomerLogForm(forms.ModelForm):
    class Meta:
        model = CustomerLog
        fields = ['email', 'phone', 'subject', 'message']