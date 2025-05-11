# 🗃️ Sistema de Inventario con Base de Datos (MySQL)

Este proyecto es una aplicación de consola en Python que permite gestionar un inventario de productos con persistencia en base de datos MySQL. Está diseñado aplicando buenas prácticas como separación en capas, acceso a datos mediante DAO y programación orientada a objetos.

## 🔧 Funcionalidades

- Conexión a base de datos MySQL
- Añadir productos
- Listar productos del inventario
- Buscar, actualizar y eliminar productos
- Arquitectura modular: separación entre lógica, conexión y modelo

## 🧱 Arquitectura

- `producto.py`: clase `Producto` con atributos básicos (nombre, stock, precio, etc.)
- `conexion.py`: gestiona la conexión a la base de datos MySQL
- `gestioninventarioDAO.py`: contiene métodos CRUD (Create, Read, Update, Delete)
- `Main.py`: punto de entrada con menú de consola para interactuar

## 🛠️ Requisitos

- Python 3.x
- MySQL instalado
- Librería `mysql-connector-python`

## ▶️ Cómo usarlo

1. **Instala Python 3.x** si no lo tienes.

2. **Instala el conector de MySQL para Python**:

```bash
pip install mysql-connector-python
