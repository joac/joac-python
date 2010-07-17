numero = 600851475143

def calcularDivisores(numero):
	lista = [1,]
	a = 1
	while a <= (numero/lista[-1]):
		if numero%a == 0:
			lista.append(a)
		a+=2
	return lista
listado =[]
a = calcularDivisores(numero)
for divisor in a:
	if len(calcularDivisores(divisor)) == 3:
		listado.append(divisor)
	print calcularDivisores(divisor)
print listado
