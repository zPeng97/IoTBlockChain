from django import forms
from .models import SensorsData, LocationData


class HomeForm(forms.ModelForm):
    temp = forms.FloatField()
    IMU = forms.FloatField()
    latitude = forms.FloatField(min_value=0.0, max_value=90.0)
    longitude = forms.FloatField(min_value=0.0, max_value=180.0)

    class Meta:
        model = SensorsData
        fields = (
            'temp',
            'IMU',
            'latitude',
            'longitude'
        )


class DetailForm(forms.Form):
    ID = forms.IntegerField()


class MapForm(forms.Form):
    latitude = forms.FloatField(min_value=0.0, max_value=90.0)
    longitude = forms.FloatField(min_value=0.0, max_value=180.0)


class CheckingAddForm(forms.ModelForm):
    lat = forms.FloatField(min_value=0.0, max_value=90.0)
    long = forms.FloatField(min_value=0.0, max_value=180.0)

    class Meta:
        model = LocationData
        fields = {
            'lat',
            'long'
        }

class CheckingForm(forms.Form):
    location = forms.ModelChoiceField(queryset=LocationData.objects.all())