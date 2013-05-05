

import time
t0 = time.time()

mx = int(5e7)

n = [1]*mx
pr = []
for i in range(2,mx):
    if not n[i]==1:
        continue
    pr.append(i)
    for j in range(i,mx,i):
        n[j] +=1


print('time',time.time()-t0)
mx2 = int(1e8)
sm = 0
for p in pr:
    for q in pr:
        if q>p:break
        if p*q<mx2:
            sm +=1
        else: break

print sm

print('time',time.time()-t0)
