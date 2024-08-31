from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def custom_login(request):
    pass