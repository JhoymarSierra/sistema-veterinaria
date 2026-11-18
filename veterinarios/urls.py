from django.urls import path
from .views import VeterinarioCreateView

app_name = 'veterinarios'

urlpatterns = [
    path(
        '',
        VeterinarioCreateView.as_view(),
        name='veterinario_crear'
    ),
]
