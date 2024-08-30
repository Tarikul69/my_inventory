from . import views
from django.urls import path


urlpatterns = [
    path('', views.users_admin),
    path('purchage/', views.purchage),
]