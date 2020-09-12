from django import forms  # for creating form
from django.contrib.auth.models import User

# form of the default User model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # this is creating email form from the User Model to display
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
