# Proyecto Final Integrador - Gestión de Inventario

## Descripción
Esta aplicación permite gestionar el inventario de una pequeña tienda. 
Incluye funcionalidades como registro, actualización, eliminación, búsqueda de productos,
 y generación de reportes de stock bajo.

## Requerimientos
- Python 3.7 o superior
- Biblioteca `sqlite3` (incluida por defecto)
- Opcional: Biblioteca `colorama` para colores en la terminal.

## Funcionalidades
1. Registro de productos: Agrega un producto con sus detalles.
2. Visualización: Muestra todos los productos del inventario.
3. Actualización: Modifica la cantidad de un producto por su ID.
4. Eliminación: Elimina un producto por su ID.
5. Búsqueda: Encuentra productos por ID, nombre o categoría.
6. Reporte: Muestra productos con stock bajo según el límite.

## Ejecución
1. Asegúrate de tener Python instalado.
2. Ejecuta `main.py` desde la terminal: `python main.py`.
3. Sigue las instrucciones en pantalla.

## Notas
- La base de datos `inventario.db` se crea automáticamente si no existe.
- Los productos se almacenan localmente en SQLite.
