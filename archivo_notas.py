# Autor: Johao Flores
# Tarea: Trabajo con Archivos de Texto
# Descripción: Escritura, lectura y cierre de archivos de texto en Python.

# ----------------------------
# 1. Escritura de un archivo
# ----------------------------
# Creamos (o sobrescribimos si ya existe) el archivo 'my_notes.txt'
# y escribimos en él al menos tres notas personales.

with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Hoy aprendí a trabajar con archivos en Python.\n")
    file.write("Nota 2: Me gusta aprender programación paso a paso.\n")
    file.write("Nota 3: Recordar siempre cerrar los archivos después de usarlos.\n")

# El uso de 'with open' se encarga de cerrar el archivo automáticamente.

# ----------------------------
# 2. Lectura de un archivo
# ----------------------------
# Abrimos el archivo en modo lectura y mostramos su contenido línea por línea.

with open("my_notes.txt", "r") as file:
    # Recorremos línea por línea
    for linea in file:
        print(linea.strip())  # strip() elimina saltos de línea extras

# Nuevamente, 'with open' asegura que el archivo se cierre al terminar.
