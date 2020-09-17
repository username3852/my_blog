from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# to avoid unauthorized users to access via urls directly
from django.contrib.auth.decorators import login_required

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
        form = UserRegisterForm(request.POST)  # for post method
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

   # here below,
    # request.POST --> data submitted in the form
    # instance=request.user --> the data i.e. username and email
    # when the user logins currently will be displayed in the form by default
    # request.FILES --> it is for the image file used in profile only


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
