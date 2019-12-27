from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    return render(request, 'home.html')