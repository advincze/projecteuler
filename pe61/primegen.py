import math

def prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    if(num%2==0):
        return False
    limit = math.floor(math.sqrt(num))
    i = 3
    while i<=limit:
        if num%i==0:
            return False
        i+=2
    return True

pp = filter(prime, range(3,10**7,2))

try:
    f = open('primes.txt', 'w')
    for p in pp:
        f.write(str(p)+",")
except Exception as ex:
    print ex
f.close()
print "done"
