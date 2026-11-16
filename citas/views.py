
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Cita
from .forms import CitaForm


# LISTAR CITAS
class CitaListView(ListView):
    model = Cita
    template_name = 'citas/cita_list.html'
    context_object_name = 'citas'
    ordering = ['fecha']


# REGISTRAR CITAS
class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('citas:listar')


# EDITAR CITAS
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'citas/cita_form.html'
    success_url = reverse_lazy('citas:listar')


# ELIMINAR CITAS
class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'citas/cita_confirm_delete.html'
    success_url = reverse_lazy('citas:listar')


