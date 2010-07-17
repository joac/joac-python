lista = [1, 2]

def sumatoriaPar(lista):
	a = 0
	for numero in lista:
		if not numero%2:
			a += numero
	return a
	
while lista[-1] <= 4000000:
	lista.append(lista[-2] + lista[-1])

print sumatoriaPar(lista)
		
