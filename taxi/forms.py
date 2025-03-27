from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Driver, Car
from taxi.validators import validate_driver_license


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(validators=[validate_driver_license],
                                     required=True)

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "license_number",)


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(validators=[validate_driver_license],
                                     required=True)

    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "license_number",)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"
