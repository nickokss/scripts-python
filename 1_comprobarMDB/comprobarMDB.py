import os
import pyodbc

# Ruta donde buscar archivos .mdb
ruta_busqueda = "ruta_completa"
# Nombre de la columna que buscas
nombre_columna_busqueda = "columna_a_buscar"

# Lista todos los archivos .mdb en la ruta especificada
archivos_mdb = [f for f in os.listdir(ruta_busqueda) if f.endswith('.mdb')]

# Función para conectar a la base de datos y verificar la existencia de la columna
def verificar_columna_en_bd(ruta_bd, nombre_columna):
    cadena_conexion = f'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={ruta_bd}'
    conexion = None
    cursor = None
    try:
        conexion = pyodbc.connect(cadena_conexion)
        cursor = conexion.cursor()

        # Recorre todas las tablas y verifica si contienen la columna buscada
        for tabla in cursor.tables(tableType='TABLE'):
            columnas = [columna.column_name for columna in cursor.columns(table=tabla.table_name)]
            if nombre_columna in columnas:
                print(f"La columna '{nombre_columna}' se encontró en la tabla '{tabla.table_name}' del archivo '{ruta_bd}'")
    except Exception as e:
        print(f"Error {ruta_bd}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()

for archivo_mdb in archivos_mdb:
    ruta_completa = os.path.join(ruta_busqueda, archivo_mdb)
    print(f"{ruta_completa}")
    verificar_columna_en_bd(ruta_completa, nombre_columna_busqueda)