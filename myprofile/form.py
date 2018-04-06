from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    # email=forms.EmailField(max_length=100)
    class Meta:
        models = User
        fields = ('username', 'password')


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirm your password',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Enter the same password as before, for verification.',
    )

    class Meta:
        model = User
        fields = ('username', 'email')
