# Autor de este programa Luis A Bentancur

import funciones  # Permite acceder a las funciones definidas en el módulo funciones.py
from colorama import (
    init,
    Fore,
)  # funcion para inicializar la biblioteca para los colores de pantalla

init()


def mostrar_menu():
    # Muestra el menú principal con borde y colores
    # Definir el ancho del menú
    ancho_menu = 35  # Ancho total del menú
    ancho_opcion = 30  # Ancho para las opciones

    # Imprime la parte superior del recuadro
    print(Fore.CYAN + "╔" + "═" * (ancho_menu - 3) + "╗")

    # Título del menú centrado
    print(
        Fore.CYAN
        + "║"
        + " " * ((ancho_menu - len("Menu Principal")) // 2)
        + "Menu Principal"
        + " " * ((ancho_menu - len("Menu Principal") - 4) // 2)
        + "║"
    )

    # Imprime la línea de separación
    print(Fore.CYAN + "╠" + "═" * (ancho_menu - 3) + Fore.CYAN + "╣")

    # Opciones del menú
    opciones = [
        "1. Agregar producto",
        "2. Mostrar productos",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Buscar producto",
        "6. Reporte de bajo stock",
        "0. Salir",
    ]

    # Imprime cada opción, alineando la opción a la izquierda dentro del borde
    for opcion in opciones:
        print(
            Fore.CYAN
            + "║ "
            + Fore.YELLOW
            + opcion.ljust(ancho_opcion)
            + Fore.CYAN
            + " ║"
        )

    # Imprime la parte inferior del recuadro
    print(Fore.CYAN + "╚" + "═" * (ancho_menu - 3) + "╝")
    print(Fore.RESET)


def ejecutar_opcion(opcion):
    if opcion == "1":
        # Crear recuadro para el ingreso de datos
        ancho_caja = 50  # Ancho fijo del recuadro

        # Encabezado del recuadro
        print(Fore.CYAN + "╔" + "═" * ancho_caja + "╗")
        print(
            "║"
            + " "
            * ((ancho_caja - len(" Ingreso de nuevo producto (0 Para Cancelar) ")) // 2)
            + "Ingreso de nuevo producto (0 Para Cancelar)"
            + " "
            * (
                (ancho_caja - len(" Ingreso de nuevo producto (0 Para Cancelar)") + 5)
                // 2
            )
            + "║"
        )
        print("╚" + "═" * ancho_caja + "╝")

        # Validación para el nombre del producto
        while True:
            nombre = input("Nombre del producto : ").strip()
            if nombre == "0":
                print(
                    Fore.YELLOW + "Operación cancelada. Regresando al menú principal."
                )
                return True  # Devuelve True para continuar al menú principal
            elif nombre:
                break
            else:
                print(
                    Fore.RED
                    + "El nombre del producto no puede estar vacío. Inténtalo de nuevo."
                )

        # Validación para la descripción
        while True:
            descripcion = input("Descripción del producto : ").strip()
            if descripcion == "0":
                print(
                    Fore.YELLOW + "Operación cancelada. Regresando al menú principal."
                )
                return True  # Regresa al menú principal
            elif descripcion:
                break
            else:
                print(
                    Fore.RED
                    + "La descripción del producto no puede estar vacía. Inténtalo de nuevo."
                )

        # Validación para la cantidad
        while True:
            try:
                cantidad = int(input("Cantidad : "))
                if cantidad == 0:
                    print(
                        Fore.YELLOW
                        + "Operación cancelada. Regresando al menú principal."
                    )
                    return True  # Regresa al menú principal
                elif cantidad > 0:
                    break
                else:
                    print(Fore.RED + "La cantidad debe ser un número entero mayor a 0.")
            except ValueError:
                print(Fore.RED + "Por favor, ingresa un número entero válido.")

        # Validación para el precio
        while True:
            try:
                precio = float(input("Precio : "))
                if precio == 0:
                    print(
                        Fore.YELLOW
                        + "Operación cancelada. Regresando al menú principal."
                    )
                    return True  # Regresa al menú principal
                elif precio > 0:
                    break
                else:
                    print(Fore.RED + "El precio debe ser un número positivo mayor a 0.")
            except ValueError:
                print(Fore.RED + "Por favor, ingresa un número decimal válido.")

        # Validación para la categoría
        while True:
            categoria = input("Categoría : ").strip()
            if categoria == "0":
                print(
                    Fore.YELLOW + "Operación cancelada. Regresando al menú principal."
                )
                return True  # Regresa al menú principal
            elif categoria:
                break
            else:
                print(
                    Fore.RED + "La categoría no puede estar vacía. Inténtalo de nuevo."
                )

        # Llamada a la función para agregar el producto
        funciones.agregar_producto(nombre, descripcion, cantidad, precio, categoria)
        print(Fore.GREEN + "Producto agregado exitosamente.")

    elif opcion == "2":
        # funcion para mostrar los productos
        funciones.mostrar_productos()

    elif opcion == "3":
        # Función para cargar los campos para actualizar un producto
        funciones.cargar_campos_para_actualizar()

    elif opcion == "4":
        # Funcion para eliminar un producto
        id_producto = int(input("ID del producto a eliminar: "))
        funciones.eliminar_producto(id_producto)

    elif opcion == "5":
        # Función para buscar un producto
        id_producto = input("Ingrese producto a buscar: ")
        funciones.buscar_producto(id_producto)

    elif opcion == "6":
        # Función para generar el reporte de productos bajo stock
        limite = int(input("Ingrese el límite de stock para bajo stock: "))
        funciones.reporte_bajo_stock(limite)

    elif opcion == "0":
        # Salir de la aplicación
        print(Fore.GREEN + "Gracias por usar Nuestra aplicación." + Fore.RESET)
        return False
    else:
        # Mensaje de opción no válida
        print(Fore.RED + "Opción no válida." + Fore.RESET)

    return True


# Menú principal
def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        continuar = ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
