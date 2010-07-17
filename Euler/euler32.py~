test = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9']
pand = []

for a in range(1, 9999):
    for b in range(1, 9999):
        c =(a * b)
        #print a, b, c
        cadena = str(a)+str(b)+str(c)
        if len(cadena) == 9:
            cadena = [n for n in cadena]
            cadena.sort()
            #print a, b, c, cadena
            if cadena == test:
                pand.append(c)
        elif len(cadena) > 9:
            break
print len(pand)
pand = set(pand)
suma = 0
for a in pand:
    suma += a

print suma


