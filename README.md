# 🐘 Prácticas de ORM en Django

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Este repositorio contiene proyectos orientados al dominio del **Object-Relational Mapping (ORM)** de Django, con énfasis en la conexión, consulta y manipulación de Bases de Datos Relacionales directamente desde código Python, sin necesidad de escribir SQL puro.

## 🗂️ Proyectos y Ejercicios

El repositorio está dividido en prácticas que abarcan desde conceptos básicos hasta interacciones más avanzadas con la base de datos:

### 1. `practica_orm`
Ejercicios introductorios al ORM. 
- Creación de modelos simples.
- Migraciones básicas (makemigrations, migrate).
- Operaciones CRUD fundamentales usando la shell de Django (`python manage.py shell`).

### 2. `practica_final_orm_django`
Aplicación integradora que pone a prueba los conocimientos adquiridos.
- Modelos relacionales complejos (OneToOne, ForeignKey, ManyToMany).
- Consultas avanzadas usando `filter()`, `exclude()`, `Q` objects y agregaciones.
- Integración del ORM con vistas para mostrar datos dinámicamente.

---

## 🛠️ Cómo Iniciar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Chacarerin/django_and_DB.git
   ```
2. Entra al directorio del ejercicio que deseas probar.
3. Crea y activa tu entorno virtual.
4. Instala las dependencias y ejecuta las migraciones:
   ```bash
   python manage.py migrate
   ```
5. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---
*Desarrollado por Rubén Schnettler.*
