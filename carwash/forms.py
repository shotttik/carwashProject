from django import forms
from django.forms import ModelChoiceField
from carwash.models import Vehicle, Order, WashType, VehicleType


class VehicleForm(forms.ModelForm):
    # manufacturer
    # model
    # plate_number =
    vehicle_type = ModelChoiceField(empty_label='Choose Type', queryset=VehicleType.objects.all())

    class Meta:
        model = Vehicle
        fields = ('manufacturer', 'model', 'plate_number', 'vehicle_type')
