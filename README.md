# Sistema de Gestión para Clínica Veterinaria

## Descripción

Este proyecto es un sistema de información web desarrollado en **Django 6.1.2** para gestionar los procesos operativos de una clínica veterinaria. Permite la administración integral de propietarios, mascotas, historias clínicas, personal veterinario, citas, vacunas y su respectiva aplicación.

## Integrantes

Este proyecto fue desarrollado bajo una metodología de trabajo colaborativo (Git/GitHub), dividiendo responsabilidades y módulos.

| Integrante | Usuario de GitHub | Rol | Módulos |
|---|---|---|---|
| Jhoymar Sierra | [@JhoymarSierra](https://github.com/JhoymarSierra) | Director de Proyecto (PM) / Scrum Master & Tech Lead | `propietarios`, `mascotas`, `historias_clinicas`, arquitectura base y configuración general |
| Diego Maldonado | [@Guerolman123](https://github.com/Guerolman123) | Desarrollador Backend | `veterinarios`, `citas` y Diagrama de Casos de Uso |
| Andrea Gonzalez | [@carolina-1808](https://github.com/carolina-1808) | Desarrolladora Backend | `vacunas`, `aplicaciones_vacunas` y Diagrama Entidad-Relación (ER) |

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| Django 6.1.2 | Framework web (modelos, vistas, plantillas y panel de administración) |
| SQLite (`db.sqlite3`) | Base de datos |
| Bootstrap | Estilos y diseño de la interfaz |
| Git y GitHub | Control de versiones (ramas `main`, `develop` y `feature/*`) |

### Cómo se incluyó Bootstrap

[COMPLETAR: indicar cuál de estas opciones se usó]

- **Opción CDN:** Bootstrap se carga desde un enlace CDN en la plantilla base (`templates/base.html`), con la etiqueta `<link>` para los estilos en el `<head>` y la etiqueta `<script>` del paquete JS antes de cerrar el `</body>`. Todas las plantillas heredan de esa base con `{% extends 'base.html' %}`.
- **Opción archivos estáticos:** los archivos de Bootstrap se descargaron a la carpeta `static/` y se cargan con `{% load static %}` y `{% static '...' %}`.

## Arquitectura y módulos

El proyecto está modularizado en 7 aplicaciones independientes para mantener un código limpio y escalable:

1. `propietarios`
2. `mascotas`
3. `historias_clinicas`
4. `veterinarios`
5. `citas`
6. `vacunas`
7. `aplicaciones_vacunas`

## Base de datos: tabla de entidades

Convención de nombres: tablas con prefijo `tbl_`, llaves primarias `pk_` y llaves foráneas `fk_`, seguidas de las iniciales de la tabla.

| App | Tabla | Llave primaria | Llaves foráneas | Relación |
|---|---|---|---|---|
| `propietarios` | `tbl_propietario` | `pk_pro_id` | — | 1 a N con `tbl_mascota` |
| `mascotas` | `tbl_mascota` | `pk_mas_id` | `fk_pro_id` | 1 a 1 con `tbl_historia_clinica`, 1 a N con `tbl_cita` y con `tbl_aplicacion_vacuna` |
| `historias_clinicas` | `tbl_historia_clinica` | `pk_his_id` | `fk_mas_id` | 1 a 1 con `tbl_mascota` |
| `veterinarios` | `tbl_veterinario` | `pk_vet_id` | — | 1 a N con `tbl_cita` |
| `citas` | `tbl_cita` | `pk_cit_id` | `fk_mas_id`, `fk_vet_id` | N a 1 con mascota y con veterinario |
| `vacunas` | `tbl_vacuna` | `pk_vac_id` | — | 1 a N con `tbl_aplicacion_vacuna` |
| `aplicaciones_vacunas` | `tbl_aplicacion_vacuna` | `pk_apv_id` | `fk_mas_id`, `fk_vac_id` | Tabla intermedia de la relación N a M entre mascota y vacuna |

## Documentación y diagramas

En la carpeta `docs/` de este repositorio se encuentran los diagramas de diseño del sistema:

| Archivo | Descripción |
|---|---|
| [`docs/diagrama_actores.png`](docs/diagrama_actores.png) | Diagrama UML de Casos de Uso |
| [`docs/diagrama_er.png`](docs/diagrama_er.png) | Diagrama Entidad-Relación final de la base de datos |

## Funcionalidades

- **CRUD completo** para cada entidad: crear, listar, editar y eliminar.
- **Panel de Administración Avanzado:** configuración completa del `admin.py` con `list_display`, `search_fields` y `list_filter`.
- **Inlines:** implementación de `TabularInline` y `StackedInline` para gestionar entidades débiles y tablas intermedias directamente desde el panel padre (por ejemplo, historias clínicas desde mascotas y aplicación de vacunas desde vacunas).
- **Datos de prueba:** la base de datos (`db.sqlite3`) se entrega pre-poblada con un mínimo de 3 registros funcionales por cada tabla.

### Rutas del CRUD

[COMPLETAR: reemplazar las rutas por las reales de cada `urls.py`]

| Módulo | Listar | Crear | Editar | Eliminar |
|---|---|---|---|---|
| Propietarios | `/propietarios/` | `/propietarios/crear/` | `/propietarios/<id>/editar/` | `/propietarios/<id>/eliminar/` |
| Mascotas | `/mascotas/` | `/mascotas/crear/` | `/mascotas/<id>/editar/` | `/mascotas/<id>/eliminar/` |
| Historias clínicas | `/historias/` | `/historias/crear/` | `/historias/<id>/editar/` | `/historias/<id>/eliminar/` |
| Veterinarios | `/veterinarios/` | `/veterinarios/crear/` | `/veterinarios/<id>/editar/` | `/veterinarios/<id>/eliminar/` |
| Citas | `/citas/` | `/citas/crear/` | `/citas/<id>/editar/` | `/citas/<id>/eliminar/` |
| Vacunas | `/vacunas/` | `/vacunas/crear/` | `/vacunas/<id>/editar/` | `/vacunas/<id>/eliminar/` |
| Panel de administración | `/admin/` | | | |

## Instrucciones de ejecución (para el evaluador)

Siga estos pasos para ejecutar el proyecto de manera local y evaluar el panel de administración.

**1. Clonar el repositorio**

```bash
git clone https://github.com/JhoymarSierra/sistema-veterinaria
cd sistema-veterinaria
```

**2. Crear y activar el entorno virtual**

En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**4. Aplicar las migraciones**

```bash
python manage.py migrate
```

**5. Ejecutar el servidor**

```bash
python manage.py runserver
```

**6. Abrir en el navegador**

- Aplicación: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## Usuarios de prueba

[COMPLETAR: poner los usuarios reales que existen en `db.sqlite3`]

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `[contraseña]` | Superusuario (acceso a `/admin/`) |

> La carpeta `venv/` y los archivos `__pycache__/` están excluidos del repositorio mediante `.gitignore`.


  
