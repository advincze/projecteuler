def val(l):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(l)+1;

import time
t0 = time.time()
f = open('words.txt','r')
words = f.readline().replace('"','').split(',')
f.close()
mxl = max([len(w) for w in words ]) # max length of word
mxv = mxl*val('Z'); # max value for a word
tt = []
i,t = 1,1;
while(t<=mxv):
    tt.append(t)   
    i += 1
    t += i

sm = 0;
for w in words:
    wval = sum([val(l) for l in w])
    if wval in tt:
        sm +=1
print('sum',sm)
print('time',time.time()-t0)
