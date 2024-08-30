from . import views
from django.urls import path


urlpatterns = [
    path('', views.supper_admin),
    path('product/', views.product_list),
]