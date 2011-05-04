def function(N):
    dic = {}
    for i in range(0,N):
        dic[i] = []
 
    arr = [1]
 
    while(True):
        bol = True
        a = 10**20
        for x in arr:
            dic[x%N].append(x)
        print dic
        if(len(dic[0]) >= 1):
            a = min(a,min(dic[0]))
            bol = False
        if(len(dic[N/2]) >= 1 and N%2 == 0):
           a = min(a,2*min(dic[N/2]))
           bol = False
        for i in range(1,N/2+1):
           if(len(dic[i]) >= 1 and len(dic[N-i]) >= 1):
               a = min(a,(min(dic[i])+min(dic[N-i])))
               bol = False
        if(not bol):
            return a
        temp = []
        for x in arr:
            y1 = int(str(x)+'0')
            y2 = int(str(x)+'1')
            temp += [y1,y2]
        arr = temp
        print arr
 
 
T = 0
 
for n in range(1,101):
    if(n%100 == 0):
        print n,T
    T += function(n)/n
print T
