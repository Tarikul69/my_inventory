# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import render


def supper_admin(request):
    return render(request, 'supper_admin/home.html')


def product_list(request):
    return render(request, 'supper_admin/product_list.html')

def inventory(request):
    return render(request, 'supper_admin/inventory.html')

def barcode_generator(request):
    print("good")
     
    return render(request, 'supper_admin/bercode.html')