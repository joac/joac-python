import time

n = 0
dec = False
while True:
#    print " "*n +"^fg(#FF0000)Hola Mundo^c(%d)" %(n*n)
    print "mama ^ib(1)^p(10)^fg(#aecf96)^c(10)^p(-15)^fg(grey40)^co(20-%d)" %n
    n += 3 
    if n == 360:
       n = 0 

    time.sleep(0.5)

