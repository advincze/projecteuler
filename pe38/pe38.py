def pandig9str(snum):
    if(len(snum)!=9):
        return False
    for i in range(1,10):
        if str(i) not in snum:
            return False
    return True
    

import time, math
t0 = time.time()

mx = 0
for i in range(1,100000):
    s = ''
    for j in range(1,10):
        s+=str(i*j)
        if pandig9str(s):
            if(int(s)>mx):
                mx = int(s)
            break
print('result',mx)
    
print('time',time.time()-t0)
