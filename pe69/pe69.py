import fractions

def relprimes(n):
    #brute force search for relative primes
    rp = [1]
    for i in range(2,n):
        if fractions.gcd(i,n)==1:
            rp.append(i)
    return rp

import time
t0 = time.time();

n = 1
for i in [2,3,5,7,11,13,17,19]:
    m = n*i
    if(m<10**6):
        n = m;

print('result:',n,'time:',time.time()-t0)

phi_n = n / len(relprimes(n))
print('phi(result):', phi_n,'time:',time.time()-t0)

