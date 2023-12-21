#Creación del diccionario de tareas
tareas_pendientes={}
i=True
while i:
    asignatura=input('Introduce la asignatura o escribe salir para acabar: ')
    if asignatura=='salir':
        break
    deberes=input('Introduce los deberes: ')
    tareas_pendientes[asignatura]=deberes
#Modificar las tareas
tareas_hoy=input('¿Deseas ver las tareas del día?:')
if tareas_hoy.lower()=='si':
    for i in tareas_pendientes:
        print(f'En la asignatura {i}, tienes pendiente {tareas_pendientes[i]}')
        completada=input('¿Has realizado la tarea?: ')
        if completada.lower()=='si':
            tareas_pendientes[i]='Completada'
        else:
          continue
#Mostrar el diccionario actualizado
    for j in tareas_pendientes:
        if tareas_pendientes[j]=='Completada':
            print(f'En la asignatura {j}, no tienes nada pendiente')
        else:
            print(f'En la asignatura {j}, tienes pendiente {tareas_pendientes[j]}')
else:
    print('!Que tengas un buen día¡')
       
