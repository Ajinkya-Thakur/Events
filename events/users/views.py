from django.shortcuts import render, redirect
from events import settings
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('events/')
    return render(request, "home.html")
