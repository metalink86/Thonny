a={'Euro':'€','Dollar':'$','Yen':'¥'}
b=input('Introduzca una divisa:')
if b in a:
    print(a[b])
else:
    print('La divisa no está')