import copy

def check(values):
    c = [0]*10
    for i in values:
        c[i] +=1
##    print('check',values,c[1:])
    for i in c[1:]:
        if i > 1:
            return False
    return True

def checkall(sc,row, col):
    if not check(sc[row]): return False
    cols = []
    for r in sc:
        cols.append(r[col])
    if not check(cols): return False
    sqs = []
    rcell = row-row%3
    ccell = col-col%3
    for r in range(rcell,rcell+3):
        for c in range(ccell,ccell+3):
            sqs.append(sc[r][c])
    if not check(sqs):return False
    return True

def last(s,row,col):
    [r,c] = next(s,row,col)
    if row>8 or col>8: return True
    return False

def next(s,row,col):
    col +=1 
    row +=col//9
    col %= 9
    while row<9 and col<9 and s[row][col]>0:
        col +=1 
        row +=col//9
        col %= 9
    return [row,col]

def prev(s,row,col):
    col += 8
    row -= 1-(col//9)
    col %=9
    while row>=0 and col>= 0 and s[row][col]>0:
        col += 8
        row -= 1-(col//9)
        col %=9
    return[row,col]

def solve(s):
    sc = copy.deepcopy(s)
    r = 0
    c = 0
    if s[r][c]>0: [r,c] = next(s,r,c)
    while True :
##        print(r,c)
##        for ro in sc: print(ro)
        sc[r][c] += 1
        if sc[r][c]>9:
            sc[r][c]=0
            [r,c] = prev(s,r,c)
##            print('prev0',r,c)
            continue
        while not checkall(sc,r,c):
            sc[r][c] += 1
            if sc[r][c]>9: break
##        print(r,c,sc[r][c])
        
        if sc[r][c]>9:
            sc[r][c]=0
            [r,c] = prev(s,r,c)
            if r<0 or c<0 :
                return "error"
##            print('prev',r,c)
        else:
            if last(s,r,c):
##                print 'last'
                return sc
            [r,c] = next(s,r,c)
            if r>8 or c>8:
##                print 'last2'
                return sc
##            print('next',r,c)

import time

t0 = time.time()
f = open('sudoku.txt','r')
sm = 0
while f:
    if(len(f.readline())==0):break
    s = []
    for i in range(9):
        s.append([int(i) for i in list(f.readline())[:9]])
##    print('solve')
##    for r in s: print(r)
    sc = solve(s)
    sm += sc[0][0]*100+sc[0][1]*10+sc[0][2]
##    print('solved:')
##    for r in sc: print(r)
##    break

print(sm)
print('time',time.time()-t0)
