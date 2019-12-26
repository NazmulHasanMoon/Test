from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        print("Post Called")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("Get Called")
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def logged_user(request):
    user = request.user
    return render(request, 'logged_user.html', {'user': user})

