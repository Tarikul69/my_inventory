from django.shortcuts import render

# Create your views here.
def users_admin(request):
    return render(request, 'users_admin/abcd.html')

def index1(request):
    return render(request, 'users_admin/home.html')