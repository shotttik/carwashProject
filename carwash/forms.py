from django import forms
from carwash.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('wash_type', 'price', 'order_date', 'washer')
