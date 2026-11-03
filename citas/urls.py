from django.urls import path
from .views import CitaCreateView

urlpatterns = [
    path(
        '',
        CitaCreateView.as_view(),
        name='cita_crear'
    ),
]
