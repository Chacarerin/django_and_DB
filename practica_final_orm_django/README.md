# 🏗️ Sistema CRUD de Laboratorios con Django ORM

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)

Este proyecto representa la práctica final del módulo de Django ORM. Implementa un sistema web de gestión de laboratorios farmacéuticos con autenticación de usuarios y operaciones CRUD completas sobre entidades relacionadas.

## 🧠 Contexto Pedagógico y Teórico
La arquitectura Django MVT (Model-View-Template) separa las responsabilidades del sistema de forma clara: el modelo encapsula la lógica de datos y sus validaciones, la vista orquesta la lógica de negocio, y la plantilla maneja la presentación. Este proyecto demuestra cómo el ORM de Django actúa como una capa de abstracción sobre la base de datos relacional, permitiendo expresar consultas SQL complejas como sentencias Python idiomáticas, reduciendo drásticamente el riesgo de inyección SQL y mejorando la mantenibilidad.

## ⚙️ Tecnologías y Frameworks Aplicados
* **Django ORM**: Elegido por su capacidad de definir el esquema de base de datos directamente desde el modelo Python (Code-First), permitiendo que el sistema de migraciones (`makemigrations` y `migrate`) versione el esquema de la BD de forma controlada y auditada.
* **Validadores de Modelo (`validators`)**: Se aplica validación a nivel de modelo (ej. `validar_anno` en `f_fabricacion`) para garantizar la integridad de datos antes de que lleguen a la capa de persistencia, siguiendo el principio de *Fail Fast*.
* **Relaciones ORM (`ForeignKey`, `OneToOneField`)**: La relación `Producto → Laboratorio` (ForeignKey) modela una relación N:1, mientras que `DirectorGeneral → Laboratorio` (OneToOneField) impone una cardinalidad 1:1, ambas expresadas directamente en el modelo de datos con restricciones de integridad referencial.

## 🛠️ Desglose Técnico (El "Cómo")
* **`laboratorio/models.py`**: Define las entidades `Laboratorio`, `DirectorGeneral` y `Producto` con sus relaciones, restricciones de integridad y validadores de campo personalizados.
* **`laboratorio/views.py`**: Implementa vistas basadas en funciones (FBV) para las operaciones Crear, Leer, Actualizar y Eliminar (CRUD) de los registros.
* **`laboratorio/forms.py`**: Utiliza `ModelForm` de Django para generar formularios HTML ligados directamente al modelo, con validación automática en el servidor.
* **`laboratorio/templates/`**: Templates HTML que extienden de `base.html` para mantener un diseño consistente con herencia de plantillas.

*Desarrollado por Rubén Schnettler.*
