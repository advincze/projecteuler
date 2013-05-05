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


for num in range(5,int(5e7),2):
    nsq = num**.5
    if testpr(num, nsq):
        primes.append(num)

print len(primes)
print('time',time.time()-t0)
mx = int(1e8)
sm = 0
for p in primes:
    for q in primes:
        if q>p:break
        if p*q<mx:
##            print p,q,p*q
            sm +=1
        
        else: break

print sm

print('time',time.time()-t0)
