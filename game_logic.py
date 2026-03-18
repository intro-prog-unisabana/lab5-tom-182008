from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

def main():
    seed = int(input("Enter a seed number: "))
    seed_secret_numbers(seed)

    secreto = generate_secret_number()
    
    intentos = 0
    adivinado = False
    
    while not adivinado:
        try:
            user_guess = int(input("What is your guess: "))
            intentos += 1
            
            mensaje, es_correcto = input_response(secreto, user_guess)
            print(mensaje)
            
            if es_correcto:
                adivinado = True
                print(f"It took you {intentos} tries!")
                
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()