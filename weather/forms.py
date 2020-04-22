from django.forms import ModelForm, TextInput
from .models import Place


class CityForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name', 'autocomplete': 'off'})}
