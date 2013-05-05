import math

def permutate(seq):
    temp = []
    for k in range(len(seq)):
        part = seq[:k] + seq[k+1:]
        for m in permutate(part):
            temp.append(seq[k:k+1] + m)
    return temp

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
#code here
a0 = 1234
sa0 = str(a0)
for a0 in range(1001, 9999):
    if prime(a0):
        pa0 = permutate(str(a0))
        for sa1 in pa0:
            a1 = int(sa1)
            if a1>a0 and prime(a1):
                a2 = 2*a1-a0;
                if (str(a2) in pa0) and prime(a2):
                    print(a0,a1,a2)
 
print('time',time.time()-t0)
