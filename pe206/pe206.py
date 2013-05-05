import time
t0 = time.time()

import re, math
prog = re.compile("1.2.3.4.5.6.7.8.9")# last 2 digits are 00

lower = math.ceil(math.sqrt(10203040506070809))
upper = math.ceil(math.sqrt(19293949596979899))
print(upper, lower, upper-lower)
for i in range(lower, upper):
    if prog.match(str(i*i)):
        print('result',i*10)
        break



print('time', time.time()-t0)
