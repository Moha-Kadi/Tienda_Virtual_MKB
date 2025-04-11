# Manual Técnico del Sistema de Gestión

## Índice

- [Introducción](#introducci%C3%B3n)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Módulos y Clases](#m%C3%B3dulos-y-clases)
  - [Clase Producto](#clase-producto)
  - [Clase ProductoDigital](#clase-productodigital)
  - [Clase Cliente](#clase-cliente)
  - [Clase Pedido](#clase-pedido)
  - [Clase Reseña](#clase-rese%C3%B1a)
- [Programa Principal](#programa-principal)
- [Manejo de Errores](#manejo-de-errores)
- [Consideraciones Finales](#consideraciones-finales)

---

## Introducción

Este sistema de gestión permite administrar productos físicos y digitales, clientes, pedidos y reseñas. Está desarrollado en Python, siguiendo un enfoque de programación orientada a objetos.

## Estructura del Proyecto

```
Proyecto/
├── Clase_Producto.py
├── Clase_ProductoDigital.py
├── Clase_Cliente.py
├── Clase_Pedido.py
├── Clase_Reseña.py
└── main.py
```

## Dependencias

El sistema utiliza únicamente bibliotecas estándar de Python:

- `os` (para limpiar y pausar terminal)

## Módulos y Clases

### Clase Producto

Ubicación: `Clase_Producto.py`

Gestiona información básica de un producto:

- Atributos: `id`, `nombre`, `precio`, `stock`
- Métodos: getters/setters y `__str__()`

### Clase ProductoDigital

Ubicación: `Clase_ProductoDigital.py`

Hereda de `Producto`, añadiendo:

- Atributos adicionales como: `formato`, `tamaño`

### Clase Cliente

Ubicación: `Clase_Cliente.py`

Representa a un cliente:

- Atributos: `id`, `nombre`, `email`, `direccion`
- Métodos: getters/setters y `__str__()`

### Clase Pedido

Ubicación: `Clase_Pedido.py`

Administra pedidos:

- Atributos: `id`, `cliente`, `fecha`, `productos` (lista)
- Métodos:
  - `set_productos(producto)` agrega un producto
  - `get_productos()` devuelve la lista
  - `calcular_total()` imprime el total del pedido

### Clase Reseña

Ubicación: `Clase_Reseña.py`

Permite añadir comentarios y puntuaciones a productos:

- Hereda de `Producto` y `Cliente` (se recomienda usar composición en lugar de herencia múltiple)
- Atributos: `id_reseña`, `comentario`, `puntuacion`
- Métodos: getters/setters y `__str__()` para mostrar detalles de la reseña

## Programa Principal

Ubicación: `main.py`

Contiene el menú interactivo con 4 grandes bloques:

- **Gestión de Productos**

  - Añadir producto
  - Listar productos
  - Actualizar stock

- **Gestión de Clientes**

  - Añadir cliente
  - Listar clientes

- **Gestión de Pedidos**

  - Crear pedido
  - Listar pedido
  - Calcular total

- **Gestión de Reseñas**

  - Añadir reseña
  - Listar reseña

## Manejo de Errores

Uso básico de `try/except` en entradas de usuario para evitar interrupciones por datos inválidos:

```python
try:
    puntuacion = int(input("Introduzca puntuación: "))
except Exception as ex:
    print(f"Error: {type(ex)}")
```

## Consideraciones Finales

- La clase `Reseña` podría beneficiarse de composición (pasar instancias como atributos), en lugar de herencia múltiple.
- Se recomienda usar `os.name` para hacer `limpiar_terminal()` multiplataforma (`cls` para Windows).
- Añadir persistencia con archivos o base de datos sería un siguiente paso lógico.

---

**Autor:** *Mohamed Kadi Brikoui* **Versión:** 1.0
**Fecha:** Abril 2025

