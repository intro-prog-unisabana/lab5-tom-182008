import random

def seed_secret_numbers(seed):
    """Inicializa el generador con una semilla."""
    random.seed(seed)

def generate_secret_number(start=1, end=100):
    """Retorna un número aleatorio inclusivo."""
    return random.randint(start, end)