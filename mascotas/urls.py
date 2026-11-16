
from django.urls import path
from .views import MascotaCreateView

app_name = 'mascotas'

urlpatterns = [
    path('', MascotaCreateView.as_view(), name='crear'),
]
