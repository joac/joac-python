file = open('matrix.txt', 'r')
contenido = file.readlines()
file.close()
matriz = []
for lista in contenido:
	matriz.append([int(a) for a in lista.split()])
	
print matriz

sumas = []

def sumasHorizontales(matriz):
	global sumas
	for y in xrange(0, len(matriz)):
		for x in xrange(0, len(matriz[y])-3):
			numero = 1
			for n in xrange(0, 4):
				numero *=matriz[y][x+n]
			sumas.append(numero)			
def sumasVerticales(matriz):
	global sumas
	for y in xrange(0, len(matriz)-3):
		for x in xrange(0, len(matriz[y])):
			numero = 1
			for n in xrange(0, 4):
				numero *=matriz[y+n][x]
			sumas.append(numero)
def sumas135(matriz):
	global sumas
	for y in xrange(0, len(matriz)-3):
		for x in xrange(0, len(matriz[y])-3):
			numero = 1
			for n in xrange(0, 4):
				numero *=matriz[y+n][x+n]
			sumas.append(numero)
def sumas45(matriz):
	global sumas
	for y in xrange(3, len(matriz)):
		for x in xrange(0, len(matriz[y])-3):
			numero = 1
			for n in xrange(0, 4):
				numero *=matriz[y-n][x+n]
			sumas.append(numero)
			
if __name__ == "__main__":
	sumasHorizontales(matriz)
	print sumas
	sumasVerticales(matriz)
	print sumas
	sumas135(matriz)
	print sumas
	sumas45(matriz)
	print sumas
	print 'el largo de la lista es de %d' %len(sumas)
	
	conjunto = set(sumas)
	print 'el largo compactado es de %d' %len(conjunto)
	sumas.sort()
	print 'el mas grande es %d' % sumas[-1]
	
