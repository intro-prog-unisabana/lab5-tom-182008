from utils import flip, count_letters

mensaje_original = input("Please type your message\n")

mensaje_invertido = flip(mensaje_original)

cantidad_aes = count_letters(mensaje_original, "a")

mensaje_codificado = mensaje_invertido + str(cantidad_aes)

print(f"Your encoded message is: {mensaje_codificado}")