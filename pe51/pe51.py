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

def pe51():
    for i in range(3,10**6,2):
        if prime(i):
            si = str(i)
            for dig in set(si):
                pr = []
                for dig2 in range(10):
                    i2 = int(si.replace(dig,str(dig2)))
                    # replacing by 0 at the first position is now allowed
                    # thus compare length
                    if prime(i2) and len(str(i2))==len(si): 
                        pr.append(i2)
                if len(pr)==8:
                    return i

import time
t0 = time.time()

print('result',pe51())

print('time', time.time()-t0)
