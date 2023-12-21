numero = int(input("Ingrese un número entero mayor que cero: "))

if numero > 0:
    print(f"Los divisores de {numero} son:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("Por favor, ingrese un número entero mayor que cero.")
