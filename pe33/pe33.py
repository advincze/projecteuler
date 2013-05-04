import time
t0 = time.time()
for i1 in range(11,100):
    for i2 in range(11,100):
        a = int(str(i1)[0])
        b = int(str(i1)[1])
        c = int(str(i2)[0])
        d = int(str(i2)[1])
        if a==d and c!=d and c!=0 and i1/i2==b/c and i1>i2:
            print(i1,i2,'-',b,c,i1/i2)
        elif b==c and (a!=d) and d!=0 and i1/i2==a/d and i1>i2:
            print(i1,i2,'-',a,d,i1/i2)
            

print('time',time.time()-t0)
