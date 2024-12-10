import sqlite3  # Librería para trabajar con bases de datos SQLite

from colorama import Fore  # Librería para manejar colores en la terminal


# Conexión a la base de datos
def conectar_bd():
    """Establece una conexión con la base de datos SQLite."""
    return sqlite3.connect("inventario.db")


# Función para mostrar los productos en formato tabla
def mostrar_tabla_productos(productos):
    # Muestra la lista de productos en formato tabular con bordes y colores

    # Definir los anchos de las columnas para mostrar en pantalla para que no deforme el recuadro
    ancho_id = 6
    ancho_nombre = 20  # Max 20 caracteres para el nombre
    ancho_descripcion = 25  # Max 25 caracteres para la descripción
    ancho_cantidad = 10
    ancho_precio = 10
    ancho_categoria = 15

    # Calcular el ancho total de la tabla
    ancho_tabla = (
        ancho_id
        + ancho_nombre
        + ancho_descripcion
        + ancho_cantidad
        + ancho_precio
        + ancho_categoria
        + 5 * 3  # Espacios entre columnas y los separadores ║
    )

    # Encabezado
    encabezado = f"{Fore.YELLOW}{'ID':<{ancho_id}} {Fore.CYAN}║ {Fore.YELLOW}{'NOMBRE':<{ancho_nombre}} {Fore.CYAN}║ {Fore.YELLOW}{'DESCRIPCIÓN':<{ancho_descripcion}} {Fore.CYAN}║ {Fore.YELLOW}{'CANTIDAD':<{ancho_cantidad}} {Fore.CYAN}║ {Fore.YELLOW}{'PRECIO':<{ancho_precio}} {Fore.CYAN}║ {Fore.YELLOW}{'CATEGORÍA':<{ancho_categoria}}"

    # Imprimir recuadro superior
    print(Fore.CYAN + "╔" + "═" * (ancho_tabla + 2) + "╗")
    print(
        Fore.CYAN
        + "║"
        + " " * ((ancho_tabla - len("Productos Registrados")) // 2)
        + "Productos Registrados"
        + " " * ((ancho_tabla - len("Productos Registrados")) // 2)
        + "  ║"
    )

    # Imprimir las líneas de separación entre encabezados
    print(
        Fore.CYAN
        + "╠"
        + f"{'═' * (ancho_id + 2)}"
        + "╦"
        + f"{'═' * (ancho_nombre + 2)}"
        + "╦"
        + f"{'═' * (ancho_descripcion + 2)}"
        + "╦"
        + f"{'═' * (ancho_cantidad + 2)}"
        + "╦"
        + f"{'═' * (ancho_precio + 2)}"
        + "╦"
        + f"{'═' * (ancho_categoria + 2)}"
        + "╣"
    )
    # Mostrar el encabezado de las columnas
    print(Fore.CYAN + "║" + Fore.YELLOW + " " + encabezado + " " + Fore.CYAN + "║")

    # Separadores entre las filas
    print(
        Fore.CYAN
        + "╠"
        + f"{'═' * (ancho_id + 2)}╬{'═' * (ancho_nombre + 2)}╬{'═' * (ancho_descripcion + 2)}╬{'═' * (ancho_cantidad + 2)}╬{'═' * (ancho_precio + 2)}╬{'═' * (ancho_categoria + 2)}"
        + "╣"
    )

    # Mostrar cada fila de los productos
    if productos:
        for idx, producto in enumerate(productos):
            precio = float(producto[4]) if producto[4] else 0.00

            # Recortar los valores si superan el tamaño máximo
            nombre = str(producto[1])[:ancho_nombre]
            descripcion = str(producto[2])[:ancho_descripcion]
            cantidad = str(producto[3])[:ancho_cantidad]
            categoria = str(producto[5])[:ancho_categoria]

            # Creo una fila con los datos formateados
            fila = (
                f"{Fore.CYAN}║{Fore.YELLOW} {str(producto[0])[:ancho_id]:<{ancho_id}} {Fore.CYAN}║ "
                f"{Fore.YELLOW}{nombre:<{ancho_nombre}} {Fore.CYAN}║ "
                f"{Fore.YELLOW}{descripcion:<{ancho_descripcion}} {Fore.CYAN}║ "
                f"{Fore.YELLOW}{cantidad:<{ancho_cantidad}} {Fore.CYAN}║ "
                f"{Fore.YELLOW}{precio:<{ancho_precio}.2f} {Fore.CYAN}║ "
                f"{Fore.YELLOW}{categoria:<{ancho_categoria}} {Fore.CYAN}║"
            )
            print(fila)

            # Imprimo las líneas de separación entre filas
            if idx < len(productos) - 1:
                print(
                    Fore.CYAN
                    + "╠"
                    + f"{'═' * (ancho_id + 2)}╬{'═' * (ancho_nombre + 2)}╬{'═' * (ancho_descripcion + 2)}╬{'═' * (ancho_cantidad + 2)}╬{'═' * (ancho_precio + 2)}╬{'═' * (ancho_categoria + 2)}"
                    + "╣"
                )

        # Línea final del recuadro
        print(
            Fore.CYAN
            + "╠"
            + f"{'═' * (ancho_id + 2)}╩{'═' * (ancho_nombre + 2)}╩{'═' * (ancho_descripcion + 2)}╩{'═' * (ancho_cantidad + 2)}╩{'═' * (ancho_precio + 2)}╩{'═' * (ancho_categoria + 2)}"
            + "╣"
        )

        # Muestro el total de registros
        mensaje = f"Total de registros: {len(productos)}"
        # Calcular el espacio sobrante
        espacio_sobrante = (ancho_tabla + 2) - len(mensaje)

        # Imprimir la línea con el mensaje centrado y ajustado al largo de la tabla
        print(
            Fore.CYAN
            + "║"
            + " " * (espacio_sobrante // 2)  # Espacio izquierdo
            + mensaje
            + " "
            * (
                espacio_sobrante // 2 + espacio_sobrante % 2
            )  # Espacio derecho, ajustando si hay sobrante
            + "║"
        )

        # Línea final del recuadro
        print(Fore.CYAN + "╚" + "═" * (ancho_tabla + 2) + "╝")

    else:
        # Si no hay productos, mostrar mensaje
        print(
            Fore.CYAN
            + "║"
            + Fore.RED
            + " " * ((ancho_tabla - len("No hay productos registrados.")) // 2)
            + "No hay productos registrados."
            + " " * ((ancho_tabla - len("No hay productos registrados.")) // 2 + 2)
            + Fore.CYAN
            + "║"
        )
        print(
            Fore.CYAN
            + "╚"
            + f"{'═' * (ancho_id + 2)}╩{'═' * (ancho_nombre + 2)}╩{'═' * (ancho_descripcion + 2)}╩{'═' * (ancho_cantidad + 2)}╩{'═' * (ancho_precio + 2)}╩{'═' * (ancho_categoria + 2)}"
            + "╝"
        )


# Función para mostrar todos los productos
def mostrar_productos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    # funcion para mostrar los productos esta la puedo re utilizar en varios modulos como busqueda etc...
    mostrar_tabla_productos(productos)

    conn.close()


# Función para actualizar un producto por su ID
def obtener_productos():
    try:
        # Establezco la conexión con la base de datos SQLite
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        # Consulta SQL para obtener los productos
        cursor.execute(
            "SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos"
        )
        productos = cursor.fetchall()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        # Convertir los productos en un diccionario
        lista_productos = []
        for producto in productos:
            lista_productos.append(
                {
                    "id": producto[0],
                    "nombre": producto[1],
                    "descripcion": producto[2],
                    "cantidad": producto[3],
                    "precio": producto[4],
                    "categoria": producto[5],
                }
            )

        return lista_productos

    except sqlite3.Error as e:
        print(f"Error al obtener productos: {e}")
        return []


def actualizar_producto(id_producto, nombre, descripcion, categoria, cantidad, precio):
    """Actualiza los datos de un producto en la base de datos"""
    try:
        # Establecer la conexión con la base de datos SQLite
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        # Consulta en SQL para actualizar el producto
        cursor.execute(
            """
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """,
            (nombre, descripcion, cantidad, precio, categoria, id_producto),
        )

        # Guardar los cambios
        conexion.commit()

        # Cerrar la conexión
        cursor.close()
        conexion.close()

        print(Fore.GREEN + "Producto actualizado correctamente." + Fore.RESET)

    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")


def cargar_campos_para_actualizar():
    # Obtener los productos existentes
    productos = (
        obtener_productos()
    )  # Esta función debe devolver una lista de diccionarios con los productos.

    try:
        # Pedir al usuario que seleccione un producto por ID
        id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))

        # Buscar el producto por ID
        producto_seleccionado = next(
            (prod for prod in productos if prod["id"] == id_producto), None
        )

        if not producto_seleccionado:
            print(Fore.RED + "No se encontró un producto con ese ID." + Fore.RESET)
            return

    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido." + Fore.RESET)
        return

    # Mostrar los detalles del producto seleccionado
    recuadrar_mensaje_seleccionado(producto_seleccionado)

    # Pedir los nuevos valores para actualizar el producto
    nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
    descripcion = input("Nueva descripción (dejar en blanco para no cambiar): ")
    try:
        cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
        cantidad = int(cantidad) if cantidad else producto_seleccionado["cantidad"]
        precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
        precio = float(precio) if precio else producto_seleccionado["precio"]
        categoria = input("Nueva categoría (dejar en blanco para no cambiar): ")
    except ValueError:
        print(Fore.RED + "Valor no válido para cantidad o precio." + Fore.RESET)
        return

    # Actualizar producto en la base de datos
    actualizar_producto(
        producto_seleccionado["id"],
        nombre if nombre else producto_seleccionado["nombre"],
        descripcion if descripcion else producto_seleccionado["descripcion"],
        categoria if categoria else producto_seleccionado["categoria"],
        cantidad,
        precio,
    )


# Función para eliminar un producto por su ID
def eliminar_producto(id_producto):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "Producto eliminado con éxito." + Fore.RESET)


# Función para buscar productos secuencialmente en varios campos los cuales son Nombre descripcion categoria y ID
def buscar_producto(valor):
    # Lista de campos por los que buscar (en orden de prioridad)
    campos = ["id", "nombre", "descripcion", "categoria"]

    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()

    # Intentar buscar en cada campo
    for campo in campos:
        # Construir la consulta SQL de manera dinámica
        consulta = f"SELECT * FROM productos WHERE {campo} LIKE ?"
        cursor.execute(consulta, (f"%{valor}%",))
        productos = cursor.fetchall()

        # Si encontramos productos, los mostramos
        if productos:
            mostrar_tabla_productos(productos)
            break  # Sale del bucle si se encuentran productos

    # Si no se encontraron productos, mostramos un mensaje de error
    else:
        print(
            Fore.RED
            + "Producto(s) no encontrado(s) en ninguno de los campos."
            + Fore.RESET
        )

    # Cerrar la conexión
    conn.close()


# Función para generar un reporte de bajo stock
# Podria haber colocado un campo en la base de datos de Stock y otro para Stock minimo y de esta forma generaria el reporte de bajo stock
def reporte_bajo_stock(limite):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    mostrar_tabla_productos(productos)

    conn.close()


# funcion para agregar un producto a la base
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conn.commit()
    conn.close()

    # Mensaje de confirmación de que ingrese un producto mas y lo muestra recuadrado
    mensaje = "Producto agregado con éxito."
    ancho_caja = len(mensaje) + 4

    print(Fore.GREEN + "╔" + "═" * ancho_caja + "╗")
    print(
        "║"
        + " " * ((ancho_caja - len(mensaje)) // 2)
        + mensaje
        + " " * ((ancho_caja - len(mensaje)) // 2)
        + "║"
    )
    print("╚" + "═" * ancho_caja + "╝" + Fore.RESET)


def recuadrar_mensaje_seleccionado(producto_seleccionado):
    # Muestra los detalles del producto seleccionado dentro de un cuadro con bordes y colores.
    # Definir el ancho del cuadro
    ancho_cuadro = 60

    # Crear el mensaje con los detalles del producto
    mensaje = f"Producto seleccionado: {producto_seleccionado['nombre']}\n"
    mensaje += f"ID: {producto_seleccionado['id']}\n"
    mensaje += f"Descripción: {producto_seleccionado['descripcion']}\n"
    mensaje += f"Cantidad: {producto_seleccionado['cantidad']}\n"
    mensaje += f"Precio: {producto_seleccionado['precio']}\n"
    mensaje += f"Categoría: {producto_seleccionado['categoria']}\n"

    # Calcular el número de líneas que necesita el cuadro
    lineas = mensaje.split("\n")

    # Imprimir el recuadro superior
    print(Fore.CYAN + "╔" + "═" * (ancho_cuadro) + "╗")

    # Imprimir las líneas de información alineadas a la izquierda
    for linea in lineas:
        # Asegurarse de que el texto quede alineado a la izquierda
        espacio_derecha = (
            ancho_cuadro - len(linea) - 2
        )  # Restamos 2 por las '║' en los extremos
        print(
            Fore.CYAN
            + "║"
            + Fore.YELLOW
            + linea
            + " " * espacio_derecha
            + Fore.CYAN
            + "  ║"
        )

    # Imprimir el recuadro inferior
    print(Fore.CYAN + "╚" + "═" * (ancho_cuadro) + "╝")
