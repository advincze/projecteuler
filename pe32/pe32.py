def pandig9(s):
    if(len(s)!=9):
        return False
    for i in range(1,10):
        if str(i) not in s:
            return False
    return True

import time
t0 = time.time()
#code here
ppr = []
for i in range(1,999):
    for j in range(1,5000):
        pr = i*j;
        s = ''.join([str(i),str(j),str(pr)]);
        if pandig9(s):
            print(i,j,pr);
            if pr not in ppr:
                ppr.append(pr)

print('sum',sum(ppr))
print('time',time.time()-t0)
