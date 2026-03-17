import os
import math

directorio_actual = os.getcwd()
print(f"Current working directory: {directorio_actual}")

entrada_usuario = input("Enter an integer: ")
numero = int(entrada_usuario)

valor_log = math.log2(numero)
print(f"Log base 2 of {numero} is: {valor_log}")

valor_piso = math.floor(valor_log)
valor_techo = math.ceil(valor_log)

print(f"Floor: {valor_piso}")
print(f"Ceiling: {valor_techo}")