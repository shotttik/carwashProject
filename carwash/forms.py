from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['plate_number', ]

    def clean_plate_number(self):
        plate_number = self.cleaned_data.get('plate_number')
        if not plate_number.isdigit() and plate_number.isalpha():
            raise forms.ValidationError("Please Enter Correctly. ex.`AA000BB`")
        return plate_number
