ss = [2,3,5,7,11,13,17]
def prop(s):
    for i in range(7):
        if int(s[1+i:4+i])%ss[i]!=0:
            return False
    return True

import time
t0 = time.time()

l17= []
for i in range(17,999,17):
    if i>9 and i<100: l17.append('0'+str(i))
    elif i>=100: l17.append(str(i))
l7 = []
for i in range(7,999,7):
    if i>9 and i<100: l7.append('0'+str(i))
    elif i>=100: l7.append(str(i))
l2 = []
for i in range(2,999,2):
    if i>9 and i<100: l2.append('0'+str(i))
    elif i>=100: l2.append(str(i))

sm = 0
for i17 in l17:
    for i7 in l7:
        for i2 in l2:
            for i in range(1,10):
                s= str(i)+i2+i7+i17
                if len(set(s))==10 and prop(s): sm+=int(s)
                        
print('result',sm)
print('time', time.time()-t0)
