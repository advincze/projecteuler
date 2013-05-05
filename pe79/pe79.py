import time, array, operator
t0 = time.time()

f = open('keylog.txt','r')

a = []
for i in range(10):
     a.append([])
     for j in range(10):
         a[i].append(0)
     
for line in f:
    i0 = int(line[0])
    i1 = int(line[1])
    i2 = int(line[2])
    a[i0][i1] = 1
    a[i1][i2] = 1
    a[i0][i2] = 1


fr = [0]*10
to = [0]*10
for i in range(10):
     for j in range(10):
          fr[i] += a[i][j]
          to[j] += a[i][j]

tt = [[i, to[i]] if (fr[i]>0 or to[i]>0) else ['',0] for i in range(10)]
tt.sort(key=operator.itemgetter(1))

tt2 = [str(tt[i][0]) for i in range(10)]
print(''.join(tt2))

f.close()

print('time',time.time()-t0)
