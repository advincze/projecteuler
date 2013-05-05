import time
t0 = time.time()
#rounds = 4  ->11/120
#rounds = 15 ->??


a = dict()
a[1,0] = 1 #(count blue, count red)-> count combnation
a[0,1] = 1

b = 1
r = 1
rounds = 15

for i in range(1,rounds):
    r +=1
    # round begin
    #print(i, a)
    olda = a.copy();
    a = dict()
    for el in olda:        
        if (el[0]+1,el[1]) in a:
            a[el[0]+1,el[1]] += olda[el]*b
        else:
            a[el[0]+1,el[1]] = olda[el]*b
        if (el[0],el[1]+1) in a:
            a[el[0],el[1]+1] += olda[el]*r
        else:
            a[el[0],el[1]+1] = olda[el]*r
    # round end
    
    
#print(a)
import math
bw = 0 #blue wins
total = 0
for el in a:
    if el[0]>el[1]:
        bw += a[el]
    total += a[el]
    
print('the answer is', math.floor(total/bw))
print('time', time.time()-t0)
