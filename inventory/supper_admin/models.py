# models.py
from django.db import models

class product(models.Model):
    p_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    supplier = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

