def pe44():
    pent = set( int(n * (3*n - 1) / 2) for n in range(1,3000))
    for i in pent:
        for k in pent:
            if k+i  in pent and k-i in pent:
                return k-i

import time
t0 = time.time()
#code here
print(pe44())


            
print('time',time.time()-t0)
