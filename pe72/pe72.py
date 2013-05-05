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

mx = int(1e6)+1
pp = [2]
for i in range(3,mx,2):
    if prime(i,pp): pp.append(i)

phi = [0,0]
phi.extend(range(1,mx))
for p in pp:
    phi[p] = p-1
    k = p
    while k < mx:
        phi[k] -= phi[k]/p
        k += p
        
print sum(phi[:mx])
print('time',time.time()-t0)
