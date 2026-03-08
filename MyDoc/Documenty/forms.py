from .models import Filials
from django.forms import ModelForm, TextInput, NumberInput

class FilialsForm(ModelForm):
    class Meta:
        model = Filials
        fields = ['title']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
        }
