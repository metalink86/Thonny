estudiantes={}

while True:
    a=input('Introduza el nombre del estudiante o fin si desea acabar:')
    if a=='fin':
          break
    b=input('Introduza la nota en Programación:')
    
    estudiantes[a]={'nota':b}
   
       
print(estudiantes)