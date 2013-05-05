import time
t0 = time.time()

import math
mx = [1,3,1/3]
for d in range(2,10**6+1):
    n = math.ceil(3*d/7-1)
    val = n/d
    if val>mx[2]:
        mx = [n,d,val]
print('result',mx[0])
print('time', time.time()-t0)
