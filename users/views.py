from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# this is to create flash message appear after registeration is complete
from django.contrib import messages

# types of messages
# 1. message.debug
# 2. message.info
# 3. message.warning
# 4. message.error
# 5 .message.success


def register(request):
    # means that it has the data of the form that has been submitted

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # changed the class from UserCreationForm to UserRegisterForm in order to bring email field on the signup form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # after this also update the base.html with flash message
            messages.success(
                request, f'{username}! Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()  # i.e. GET method or request
        return render(request, 'users/register.html', {'form': form})
