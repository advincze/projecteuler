

def intToMinRoman(n):
##    print 'to roman:',n
    rom = ''
    th = n//1000
    for i in range(th): rom += 'M'
    n %= 1000
    
    hu = n//100
    if hu==9:
        rom += 'CM'
        hu = 0
    elif hu>4:
        rom += 'D'
        hu -= 5
    if hu==4:
        rom += 'CD'
    else:
        for i in range(hu): rom += 'C'
    
    n %= 100
    te = n//10
    if te==9:
        rom += 'XC'
        te = 0
    elif te>4:
        rom += 'L'
        te -= 5
    if te==4:
        rom += 'XL'
    else:
        for i in range(te): rom += 'X'
        
    n %= 10

    if n==9:
        rom += 'IX'
        n = 0
    elif n>4:
        rom += 'V'
        n -= 5
    if n==4:
        rom += 'IV'
    else:
        for i in range(n): rom +='I'
        
##    print th,'-',hu,'-',te,'-',n,'=>',rom
    
    return rom

r2i = {'I': 1, 'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
i2r = {1:'I', 5:'V', 10:'X',50:'L',100:'C',500:'D',1000:'M'}

def romanToInt(rom):
##    print 'to int:',rom
    val = 0
    i0 = rom[0]
    for i in range(len(rom)-1):
        v0 = r2i[rom[i]]
        v1 = r2i[rom[i+1]]
        if v0<v1: val -= v0
        else: val += v0
    val += r2i[rom[len(rom)-1]]
    return val


import time

t0 = time.time()
f = open('roman.txt','r')
sm = 0
k = 0
while f:
    line = f.readline().strip('\n')
    if(len(line)==0):break
    i = romanToInt(line)
    s = intToMinRoman(i)
    saved = len(line)-len(s)
##    print 'saved:',saved
    sm += saved
    
    k += 1
##    if k==20: break
f.close()
print 'solution to 89:',sm
print 'time',time.time()-t0
