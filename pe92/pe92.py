ss = {str(i):i*i for i in range(10)}
dd = {1:0,89:1}
        
def ends89(n):
    if n in dd: return dd[n]
    m = sum(ss[i] for i in list(str(n)))
    dd[m] = ends89(m)
    return dd[m]
    
import time
t0 = time.time()

sum89 = 0
for i in range(1,10**7):sum89+=ends89(i)

print('result', sum89)
print('time', time.time()-t0)
