import time
t0 = time.time()
#code here

s = 0
for k in range(0,1000):
    [n,d] = [2,1]
    for i in range(0,k):
        [n,d] = [d+2*n,n]
    [n,d] = [d+n,n]
    if(len(str(n)) > len(str(d))):
        s+=1

print('result',s)

print('time',time.time()-t0)
