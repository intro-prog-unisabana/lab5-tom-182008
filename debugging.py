# debugging.py

# Function to get user input
def get_daily_steps():
    """Return list of daily steps."""
    steps = input("Enter your daily steps for 7 days separated by spaces: ")
    step_list = steps.split
    step_list = [int(s) for s in step_list]
    return step_list

# Function to calculate total steps
def total_steps(nums):
    """Return total steps."""
    total = sum(nums)

# Function to calculate average daily steps
def average_steps(total, days=7):
    """Return average steps as int."""
    return total / days

# Function to get maximum steps
def max_steps(nums):
    """Return max steps."""
    max_val = max(nums)
    return maxvalue

# Function to get minimum steps
def min_steps(nums):
    """Return min steps."""
    return min(nums)

# Function to check if each day meets the goal
def goal_check(nums, goal=10000):
    """Return list of booleans for goal."""
    result = []
    for s in nums:
        if s >= goal:
            result.append("True")
        else:
            result.append("False")
    return result

# ----------------------
# Main Program
# ----------------------
step_list = get_daily_steps()

total = total_steps(step_list)
average = average_steps(total)
highest = max_steps(step_list)
lowest = min_steps(step_list)
goal_met = goal_check(step_list)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goal_met)
def analizar_pasos():
    # 1. Entrada y conversión (Error común: olvidar convertir a int)
    entrada = input("Ingresa tus pasos diarios durante 7 días (separados por espacios): ")
    # Usamos una lista de comprensión para convertir cada texto en entero
    pasos = [int(x) for x in entrada.split()]

    # Llamadas a las funciones
    total = calcular_total(pasos)
    promedio = calcular_promedio(pasos)
    maximo = calcular_maximo(pasos)
    minimo = calcular_minimo(pasos)
    metas = verificar_metas(pasos)

    # Impresión del resumen
    print(f"Total steps: {total}")
    print(f"Average daily steps: {promedio}")
    print(f"Highest steps in a day: {maximo}")
    print(f"Lowest steps in a day: {minimo}")
    print(f"Goal met each day: {metas}")

# --- Funciones de Cálculo ---

def calcular_total(lista):
    return sum(lista)

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) // len(lista)

def calcular_maximo(lista):
    return max(lista)

def calcular_minimo(lista):
    return min(lista)

def verificar_metas(lista):
    resultados = []
    for dia in lista:
        if dia >= 10000:
            resultados.append(True)
        else:
            resultados.append(False)
    return resultados

if __name__ == "__main__":
    analizar_pasos()