from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def custom_login(request):
    if request.method == 'POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')  # Redirect to a desired page after successful login
         else:
            messages.error(request, "Invalid username or password.")
      else:
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})