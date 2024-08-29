from . import views
from django.urls import path


urlpatterns = [
    path('', views.index1),
    path('users/', views.users_admin),
]