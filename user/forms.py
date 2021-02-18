from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from user.models import User


class CustomUserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn`t match.',
    }
    password1 = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),
        strip=False,
        help_text='Enter the same password as before, for verification',
    )
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'image',
            'password1',
            'password2',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return
