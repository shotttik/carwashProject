from django import forms
from carwash.models import Vehicle, Order, WashType, VehicleType


class VehicleForm(forms.ModelForm):
    manufacturer = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    model = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    plate_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all(),
                                          widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Vehicle
        fields = ('manufacturer', 'model', 'plate_number', 'vehicle_type')

        # widgets = {
        #     'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
        #     'model': forms.TextInput(attrs={'class': 'form-control'}),
        #     'plate_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
        # }


class OrderForm(forms.ModelForm):
    wash_type = forms.ModelChoiceField(queryset=WashType.objects.all(),
                                       widget=forms.Select(
                                           attrs={'class': 'form-control'}
                                       ))
    # completion_date = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'datetimepicker1',
    #     })
    # )
    #
    # order_date = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'datetimepicker1',
    #     })
    # )

    class Meta:
        model = Order
        fields = ('wash_type', )
