size = 80

def readdata():
    f = open('matrix.txt','r')
    data = []
    for l in range(0,size):
        data.append([int(s) for s in (f.readline().split(','))])
    f.close()
    return data

def zeros(x,y):
    return [[0 for i in range(0,y)] for j in range(0,x)]

import time
t0 = time.time()
#code here

data = readdata()
for i in range(1,size):
    data[0][i] = data[0][i]+data[0][i-1];
    data[i][0] = data[i][0]+data[i-1][0];

for y in range(1,size):
    for x in range(1,size):
        data[y][x] = min(data[y-1][x],data[y][x-1])+data[y][x];
print('result:',data[size-1][size-1])

print('time',time.time()-t0)
