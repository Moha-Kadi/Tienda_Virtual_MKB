# Manual de Usuario - Sistema de Gestión de Productos, Clientes, Pedidos y Reseñas

Este sistema permite gestionar productos (físicos y digitales), clientes, pedidos y reseñas a través de un menú interactivo desde la terminal.

---

## Requisitos

- Python 3.10 o superior
- Sistema operativo compatible con comandos de terminal (Linux, macOS o Windows con ajustes necesarios)

---

## Inicio del Sistema

Para ejecutar el sistema, abre una terminal y corre el archivo principal:

```bash
python main.py
```

---

## Menú Principal

Al ejecutar el sistema, verás el siguiente menú:

```
+++++++++++++++
      MENÚ
+++++++++++++++

0 - SALIR
1 - GESTIONAR PRODUCTOS
2 - GESTIONAR CLIENTES
3 - GESTIONAR PEDIDOS
4 - GESTIONAR RESEÑAS
```

Selecciona la opción deseada escribiendo el número correspondiente y presiona `Enter`.

---

## Gestión de Productos

### Opciones Disponibles:

1. **Añadir Producto:**
   - Introduce ID, nombre, precio y stock del producto.
   - El producto se guarda en una lista interna.

2. **Listar Productos:**
   - Muestra todos los productos registrados.

3. **Actualizar Stock:**
   - Selecciona el producto por su ID.
   - Introduce el nuevo stock.

---

## Gestión de Clientes

### Opciones Disponibles:

1. **Añadir Cliente:**
   - Introduce ID, nombre, email y dirección.
   - El cliente se guarda en un diccionario con su ID como clave.

2. **Listar Clientes:**
   - Muestra todos los clientes registrados.

---

## Gestión de Pedidos

### Opciones Disponibles:

1. **Crear Pedido:**
   - Introduce ID y fecha del pedido.
   - Se asignan todos los productos registrados al pedido.

2. **Listar Pedidos:**
   - Muestra el ID, fecha y productos del pedido creado.

3. **Calcular Total:**
   - Calcula el total del pedido en base al precio y stock de los productos incluidos.

---

## Gestión de Reseñas

### Opciones Disponibles:

1. **Añadir Reseña:**
   - Introduce ID, comentario y puntuación.
   - Se crea una reseña sobre el producto de un cliente específico.

2. **Listar Reseñas:**
   - Muestra el contenido de la última reseña generada.

---

## Notas Finales

- Puedes volver atrás en cualquier submenú introduciendo la opción `0`.
- Si introduces datos incorrectos, el sistema te mostrará un mensaje de error indicando el tipo de problema.

---

## Contacto y Soporte

Para reportar errores o sugerencias, contacta al desarrollador del sistema o utiliza el sistema de control de versiones si está disponible (como GitHub).

---

¡Gracias por usar el sistema de gestión!

