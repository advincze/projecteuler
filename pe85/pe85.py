
def countrect(xmax,ymax):
    sm = 0
    for x in range(1,xmax+1):
        for y in range(1,ymax+1):
            sm += (xmax-x+1)*(ymax-y+1)
    return sm
import time
import math
t0 = time.time()
sm = 0

target = int(2e6)
dist = target
area = 0
for xmax in range(1,100):
    for ymax in range(1,100):
        d = math.fabs(countrect(xmax,ymax)-target)
##        print d
        if(d<dist):
            area = xmax*ymax
            dist = d
            print d,area,xmax,ymax

print 'solution:',area


print('time',time.time()-t0)
