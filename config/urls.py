from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ruta principal http://127.0.0.1:8000/
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Autenticación (Login y Logout)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Panel de administración
    path('admin/', admin.site.urls),

    # Aplicaciones
    path('propietarios/', include('propietarios.urls')),
    path('mascotas/', include('mascotas.urls')),
    path('citas/', include('citas.urls')),
    # Si en la carpeta 'veterinarios' ya crearon el archivo 'urls.py', descomenta la línea de abajo:
    path('veterinarios/', include('veterinarios.urls')),
]