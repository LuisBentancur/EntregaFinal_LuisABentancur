import sqlite3


def crear_base_datos():
    # Creo la base de datos inventario.db y la tabla productos.
    # Conectar a la base de datos y se creará si no existe
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Creo la tabla productos si no existe
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
    """
    )

    # confirno los cambios y cierro la conexión
    conn.commit()
    conn.close()

    print("Base de datos 'inventario.db' y tabla 'productos' creadas exitosamente.")


# Llamada a la función para crear la base de datos
crear_base_datos()
