import math, time, itertools

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

t0 = time.time()

mx = 0;
for n in range(1,9):
    snum = ''.join([str(i) for i in range(1,n+1)])
    for num in itertools.permutations(snum):
        if prime(int(''.join(num))):
            mx = int(''.join(num));
print('max',mx)
print('time',time.time()-t0)
