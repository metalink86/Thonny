import random

class Mago():
    
    def __init__(self):
        self.__ataque=3
        self.__defensa=4
        self.__HP=100
        self.__precision=7
        self.__velocidad=2
        
    def atacar(self):
    
        atacar=self.__ataque
        
        defensar=self.__defensa
        
        valor=random.randint(0,10)
        
        daño=atacar-0.3*defensar
        
        if self.__precision>valor:
            
            HP=self.__HP-daño
            
            return f'El usuario ha lanzado un ataque.El daño causado es {daño} y el oponente Aragorn dispone de un HP de {HP}'

        else:
            
            return 'El usuario ha fallado'