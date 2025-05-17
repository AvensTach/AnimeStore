from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def registrationPage(request):
    form = CustomUserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Error creating account')
            return render(request, 'accounts/registration.html', context)
    return render(request, 'accounts/registration.html', context)


def user_profile(request):
    return render(request, 'accounts/profile.html')
