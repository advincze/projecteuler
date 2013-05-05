import time
t0 = time.time()
#code here
i = 0
#10**(n)<=9**(n)
limit = 22
for d in range(1,limit):
    for n in range(1,10):
        if d==len(str(n**d)):
            i+=1;
print(i)

print('time',time.time()-t0)
