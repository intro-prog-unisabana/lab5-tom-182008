def promedio_estudiante(calificaciones):

    if len(calificaciones) == 0:
        return 0.0
    
    suma_total = sum(calificaciones)
    resultado = suma_total / len(calificaciones)
    
    return float(resultado)