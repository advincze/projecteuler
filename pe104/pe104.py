def pandig9(s):
    if(len(s)!=9):
        return False
    for i in range(1,10):
        if str(i) not in s:
            return False
    return True

def pd(n):
    dd = [0]*10
    for i in range(9):
      d = n%10
      if d==0:
          return False;
      if dd[d]==1:
          return False;
      dd[d] = 1
      n = n/10
    return True
    


import time;
t0 = time.time()
k = 2
f1 = 1
f2 = 1
fk = 2
for k in range(3,1000000):
    fk = f1+f2
    f1 = f2
    f2 = fk    
    if pd(fk%(10**9)):
        sfk = str(fk)
        if pandig9(sfk[:9]):
            print k
 

print("time",time.time()-t0)
