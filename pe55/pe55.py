import math

def pal(s):
    for i in range(math.floor(len(s)/2)):
        if s[i] != s[-i-1]:
            return False
    return True

def lycrel(num, it):
    if(it>50):
        return True
    rev = int(str(num)[::-1])
    sm = rev+num
    if pal(str(sm)):
        return False
    else:
        return lycrel(sm,it+1)

import time
t0 = time.time()
#code here

sm = 0;
for i in range(10000):
    if lycrel(i,1):
        sm += 1
        
print('sum',sm)
print('time',time.time()-t0)
