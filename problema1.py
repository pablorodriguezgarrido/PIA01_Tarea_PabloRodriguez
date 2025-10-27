def procesar_lista(numeros):
    # 1. Eliminar negativos
    numeros = [n for n in numeros if n >= 0]
    # 2. Eliminar duplicados
    numeros = list(set(numeros))
    # 3. Ordenar de menor a mayor
    numeros.sort()
    return numeros

# Ejemplo de ejecución
print(procesar_lista([4, -1, 2, 4, 3, -5, 2]))
