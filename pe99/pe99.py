import time
t0 = time.time();
import math
f = open('base_exp.txt','r')
mxval = -1
n = 0
for line in f:
    n+=1
    [base, exp] = line.split(',')
    val = int(exp)*math.log(int(base))
    if val > mxval:
        mxval = val
        mxline = n
f.close()
print('result:',mxline)
print('time:',time.time()-t0)

