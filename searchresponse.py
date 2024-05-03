print("Este script está diseñado para procesar archivos de texto (.txt)")
print("Asegúrate de proporcionar la ruta de un archivo de texto válido.\n")
print("Created by Josh..................................................\n")
import re

# Solicitar al usuario la ubicación del archivo
archivo = input("Por favor, ingresa la ruta del archivo: ")

with open(archivo, "r", encoding="utf-8") as f:
    # Leer cada línea del archivo
    for linea in f:
        # Buscar la palabra clave y la respuesta correcta en la línea
        matches = re.findall(r'"keyword\\":\\"([^"]+)', linea)
        for match in matches:
            # Eliminar las barras invertidas y convertir a formato correcto
            keyword = match.replace("\\", "")
            respuesta_correcta = 'S' + keyword[1:]
            
            # Imprimir la palabra clave y la respuesta correcta
            print(f"Respuesta correcta: {respuesta_correcta}")
