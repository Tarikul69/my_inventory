# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
