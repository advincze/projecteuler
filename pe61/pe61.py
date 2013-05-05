def p(i,n):
    values = {
        3: n*(n+1)/2,
        4: n*n,
        5: n*(3*n-1)/2,
        6: n*(2*n-1),
        7: n*(5*n-3)/2,
        8: n*(3*n-2)
        }
    return values.get(i)

import time

t0 = time.time()
print p(3,15)
print('time',time.time()-t0)
