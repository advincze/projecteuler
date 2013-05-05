import math
ss = { str(x): math.factorial(x) for x in range(10)}

def sumfact(n):
    return sum([ss[i] for i in list(str(n))])

@cache
def chain(n,used):
    if n in used:
        return len(used)
    else:
        used.append(n)
        m = sumfact(n)
        result = chain(m,used)
        return result
        

import time
t0 = time.time()

print('145',chain(145,[]))
print('169',chain(169,[]))
print('69',chain(69,[]))
print('78',chain(78,[]))
print('540',chain(540,[]))
c60 = 0
for start in range(1,10**6):
    if(chain(start,[])==60): c60+=1
print('result',c60)
    
print('time', time.time()-t0)
