listaPrimos = [2,3,5,7,11,13, 17, 19]
def esPrimo(numero):
	global listaPrimos
	
	for primo in listaPrimos:
		if numero%primo:
			continue
		else:
			return False
	listaPrimos.append(numero)
	return True
a=21
while len(listaPrimos) < 10001:
	esPrimo(a)
	a += 1
	print len(listaPrimos), a
print listaPrimos[10000]

