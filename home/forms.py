from django import forms
from .models import SensorsData


class HomeForm(forms.ModelForm):
    temp = forms.FloatField()
    IMU = forms.FloatField()
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    class Meta:
        model = SensorsData
        fields = ('temp', 'IMU', 'latitude', 'longitude')


class DetailForm(forms.Form):
    ID = forms.IntegerField()
