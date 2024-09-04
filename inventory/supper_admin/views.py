# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import Add_products

from supper_admin.models import product


def supper_admin(request):
    return render(request, 'supper_admin/home.html')


def product_list(request):
    products = product.objects.all()
    return render(request, 'supper_admin/product_list.html', {'products': products})

#Add product to the inventory
def add_product(request):
    if request.method == 'POST':
        form = Add_products(request.POST)
        print("Good1")
        if form.is_valid():
            #form.save()
            print(form)
            return redirect('/supper_admin/product/')
    else:
        form = Add_products()
    #return render(request, 'supper_admin/product_list.html', {'form':form})

def inventory(request):
    return render(request, 'supper_admin/inventory.html')

def barcode_generator(request):
    print("good")
     
    return render(request, 'supper_admin/bercode.html')