import math

a = int(input())
b = int(input())

N = []
n = 0

for i in range (a, b+1) :
    if int(math.sqrt(i)) ** 2 == i:
        N.append(i)


if len(N) > 0 :
    for i in N :
        n += i
        
    print (n)
    print (min(N))

else :
    print (-1)
