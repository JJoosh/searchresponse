import signal
import sys
import re

def salir_con_ctrl_c(sig, frame):
    print("\nSaliendo...")
    sys.exit(0)


signal.signal(signal.SIGINT, salir_con_ctrl_c)

print("Este script está diseñado para procesar archivos de texto (.txt)")
print("Asegúrate de proporcionar la ruta de un archivo de texto válido.\n")
print("Created by Josh..................................................\n")


archivo = input("Por favor, ingresa la ruta del archivo: ")

try:
    with open(archivo, "r", encoding="utf-8") as f:

        for linea in f:
            matches = re.findall(r'"keyword\\":\\"([^"]+)', linea)
            for match in matches:
                keyword = match.replace("\\", "")
                respuesta_correcta = 'S' + keyword[1:]
                
                print(f"Respuesta correcta: {respuesta_correcta}")

except FileNotFoundError:
    print("El archivo especificado no fue encontrado.")
