from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Propietario
from .forms import PropietarioForm

class PropietarioCreateView(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'propietarios/propietario_form.html'
    success_url = reverse_lazy('propietario_crear')