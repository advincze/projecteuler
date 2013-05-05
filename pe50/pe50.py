import math, time

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

pp = []
for i in range(1,10000):
    if prime(i):
        pp.append(i)
print('len pp',len(pp))

qq = [[]] * (len(pp)-1)
for i in range(0,len(qq)):
    qq[i] = pp[i] + pp[i+1]
print('len qq',len(qq))

limit = 10**6;
mx = 0;
maxl = 0;
l = 3;
done = False;
while(len(qq)>=2):
    rr = [[]] * (len(qq)-1)
    for i in range(0,len(rr)):
        rr[i] = qq[i] + qq[i+1] - pp[i+1]
        if prime(rr[i]) and rr[i]<=limit:
            mx = rr[i]
            maxl = l;
    if rr[0]>limit:
        break
    l+=1
    pp = qq;
    qq = rr;


print('max',mx)
print('maxl',maxl)
print('time',time.time()-t0)
