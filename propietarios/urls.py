from django.urls import path
from .views import PropietarioCreateView

app_name = 'propietarios'

urlpatterns = [
    path('', PropietarioCreateView.as_view(), name='crear'),
]