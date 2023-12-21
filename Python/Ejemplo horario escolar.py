# Definir los horarios y asignaturas
horarios_dia = ['08:00', '08:55', '09:50', '11:15', '12:10', '13:05']
asignaturas = ['Castellano', 'Matemáticas', 'Historia', 'Filosofía', 'Catalán', 'Inglés']

# Solicitar al usuario el día de la semana
dia = input("Ingresa el día de la semana (lunes, martes, miércoles, jueves, viernes): ").lower()

# Verificar si el día ingresado es válido
if dia not in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']:
    print("Día no válido.")
else:
    # Solicitar al usuario la hora de inicio de la clase
    hora_inicio = input("Ingresa la hora de inicio de la clase (en formato HH:MM): ")

    # Verificar si la hora ingresada es válida
    if hora_inicio not in horarios_dia:
        print("Hora no válida.")
    else:
        # Encontrar la asignatura correspondiente al día y hora ingresados
        indice_horario = horarios_dia.index(hora_inicio)
        asignatura = asignaturas[indice_horario]

        # Mostrar la asignatura
        print(f"La asignatura para el día {dia} a las {hora_inicio} es: {asignatura}")
