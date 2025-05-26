import os
import shutil

def organizar_descargas():
  carpeta_descargas = os.path.join(os.path.expanduser("~", "Downloads")
  subcarpetas = {
      "Documentos": [".pdf", ".docs", ".xlsx",".xls", ".txt"]
      "Imagenes": [".jpg", ".jpeg"]
  
  }

for archivo in os.listdir(carpeta_descargas):
    ruta_archivo = os.path.join(carpeta_descargas, archivo)

    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        movido = False

        for subcarpeta, extensiones in subcarpetas.items():
            if extension in extensiones:
                carpeta_destino = os.path.join(carpeta_descargas, subcarpeta)
                os.makedirs(carpeta_destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                movido = True
                break
              
        if not movido:
            carpeta_destino = os.path.join(carpeta_descargas, "Otros")
            os.makedirs(carpeta_destino, exist_ok=True)
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))

if __name__ == "__main__":
    organizar_descargas()
