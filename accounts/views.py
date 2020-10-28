from django.shortcuts import render, redirect
from .forms import LoginForm, ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('main:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You've logged out successfully")
    return redirect('accounts:login')



@login_required(login_url='accounts:login')
def dashboard(request):
    try:
        user_profile = request.user.profile 
    except Profile.DoesNotExist:
        user_profile = None

    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/dashboard.html', context)


def update_profile(request):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.info(request, "You have successfully updated your profile")
            return redirect('accounts:dashboard')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/update_profile.html', context)


