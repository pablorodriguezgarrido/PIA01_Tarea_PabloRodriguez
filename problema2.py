def contar_palabras(frase):
    # Convertir la frase a minúsculas
    frase = frase.lower()
    # Separar por espacios y eliminar signos de puntuación simples
    for signo in [".", ",", ";", ":", "!", "?"]:
        frase = frase.replace(signo, "")
    palabras = frase.split()
    # Contar las palabras con un diccionario
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# Ejemplo de ejecución
texto = "Hola mundo, hola inteligencia artificial. Hola de nuevo!"
print(contar_palabras(texto))
