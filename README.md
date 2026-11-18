# Sistema de Gestión para Clínica Veterinaria

## Descripción

Sistema de información web desarrollado en **Django 6.1.2** para gestionar los procesos operativos y clínicos de una clínica veterinaria. Permite administrar propietarios, mascotas, historias clínicas, personal veterinario, agendamiento de citas, catálogo de vacunas y su aplicación.

## Integrantes

Proyecto desarrollado bajo metodología colaborativa con Git y GitHub, dividiendo responsabilidades por módulos funcionales y diseño de base de datos:

| Integrante | Usuario de GitHub | Rol | Módulos |
| :--- | :--- | :--- | :--- |
| Jhoymar Sierra | [@JhoymarSierra](https://github.com/JhoymarSierra) | Director de Proyecto (PM) / Scrum Master & Tech Lead | `propietarios`, `mascotas`, `historias_clinicas`, arquitectura base, autenticación y configuración general |
| Diego Maldonado | [@Guerolman123](https://github.com/Guerolman123) | Desarrollador Backend | `veterinarios`, `citas` (CRUD completo) y Diagrama de Casos de Uso |
| Andrea Gonzalez | [@carolina-1808](https://github.com/carolina-1808) | Desarrolladora Backend | `vacunas`, `aplicaciones_vacunas` y Diagrama Entidad-Relación (ER) |

## Tecnologías

| Tecnología | Uso |
| :--- | :--- |
| Python | Lenguaje de programación principal |
| Django 6.1.2 | Framework web (ORM, vistas basadas en clases, plantillas y panel administrativo) |
| SQLite (`db.sqlite3`) | Motor de base de datos relacional |
| Bootstrap 5 | Diseño responsivo y estilizado de interfaz de usuario |
| Git y GitHub | Control de versiones con flujo de ramas (`main`, `develop` y `feature/*`) |

### Integración de Bootstrap

Bootstrap 5 se carga mediante **CDN** en la plantilla base global (`templates/base.html`), incluyendo la hoja de estilos en el `<head>` y el paquete JavaScript antes del cierre de `</body>`. Todas las vistas públicas del sistema heredan esta estructura mediante `{% extends 'base.html' %}` y utilizan espacios de nombres (`app_name`) en sus rutas.

## Arquitectura y módulos

El proyecto está modularizado en 7 aplicaciones independientes dentro de `config/`:

1. `propietarios` — Registro operativo de dueños de mascotas.
2. `mascotas` — Registro de mascotas vinculadas a sus propietarios.
3. `citas` — Proceso principal del negocio con CRUD completo en interfaz web.
4. `veterinarios` — Gestión del personal médico veterinario.
5. `historias_clinicas` — Registro clínico asociado a cada mascota.
6. `vacunas` — Catálogo de biológicos y vacunas disponibles.
7. `aplicaciones_vacunas` — Registro de aplicación de vacunas por mascota.

## Base de datos: tabla de entidades

Convención de nombres aplicada: tablas con prefijo `tbl_`, llaves primarias `pk_` y llaves foráneas `fk_`, seguidas de las iniciales de la entidad.

| App | Tabla | Llave primaria | Llaves foráneas | Cardinalidad y relación |
| :--- | :--- | :--- | :--- | :--- |
| `propietarios` | `tbl_propietario` | `pk_pro_id` | — | **1 a N** con `tbl_mascota` |
| `mascotas` | `tbl_mascota` | `pk_mas_id` | `fk_pro_id` | **1 a 1** con `tbl_historia_clinica`; **1 a N** con `tbl_cita` y `tbl_aplicacion_vacuna` |
| `historias_clinicas` | `tbl_historia_clinica` | `pk_his_id` | `fk_mas_id` | **Entidad débil** dependiente de `tbl_mascota` |
| `veterinarios` | `tbl_veterinario` | `pk_vet_id` | — | **1 a N** con `tbl_cita` |
| `citas` | `tbl_cita` | `pk_cit_id` | `fk_mas_id`, `fk_vet_id` | **N a 1** con `tbl_mascota` y `tbl_veterinario` |
| `vacunas` | `tbl_vacuna` | `pk_vac_id` | — | **1 a N** con `tbl_aplicacion_vacuna` |
| `aplicaciones_vacunas` | `tbl_aplicacion_vacuna` | `pk_apv_id` | `fk_mas_id`, `fk_vac_id` | Tabla intermedia de relación **N a M** entre mascota y vacuna |

## Documentación y diagramas

En la carpeta `docs/` de este repositorio se encuentran los diagramas de diseño del sistema:

| Diagrama | Descripción |
| :--- | :--- |
| [Diagrama de Casos de Uso](docs/diagrama_actores.png) | Diagrama UML de actores y casos de uso del sistema |
| [Diagrama Entidad-Relación](docs/diagrama_er.png) | Diagrama Entidad-Relación final de la base de datos |

## Funcionalidades

* **CRUD completo en interfaz web** para el proceso principal (**Citas**): listar, crear, editar y eliminar registros con vistas basadas en clases (`ListView`, `CreateView`, `UpdateView`, `DeleteView`).
* **Flujo operativo integrado:** registro de **Propietarios** y **Mascotas** en frontend conectados directamente con la programación de citas médicas.
* **Autenticación y control de acceso:** inicio y cierre de sesión integrados con la plantilla base del sistema.
* **Panel de Administración Avanzado (`/admin/`):** configuración personalizada con `list_display`, `search_fields`, `list_filter` e *inlines* (`TabularInline` / `StackedInline`) para gestionar entidades débiles y tablas intermedias (`historias_clinicas`, `veterinarios`, `vacunas`, `aplicaciones_vacunas`).
* **Base de datos pre-poblada:** `db.sqlite3` incluye datos de prueba consistentes y realistas listos para evaluación.

### Rutas del sistema

| Módulo / Vista | Operación | Ruta URL | Nombre de ruta (`app_name`) |
| :--- | :--- | :--- | :--- |
| Inicio | Página principal | `/` | `home` |
| Autenticación | Iniciar sesión | `/login/` | `login` |
| Autenticación | Cerrar sesión | `/logout/` | `logout` |
| Propietarios | Registrar propietario | `/propietarios/` | `propietarios:crear` |
| Mascotas | Registrar mascota | `/mascotas/` | `mascotas:crear` |
| Citas | Listar citas | `/citas/` | `citas:listar` |
| Citas | Crear cita | `/citas/crear/` | `citas:crear` |
| Citas | Editar cita | `/citas/editar/<int:pk>/` | `citas:editar` |
| Citas | Eliminar cita | `/citas/eliminar/<int:pk>/` | `citas:eliminar` |
| Administración | Gestión de catálogos y registros clínicos | `/admin/` | `admin:index` |

## Instrucciones de ejecución (para el evaluador)

**1. Clonar el repositorio**

```bash
git clone https://github.com/JhoymarSierra/sistema-veterinaria.git
cd sistema-veterinaria
```

**2. Crear y activar el entorno virtual**

En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

En macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**4. Verificar migraciones (opcional)**

El repositorio incluye `db.sqlite3` con las migraciones aplicadas y datos de prueba cargados. Si desea verificar el estado de la base de datos:

```bash
python manage.py migrate
```

**5. Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

**6. Acceder en el navegador**

* **Aplicación web:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Panel de administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Usuarios de prueba

| Usuario | Contraseña | Rol |
| :--- | :--- | :--- |
| `admin` | `jhoimar25647` | Superusuario (acceso completo al sistema y a `/admin/`) |

> **Nota:** La carpeta `venv/` y los archivos temporales `__pycache__/` están excluidos del repositorio mediante `.gitignore`.
  
