import time
t0 = time.time()
sm = 0
for i in range(1,1000):
    sm += i**i
print(str(sm)[-10:])
print('time',time.time()-t0)

