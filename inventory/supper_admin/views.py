# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import render

from supper_admin.models import product


def supper_admin(request):
    return render(request, 'supper_admin/home.html')


def product_list(request):
    products = product.objects.all()
    return render(request, 'supper_admin/product_list.html', {'products': products})

def inventory(request):
    return render(request, 'supper_admin/inventory.html')

def barcode_generator(request):
    print("good")
     
    return render(request, 'supper_admin/bercode.html')