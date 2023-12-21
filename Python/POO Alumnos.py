class alumnado():
    
    def __init__(self,nombre,edad,grupo,rama_bachillerato):
        
        self.nombre=nombre
        self.edad=edad
        self.grupo=grupo
        self.rama_bachillerato=rama_bachillerato
        
    def descripcion(self):
        
        print('Nombre:', self.nombre,'\n' 'Edad:', self.edad,'\n' 'Grupo:', self.grupo, '\n' 'Rama de Bachillerato:', self.rama_bachillerato)
        
class nivel_programacion(alumnado):
    
    def __init__(self, nota, motivacion, nombre_alumnado,edad_alumnado,grupo_alumnado,rama_bachillerato):
        
        super().__init__(nombre_alumnado,edad_alumnado,grupo_alumnado,rama_bachillerato)
        self.nota=nota
        self.motivacion=motivacion
    
    def descripcion(self):
        
        super().descripcion()
        
        print('Su nivel de programacion es', self.nota, 'y su nivel de motivación es', self.motivacion)
        
Aina=alumnado('Aina',17,'B','Ciencias')

Aina.descripcion()

print(isinstance(Aina,nivel_programacion))

