from django.shortcuts import render

# Create your views here.
def supper_admin(request):
    return render(request, 'supper_admin/home.html')


def product_list(request):
    return render(request, 'supper_admin/product_list.html')