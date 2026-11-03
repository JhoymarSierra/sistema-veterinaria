
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Veterinario
from .forms import VeterinarioForm


class VeterinarioCreateView(CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'veterinarios/veterinario_form.html'
    success_url = reverse_lazy('veterinario_crear')
# Create your views here.
