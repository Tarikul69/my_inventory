from django.shortcuts import render

# Create your views here.
def supper_admin(request):
    return render(request, 'supper_admin/test.html')