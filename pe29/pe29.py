import time
t0 = time.time()
l = []
for a in range(2,101):
    for b in range(2,101):
        n = a**b;
        if n not in l:
            l.append(n)
print('l',len(l))
print('time',time.time()-t0)
