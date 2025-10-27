def operar_conjuntos(lista1, lista2):
    # Convertimos las listas en conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Calculamos las operaciones pedidas
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    # Creamos el diccionario de resultados
    resultado = {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica
    }

    return resultado

# Ejemplo de ejecución
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
print(operar_conjuntos(lista_a, lista_b))
