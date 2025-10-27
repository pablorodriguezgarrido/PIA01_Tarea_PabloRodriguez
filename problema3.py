def calcular_media(datos):
    if not datos:
        return 0
    # Calcular la media aritmética de una lista de números
    return sum(datos) / len(datos)

def calcular_maximo(datos):
    if not datos:
        return None
    return max(datos)

def calcular_minimo(datos):
    if not datos:
        return None
    return min(datos)

# Ejemplo de ejecución
numeros = [5, 8, 2, 10, 3]
print("Media:", calcular_media(numeros))
print("Máximo:", calcular_maximo(numeros))
print("Mínimo:", calcular_minimo(numeros))
