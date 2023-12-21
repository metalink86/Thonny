estudiantes = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'fin' para salir): ")

    if nombre.lower() == 'fin':
        break

    notas = [float(nota) for nota in input(f"Ingrese las notas de {nombre} separadas por espacios: ").split()]
    promedio = sum(notas) / len(notas)

    estudiantes[nombre] = {'notas': notas, 'promedio': promedio}
print(estudiantes)
# Mostrar el promedio de notas
print("Promedio de Notas:")
for nombre, datos in estudiantes.items():
    print(f"{nombre}: {datos['promedio']}")