from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('custom_login/', views.login_function),
]
