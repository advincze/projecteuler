import math

def prime(num):
    limit = math.floor(math.sqrt(num))
    i = 3
    while i<=limit:
        if num%i==0:
            return False
        i+=2
    return True

prcache = dict()
def cprime(num):
    if num not in prcache:
        prcache[num] = prime(num)
    return prcache[num]

def testgr(pr, prg):
    spr = str(pr)
    for pr2 in prg:
        spr2 = str(pr2)
        if not cprime(int(spr+spr2)) or not cprime(int(spr2+spr)):
            return False
    return True


def pe60():
    prs = filter(cprime,range(3,10**4,2))
    prgs = []
    for pr in prs:
        prgs.append([pr])
        for prg in prgs:
            if testgr(pr, prg):
                prg2 = prg[:]
                prg2.append(pr)
                if(len(prg2)==5):
                    return sum(prg2)
                prgs.append(prg2)
                
import time

t0 = time.time()
print pe60()
print('time',time.time()-t0)
