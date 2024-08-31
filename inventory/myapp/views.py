from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def login_function(request):
    print("Good")
    if request.method == 'POST':
        print("Good-1")
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        user = authenticate(username, password)
        print(user)

        if user is not None:
            login(request, user)
            print("Good")
            return render(request, 'supper_admin/home.html')
        
        else:
            messages.error(request, "Wrong Credentials")
            return redirect('')
           

    return render(request, 'login/login.html')

