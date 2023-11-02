from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Sprzedaz

class CategoryForm(ModelForm):
    class Meta:
        model = Sprzedaz
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }