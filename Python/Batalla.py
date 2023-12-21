import random

class Mago():
    
    def __init__(self):
        self.ataque = 3
        self.defensa = 4
        self.vida = 100
        self.precision = 7
        self.velocidad = 2
        
    def atacar(self):
        valor = random.randint(0, 10)
        
        Gandalf_daño = self.ataque - 0.3 * self.defensa
        
        if self.precision > valor:
            self.vida -= Gandalf_daño
            return f'El usuario ha lanzado un ataque. El daño causado es {Gandalf_daño} y el oponente Aragorn dispone de un HP de {self.vida}'
        else:
            return 'El usuario ha fallado'
        
    def obtener_HP(self):
        return f'El HP de Gandalf es {self.vida}'


class Guerrero():
    
    def __init__(self):
        self.__ataque = 6
        self.__defensa = 5
        self.__HP = 100
        self.__precision = 8
        self.__velocidad = 5
        
    def atacar(self):
        valor = random.randint(0, 10)
        
        Aragorn_daño = self.__ataque - 0.3 * self.__defensa
        
        if self.__precision > valor:
            self.__HP -=Aragorn_daño
            return f'El usuario ha lanzado un ataque. El daño realizado es {Aragorn_daño} y el oponente Gandalf dispone de un HP de {self.__HP}'
        else:
            return 'El usuario ha fallado'
        
    def obtener_HP(self):
        return f'El HP de Aragorn es {self.__HP}'

# Crear instancias de las clases
Gandalf = Mago()
Aragorn = Guerrero()

# Loop de batalla hasta que uno de los personajes se quede sin HP
while Gandalf.vida > 0 and Aragorn._Guerrero__HP > 0:
    print(Gandalf.atacar())
    print(Gandalf.obtener_HP())
    
    print(Aragorn.atacar())
    print(Aragorn.obtener_HP())
