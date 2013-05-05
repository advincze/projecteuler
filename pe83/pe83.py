import copy
import time

def printm(name, m):
    print(name,'[')
    for line in m:
        print line
    print(']')
t0 = time.time()


f = open('matrix.txt','r')
m = []
while True:
    line = f.readline()
    if len(line)==0: break
    l = []
    for i in line.split(','):
        l.append(int(i))
    m.append(l)
f.close()
ml = len(m)
mx = ml-1
##printm('m',m)


m2 = [[]]

m2[0].append(m[0][0])
m3 = [[]]
m3[0].append(0)
upd = []

for i in range(1,len(m[0])):
    m2[0].append(m2[0][i-1]+m[0][i])
    m3[0].append(m2[0][i-1])
    upd.append([0,i])
for i in range(1,len(m)):
    m2.append([m2[i-1][0]+m[i][0]])
    m3.append([m2[i-1][0]])
    upd.append([i,0])
    for j in range(1,len(m[i])):
        m2[i].append(m2[i][j-1]+m[i][j])
        m3[i].append(m2[i][j-1])
        upd.append([i,j]) 


##printm('m2',m2)
##printm('m3',m3)
##printm('upd',upd)

k = 0

while len(upd)>0:
    [i,j] = upd.pop(0)
##    print('i,j',i,j)
##    printm('m2',m2)
##    printm('m3',m3)
##    printm('upd',upd)
    nn = []
    nnc = []
    if j>0:
        left = m2[i][j-1]
        nn.append(left)
        nnc.append([i,j-1])
    if j<len(m[0])-1:
        right = m2[i][j+1]
        nn.append(right)
        nnc.append([i,j+1])
    if i>0:
        top = m2[i-1][j]
        nn.append(top)
        nnc.append([i-1,j])
    if i<len(m)-1:
        bot = m2[i+1][j]
        nn.append(bot)
        nnc.append([i+1,j])
        
##    print('neighbors',nn)
    minn = min(nn)
##    print('min neighbor',minn)
    if minn<m3[i][j]:
##        print('i,j not min')
        m2[i][j] = m2[i][j] - (m3[i][j]-minn)
        m3[i][j] = minn
        for c in nnc:
            upd.append(c)
##    k +=1
##    if k==6:
##        break
        
##printm('m2',m2)
##printm('m3',m3)

print('solution',m2[mx][mx])


print('time',time.time()-t0)
