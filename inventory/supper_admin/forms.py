from django import forms

class Add_products(forms.Form):
    productName = forms.CharField(max_length=500)
    productCategory = forms.CharField()
    productQuantity = forms.CharField()
    productPrice = forms.CharField()
    purchasePrice = forms.CharField()
    productSupplier = forms.CharField(max_length=500)

