from django import forms
from .models import Cita


class CitaForm(forms.ModelForm):

    fecha = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }
        )
    )

    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'mascota': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'veterinario': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'motivo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }
