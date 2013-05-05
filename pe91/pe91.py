

import time
t0 = time.time()

mx = 51
sm = 0
for x1 in range(mx):
    for y1 in range(mx):
        l1sq = (x1*x1+y1*y1)
##        l1 = l1sq**.5
        if x1==y1==0:
            continue
        for x2 in range(mx):
            for y2 in range(mx):
                l2sq = (x2*x2+y2*y2)
##                l2 = l2sq**.5
                l12sq = ((x2-x1)**2+(y2-y1)**2)
##                l12 = l12sq**.5
                
                if x2==y2==0:
##                    print '1.',x1,y1,x2,y2
                    continue
                if x1==x2==0 or y1==y2==0:
##                    print '2.',x1,y1,x2,y2
                    continue
                if (x1==x2 and y1==y2):
##                    print '3.',x1,y1,x2,y2
                    continue
                if l1sq +l2sq == l12sq or l1sq+l12sq == l2sq or l2sq+l12sq==l1sq:
##                    print 'XXXX',x1,y1,x2,y2
                    sm += 1
##                else:
##                    print '4.',x1,y1,x2,y2,l1sq,l2sq,l12sq

print sm/2

print('time',time.time()-t0)
