
from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'especie': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'raza': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'propietario': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

