import time
t0 = time.time()

ff = [2]
for i in range(1,34):
    ff.append(1)
    ff.append(i*2)
    ff.append(1)
ff.reverse()
print(ff)

[n,d] = [ff[0],1]
##print(n,d,n/d)
for f in ff[1:]:
    [n,d] = [d+f*n,n]
##    print(n,d,n/d)


print(n,d,n/d,(n/d)**2)
print('result', sum([int(i) for i in list(str(n))]))

print('time', time.time()-t0)
