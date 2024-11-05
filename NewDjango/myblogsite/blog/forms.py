from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerLog

# Signup Form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Only keep username and password fields

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Remove password matching check or any custom logic
        # This method can remain empty or just call super() if you don't need additional logic
        return cleaned_data

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Contact Form
class ContactForm(forms.Form):
    
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    subject = forms.ChoiceField(choices=[ ('general', 'General Inquiry'),
    ('support', 'Support'),
    ('sales', 'Sales'),
    ('other', 'Other'),],required=True)
    message = forms.CharField(widget=forms.Textarea)

class CustomerLogForm(forms.ModelForm):
    class Meta:
        model = CustomerLog
        fields = ['email', 'phone', 'subject', 'message']