
def esDivisible(numero):
	for numero in range(1, 21):
		if a%numero:
			return False
	else: return True

a = 20
while True:
	if esDivisible(a):	
		print a
		break
  	a += 10


