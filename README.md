# Sistema de Clínica Veterinaria

## Descripción
Sistema web desarrollado con Django para gestionar la información de una clínica veterinaria, incluyendo mascotas, veterinarios y citas médicas.

## Tecnologías utilizadas
- Python
- Django
- SQLite
- HTML y CSS

## Requisitos previos
- Python 3 instalado.
- Git instalado.
- Visual Studio Code (opcional).

## Instalación en Linux

### 1. Clonar el repositorio

```bash
git clone https://github.com/JhoymarSierra/sistema-veterinaria.git
cd sistema-veterinaria
```

### 2. Crear un entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

```bash
source .venv/bin/activate
```

### 4. Instalar Django

```bash
python -m pip install django
```

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 6. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Sigue las instrucciones de la terminal para definir el nombre de usuario y la contraseña. Para la cuenta compartida del equipo, coordina las credenciales por un canal privado; no publiques contraseñas en este repositorio.

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre en el navegador:

- Aplicación: http://127.0.0.1:8000/
- Administración: http://127.0.0.1:8000/admin/

## Diagrama de actores

El diagrama de actores del sistema se encuentra en:

`docs/diagrama_actores.png`

## Integrantes

Proyecto académico de desarrollo de software para una clínica veterinaria.
