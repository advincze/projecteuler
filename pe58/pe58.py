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


    



def pe58():
    total = 1;
    pr = 0;
    i = 1
    step = 2
    ratio = 1
    while True:
        for k in range(4):
            i += step
            if prime(i):
                pr +=1
            total+=1
        ratio = float(pr)/total
        if ratio<0.1:
            return step +1
        step +=2


import time

t0 = time.time()
print pe58()
print('time',time.time()-t0)
