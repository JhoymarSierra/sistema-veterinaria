from django import forms
from .models import Veterinario


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = '__all__'
        widgets = {
            'tarjeta_profesional': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'especialidad': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }

