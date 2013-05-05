import time
t0 = time.time()

sp = [0]*37
sc = [0]*37

for i1 in range(1,5):
    for i2 in range(1,5):
        for i3 in range(1,5):
            for i4 in range(1,5):
                for i5 in range(1,5):
                    for i6 in range(1,5):
                        for i7 in range(1,5):
                            for i8 in range(1,5):
                                for i9 in range(1,5):
                                    s = i1+i2+i3+i4+i5+i6+i7+i8+i9
                                    sp[s] +=1
                                    

for i1 in range(1,7):
    for i2 in range(1,7):
        for i3 in range(1,7):
            for i4 in range(1,7):
                for i5 in range(1,7):
                    for i6 in range(1,7):
                        s = i1+i2+i3+i4+i5+i6
                        sc[s] +=1
    
print(sp)
print(sc)

pw = 0
nw = 0
cw = 0
t = 0
for i in range(len(sp)):
    for j in range(len(sc)):
        p = sp[i]
        c= sc[j]
        t += p*c
        if i>j:
            pw += p*c
        elif i==j:
            nw += p*c
        elif i<j:
            cw += p*c

print(pw)
print(nw)
print(cw)
print(t)

print(pw/t)
print('time', time.time()-t0)
