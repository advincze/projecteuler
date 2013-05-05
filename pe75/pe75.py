import time,fractions

t0 = time.time()
lim = 1500000
sqlim = int(lim**.5)

sq = [i*i for i in range(lim)]

sm = [0]*lim
for i in range(1, sqlim,2):
  for j in range(2, sqlim,2):
    if fractions.gcd(i, j) == 1:
        sqi = sq[i]
        sqj = sq[j]        
        a = abs(sqj - sqi)
        b = 2 * i * j
        c = sqj +sqi
        s = a + b + c
        for k in range(s,lim,s):
            sm[k] +=1
            
print(sm.count(1))

print('time',time.time()-t0)
