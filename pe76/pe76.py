
dd = dict();

import math

def cc_cache(n,m):
    if n in dd:
        if m in dd[n]:
            return dd[n][m];
    else:
        dd[n] = dict()
    result = 1
    for i in range(m,math.floor(n/2)+1):
        result += cc_cache(n-i, i)
    dd[n][m] = result
    return result

def cc(n, m):
    result = 1
    for i in range(m,math.floor(n/2)+1):
        result += cc(n-i, i)
    return result
        
import time
t0 = time.time()
print(cc_cache(100,1)-1)
print('time', time.time()-t0)

##t0 = time.time()
##print(cc(65,1)-1)
##print('time', time.time()-t0)


