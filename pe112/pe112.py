def bouncy(n):
    s = str(n)
    inc,dec = False, False
    for i in range(1,len(s)):
        if s[i-1]>s[i]:
            if(dec): return True
            inc = True
        elif s[i-1]<s[i]:
            if(inc): return True
            dec = True
    return False

import time
t0 = time.time()

b = 0
for i in range(1,10**8):
    if bouncy(i):
        b+=1
    if(b/i>=0.99):
        print('result',i)
        break
print('time', time.time()-t0)
