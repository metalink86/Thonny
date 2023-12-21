import math
def area_circulo(radio):
    return (math.pi*radio**2)

def volumen_circulo(radio,altura):
    return area_circulo(radio)*altura

area_circulo(5)

volumen_circulo(5,10)