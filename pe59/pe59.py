import string
def keys():
    keys = []
    for i in string.ascii_lowercase: 
        for j in string.ascii_lowercase:
           for k in string.ascii_lowercase:
            keys.append([ord(i),ord(j),ord(k)])
    return keys


def decypher(data,key):
     result = [ chr(d ^ k[i%3]) for i, d in enumerate(data) ]
     return "".join(result)


import time
t0 = time.time()
#code here
f = open('cipher1.txt','r')
data =[int(s) for s in (f.readline().split(','))]
f.close()

for k in keys():
    x = decypher(data, k)
    if ("@" not in x) and \
       ("#" not in x) and \
       ("$" not in x) and \
       ("%" not in x) and \
       ("^" not in x) and \
       ("&" not in x) and \
       ("<" not in x) and \
       (">" not in x) and \
       ("|" not in x) and \
       ("{" not in x) and \
       ("}" not in x) and \
       ("+" not in x) and \
       ("*" not in x):
        s = sum(ord(a) for a in x)
        kc = "".join([chr(l) for l in k])
        print(x, k, kc, s)

    

print('time',time.time()-t0)
