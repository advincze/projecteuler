import time
t0 = time.time()
#code here          
#28433 * 2**7830457+1.
k = 2;
for i in range(1,7830457):
    k = (k*2)%(10**10)
k = (k*28433)%(10**10)
k += 1
print('k',k)
print('time',time.time()-t0)
