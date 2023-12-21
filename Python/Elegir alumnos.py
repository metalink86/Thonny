import random

alumnos = []

# Solicita el nombre de 20 alumnos
for _ in range(20):
    alumno = input('Introduzca el nombre del alumno: ')
    alumnos.append(alumno)

# Elegir aleatoriamente a los alumnos para cada actividad evaluativa
actividad_evaluativa1 = random.sample(alumnos, k=5)
print("Alumnos seleccionados para Actividad Evaluativa 1:", actividad_evaluativa1)
alumnos = list(set(alumnos) - set(actividad_evaluativa1))

actividad_evaluativa2 = random.sample(alumnos, k=5)
print("Alumnos seleccionados para Actividad Evaluativa 2:", actividad_evaluativa2)
alumnos = list(set(alumnos) - set(actividad_evaluativa2))

actividad_evaluativa3 = random.sample(alumnos, k=5)
print("Alumnos seleccionados para Actividad Evaluativa 3:", actividad_evaluativa3)
alumnos = list(set(alumnos) - set(actividad_evaluativa3))

actividad_evaluativa4 = random.sample(alumnos, k=4)
print("Alumnos seleccionados para Actividad Evaluativa 4:", actividad_evaluativa4)
alumnos = list(set(alumnos) - set(actividad_evaluativa4))
