from django.urls import path
from .views import PropietarioCreateView

urlpatterns = [
    path('', PropietarioCreateView.as_view(), name='propietario_crear'),
]