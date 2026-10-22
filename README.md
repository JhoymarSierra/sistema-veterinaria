# Sistema de Gestión para Clínica Veterinaria

Este proyecto es un sistema de información web desarrollado en **Django 6.1.2** para gestionar los procesos operativos de una clínica veterinaria. Permite la administración integral de propietarios, mascotas, historias clínicas, personal veterinario, citas, vacunas y su respectiva aplicación.

## Equipo de Desarrollo
Este proyecto fue desarrollado bajo una metodología de trabajo colaborativo (Git/GitHub), dividiendo responsabilidades y módulos:

* **Jhoymar Sierra**: Director de Proyecto (PM) / Scrum Master & Tech Lead. 
  * *Módulos:* `propietarios`, `mascotas`, `historias_clinicas`, arquitectura base y configuración general.
* **Diego Maldonado**: Desarrollador Backend.
  * *Módulos:* `veterinarios`, `citas` y Diagrama de Casos de Uso.
* **Andrea Gonzalez**: Desarrolladora Backend.
  * *Módulos:* `vacunas`, `aplicaciones_vacunas` y Diagrama Entidad-Relación (ER).

## Arquitectura y Módulos
El proyecto está modularizado en 7 aplicaciones independientes para mantener un código limpio y escalable:
1. `propietarios`
2. `mascotas`
3. `historias_clinicas` (Entidad débil - Implementada con OneToOneField)
4. `veterinarios`
5. `citas`
6. `vacunas`
7. `aplicaciones_vacunas` (Tabla intermedia - Relación N:M)

## Características Técnicas (Cumplimiento de Rúbrica)
* **Nomenclatura Estricta de Base de Datos:** Los modelos de Django reflejan exactamente la estructura del diagrama ER, utilizando el prefijo `tbl_` para las tablas, y nombres explícitos para las llaves primarias (`pk_`) y foráneas (`fk_` usando `db_column`).
* **Panel de Administración Avanzado:** Configuración completa del `admin.py` con `list_display`, `search_fields` y `list_filter`.
* **Inlines:** Implementación de `TabularInline` y `StackedInline` para gestionar entidades débiles y tablas intermedias directamente desde el panel padre (ej. Historias Clínicas desde Mascotas, Aplicación de Vacunas desde Vacunas).
* **Datos de Prueba:** La base de datos (`db.sqlite3`) se entrega pre-poblada con un mínimo de 3 registros funcionales por cada tabla.

## Documentación
En la carpeta `docs/` de este repositorio se encuentran los diagramas de diseño del sistema:
* `diagrama_actores.png`: Diagrama UML de Casos de Uso.
* `diagrama_er.png`: Diagrama Entidad-Relación final de la base de datos.

## Instrucciones de Ejecución (Para el Evaluador)

Siga estos pasos para ejecutar el proyecto de manera local y evaluar el panel de administración:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/JhoymarSierra/sistema-veterinaria
   cd sistema-veterinaria

2. **Crear y activar el entorno virtual**
   # En Windows
   python -m venv venv
   .\venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

3. **Instalar Django**
   pip install django
   (Nota: No es necesario ejecutar migraciones ya que se incluye el archivo db.sqlite3 con las tablas y datos creados).

4. **Ejecutar el servidor local**
   python manage.py runserver

5. **Acceder al panel de administración**
   Abra su navegador y diríjase a: http://127.0.0.1:8000/admin/

6. **CREDENCIALES DE SUPERUSUARIO**
   Para calificar el trabajo dentro del panel de administración, inicie sesión con las siguientes credenciales de prueba:

   Usuario: admin

   Contraseña: jhoimar25647

Desarrollado como proyecto académico para la Universidad de La Guajira.