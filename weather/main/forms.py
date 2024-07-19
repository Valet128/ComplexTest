from django.forms import ModelForm, TextInput
from .models import Weather


class CityForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['title']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Введите город',
                'list': 'cities',
                'class': 'input-city form-control'
            })
        }
