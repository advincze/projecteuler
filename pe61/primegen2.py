import math

primes = [2,3]

def testpr(num, lim):
    for i in primes:
        if i>lim:
            return True
        if num%i==0:
            return False
    return True

import time
t0 = time.time()

for num in range(5,10**6,2):
    nsq = math.sqrt(num)
    if testpr(num, nsq):
        primes.append(num)
       
print(len(primes))

print('time',time.time()-t0)
