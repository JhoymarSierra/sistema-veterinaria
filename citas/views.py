from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Cita
from .forms import CitaForm


class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('cita_crear')
# Create your views here.
