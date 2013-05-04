import math

def prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    if(num%2==0):
        return False
    limit = math.floor(math.sqrt(num))
    i = 3
    while i<=limit:
        if num%i==0:
            return False
        i+=2
    return True

import time
t0 = time.time()

sm = 0;
for num in range(10,1000000):
    if prime(num):
        snum = str(num)
        pr = True
        for i in range(1,len(snum)):
            if ( not prime(int(snum[:-i])) ) or ( not prime(int(snum[i:])) ):
                pr = False
                break
        if(pr):
            sm += num
print('sum',sm)
print('time',time.time()-t0)
