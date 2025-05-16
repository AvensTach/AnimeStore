from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        raise exception("Not implemented yet")
    else:
        return render(request, 'accounts/login.html')

def registraion(request):
    form = CustomUserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'accounts/registration.html', context)
    else:
        return render(request, 'accounts/registration.html', context)

def user_profile(request):
    raise excration("Not implemented yet")