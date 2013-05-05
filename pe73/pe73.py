import fractions, math

def relprimes(n):
    #brute force search for relative primes
    rp = []
    for i in range(math.floor(n/3+1),math.ceil(n/2-1)+1):
        if fractions.gcd(i,n)==1:
            rp.append(i)
    return rp

import time
t0 = time.time();


i = 0
for d in range(1,12001):
    for n in relprimes(d):
         i+=1
                
print('result:',i)
print('time:',time.time()-t0)

