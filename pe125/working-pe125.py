##The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
##
##There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
##
##Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
import math
def ispal(s):
    s = str(s)
    for i in range(math.floor(len(s)/2)):
        if s[i] != s[-1-i]:
            return False;
    return True

import time
t0 = time.time()

li = 10+1
sq = [i*i for i in range(li)]

print(sq)



a = [sq]*li
print(a)

  
##for i in range(10**4):
##    for j in range(10**4-i):
##        a[i,j] = 5

print('time',time.time()-t0)
