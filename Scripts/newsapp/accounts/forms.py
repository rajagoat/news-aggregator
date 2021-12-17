from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reader, Profile, Author

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'address']
        widgets = {'birth_date': forms.DateInput(attrs={'class': 'datepicker', 'id': 'birth_date'})}

class AuthorRegisterForm(forms.ModelForm):
    awards = forms.CharField(max_length=150)
    preferred_genre = forms.CharField(max_length=150)

    class Meta:
        model = Author
        fields = ['awards', 'preferred_genre']
