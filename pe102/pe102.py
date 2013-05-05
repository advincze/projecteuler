def intersect(p1,p2,p3,p4):
    dx13 = p1[0]-p3[0]
    dx43 = p4[0]-p3[0]
    dx21 = p2[0]-p1[0]
    dy13 = p1[1]-p3[1]
    dy43 = p4[1]-p3[1]
    dy21 = p2[1]-p1[1]
    
    d = dy43*dx21 - dx43*dy21
    if(d==0):
        return False
    ua = (dx43*dy13 - dy43*dx13)/d
    ub = (dx21*dy13-dy21*dx13)/d
    if ua>=0 and ua<=1 and ub>=0 and ub<=1:
        #x = p1[0]+ua*(p2[0]-p1[0])
        #y = p1[1]+ua*(p2[1]-p1[1])
        return True
    else:
        return False

def zeroinside(a,b,c):
    s = 0
    if intersect(a,b,[0,0],[2000,0]): s+=1
    if intersect(b,c,[0,0],[2000,0]): s+=1
    if intersect(c,a,[0,0],[2000,0]): s+=1
    if s%2==1:
        return True
    else:
        return False

import time
t0 = time.time()
#code here

f = open('triangles.txt','r')
s = 0
for line in f:
    ll = line.split(',')
    if zeroinside([int(ll[0]), int(ll[1])],[int(ll[2]),int(ll[3])],[int(ll[4]),int(ll[5])]):
        s+=1
f.close()

print('result',s)
print('time',time.time()-t0)
