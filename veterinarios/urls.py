from django.urls import path
from .views import VeterinarioCreateView

urlpatterns = [
    path(
        '',
        VeterinarioCreateView.as_view(),
        name='veterinario_crear'
    ),
]
