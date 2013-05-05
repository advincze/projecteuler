import math
import fractions

def prime(num,pp):
    limit = math.floor(math.sqrt(num))
    i = 3
    for p in pp:
        if p>limit: break
        if num%p==0: return False
    return True

import time

t0 = time.time()

mx = int(1e7)+1
pp = [2]
for i in range(3,mx,2):
    if prime(i,pp): pp.append(i)
##print('primes time',time.time()-t0)

phi = [0]
phi.extend(range(0,mx))
for p in pp:
    phi[p] = p-1
    k = p
    while k < mx:
        phi[k] -= phi[k]/p
        k += p
mn = 100;
mi = -1;
for i in range(2,len(phi)):
    si = str(i)
    spi = str(phi[i])
    if len(si)==len(spi):
       lsi = list(si)
       lsi.sort()
       lspi = list(spi)
       lspi.sort()
       if(lsi==lspi):
           r = float(i)/float(phi[i])
           if(r<mn):
               mn = r
               mi = i
##               print(i,phi[i],si,spi,lsi,lspi,r)
print mi
print('time',time.time()-t0)
