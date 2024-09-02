from django.shortcuts import render

from supper_admin.models import product

# Create your views here.
def users_admin(request):
    return render(request, 'users_admin/home.html')

def purchage(request):
    products = product.objects.all()
    return render(request, 'users_admin/purchage.html', {'products': products})