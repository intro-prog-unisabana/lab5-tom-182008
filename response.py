def input_response(secret_value, user_input):
    """
    Compara la entrada con el secreto.
    Retorna: (mensaje_de_texto, es_correcto)
    """
    if user_input < secret_value:
        return "Too low! Try a higher number.", False
    elif user_input > secret_value:
        return "Too high! Try a lower number.", False
    else:
        return "Correct! You guessed the number!", True