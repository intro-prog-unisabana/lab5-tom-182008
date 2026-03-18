from utils import *

def main():
    while True:
        # 1. Elegir operación (sin distinción de mayúsculas)
        op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

        if op == "exit":
            break
        
        if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
            print("Invalid option!")
            continue

        # 2. Aceptar entradas
        if op == "absolute":
            n = float(input("Enter the number:\n"))
            # Si el número no tiene decimales significativos, convertir a int para la salida pura
            result = absolute(int(n) if n == int(n) else n)
        else:
            n1 = float(input("Enter the first number:\n"))
            n2 = float(input("Enter the second number:\n"))
            
            # Convertir a int si es posible para mantener la "salida sin procesar" esperada
            val1 = int(n1) if n1 == int(n1) else n1
            val2 = int(n2) if n2 == int(n2) else n2

            # 3. Ejecutar y mostrar
            if op == "add": result = add(val1, val2)
            elif op == "subtract": result = sub(val1, val2)
            elif op == "multiply": result = multiply(val1, val2)
            elif op == "divide": result = divide(val1, val2)
            elif op == "exponent": result = exponent(val1, val2)
            elif op == "modulo": result = modulo(val1, val2)
            elif op == "floor_divide": result = floor_divide(val1, val2)

        if isinstance(result, str):
            print(result) # Imprime el mensaje de error
        else:
            print(f"The result is: {float(result) if op == 'divide' else result}")

if __name__ == "__main__":
    main()