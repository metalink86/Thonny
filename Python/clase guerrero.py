import random

class Guerrero:
    
     def __init__(self2):
        self2.__ataque=6
        self2.__defensa=5
        self2.__HP=100
        self2.__precision=8
        self2.__velocidad=5
        
     def atacar2(self2):
        
        valor=random.randint(0,10)
        
        daño=self2.__ataque-0.3*self2.__defensa
        
        HP=self2.__HP-daño
        
        if self2.__precision>valor:
            return f'El usuario ha lanzado un ataque. El daño realiza es {daño} y el HP es {HP}'
        else:
            return 'El usuario ha fallado'
        
     def defensar2(self2):
         
        defensar2=self2.__defensa
        
        if(self2.__defensa):
            return 'El usuario ha bloqueado el ataque'
        else:
            return 'El usuario ha recibido el ataque'
        
Aragorn=Guerrero()

print(Aragorn.atacar2())