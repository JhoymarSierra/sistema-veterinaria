
from django.urls import path

from .views import (
    CitaListView,
    CitaCreateView,
    CitaUpdateView,
    CitaDeleteView,
)

app_name = 'citas'

urlpatterns = [
    path('', CitaListView.as_view(), name='listar'),
    path('crear/', CitaCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', CitaUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', CitaDeleteView.as_view(), name='eliminar'),
]



