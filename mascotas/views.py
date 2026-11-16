
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Mascota
from .forms import MascotaForm


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascotas:crear')


