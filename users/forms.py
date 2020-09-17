from django import forms  # for creating form
from django.contrib.auth.models import User
from .models import Profile
# form of the default User model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # this is adding 'email' form from the User Model to display it in the form
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # to update the user in profile
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # to update the image in profile
    class Meta:
        model = Profile
        fields = ['image']
