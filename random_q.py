import random
random.seed(123)

inicio = int(input("Enter the start value:\n"))
fin = int(input("Enter the end value:\n"))

numero_aleatorio = random.randint(inicio, fin)

print(f"Generated random number: {numero_aleatorio}")