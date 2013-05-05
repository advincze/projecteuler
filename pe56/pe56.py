def sumdig(num):
    s = 0
    for i in str(num):
        s += int(i)
    return s

import time
t0 = time.time()
#code here          

mxsm = 0;
for a in range(1,101):
    for b in range(1,101):
        tmp = sumdig(a**b);
        if tmp>mxsm:
            mxsm = tmp
print(mxsm)
print('time',time.time()-t0)
