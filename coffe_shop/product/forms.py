from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(
        max_length=300, label="Descripción", widget=forms.Textarea
    )
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponibilidad", required=False)
    photo = forms.ImageField(required=False, label="Foto")

    class Meta:
        model = Product
        fields = ["name", "description", "price", "available", "photo"]

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product
