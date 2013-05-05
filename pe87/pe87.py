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
    nsq = num**.5
    if testpr(num, nsq):
        primes.append(num)


pr2 = [i*i for i in primes]
pr3 = [i*i*i for i in primes]
pr4 = [i*i*i*i for i in primes]


mx = int(5e7)
sms = set()
for p2 in pr2:
    if p2>=mx: break
    for p3 in pr3:
        s2 = p2 +p3
        if s2>=mx: break
        for p4 in pr4:
            s3 = s2+ p4
            if s3>=mx:  break
            sms.add(s3)
print(len(sms))

print('time',time.time()-t0)
