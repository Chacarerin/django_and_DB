# 🏗️ Sistema CRUD de Productos y Fabricantes con Django ORM

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)

Aplicación web Django que implementa un sistema completo de gestión de inventario de productos y sus fabricantes. El proyecto explora el ciclo completo del desarrollo con Django ORM, desde la definición de modelos relacionales hasta la presentación de datos en plantillas renderizadas en el servidor.

## 🧠 Contexto Pedagógico y Teórico
Este proyecto aborda uno de los patrones más comunes en sistemas de información empresarial: la gestión de inventarios. Al modelar la relación entre Producto y Fabricante, se practica el concepto de **normalización de datos** (3NF) directamente en el ORM: los datos del fabricante viven en su propia tabla y se referencian mediante una clave foránea, evitando la desnormalización y garantizando la consistencia referencial. La evolución del esquema se refleja en tres migraciones sucesivas, documentando cómo el sistema de BD escala incrementalmente.

## ⚙️ Tecnologías y Frameworks Aplicados
* **Django ORM con Migraciones Iterativas**: Las tres migraciones (`0001_initial`, `0002`, `0003`) documentan la evolución del diseño de datos. Este enfoque de *database migration versioning* es el estándar de la industria para equipos que trabajan con control de versiones compartido.
* **`ForeignKey` con `on_delete=CASCADE`**: Asegura que al eliminar un Fabricante, todos sus Productos asociados se eliminen automáticamente, manteniendo la integridad referencial sin intervención manual.
* **Autenticación con `django.contrib.auth`**: Integración del sistema de autenticación nativo de Django para controlar el acceso a las vistas de escritura (agregar, editar, eliminar).

## 🛠️ Desglose Técnico (El "Cómo")
* **`productos_del_proyecto/models.py`**: Define `Fabricante` (con nombre y país) y `Producto` (con descripción, precio, fabricante y fecha de vencimiento).
* **`productos_del_proyecto/views.py`**: Vistas basadas en funciones para el CRUD completo de productos, incluyendo la vista de detalle para un producto específico.
* **`productos_del_proyecto/templates/`**: Sistema de templates con herencia desde `base.html`, incorporando templates de registro y login para el flujo de autenticación.

*Desarrollado por Rubén Schnettler.*
