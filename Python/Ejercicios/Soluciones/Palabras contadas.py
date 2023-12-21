frase_usuario = input("Ingrese una frase: ")
palabras = frase_usuario.split()
clasificacion = {}

for palabra in palabras:
    longitud = len(palabra)
    clasificacion[longitud] = [palabra]

print("Clasificación de palabras por longitud:", clasificacion)