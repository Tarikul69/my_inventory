from django.shortcuts import render

# Create your views here.
def users_admin(request):
    return render(request, 'users_admin/home.html')

def purchage(request):
    return render(request, 'users_admin/purchage.html')