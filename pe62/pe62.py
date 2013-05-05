def sortnr(n):
    s = list(str(n))
    s.sort()
    return ''.join(s)
import time

t0 = time.time()
d = dict()# init empty dictionary
for i in range(10**5):
    val = i**3 #value of cube
    sn = sortnr(val) #digits in ascending order as string
    if sn in d: #these digits already occured
        if d[sn][0]<4:
            d[sn][0] += 1
        else:
            #fifth occurence of this string
            print('result:',d[sn][1])
            print('len(dict):',len(d))
            break
    else:
        d[sn] = [1, val]

        
print('time', time.time()-t0)
