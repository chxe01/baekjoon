a = int(input())
A = a
for i in range (1, 2*a, 2) :
    print (" " * (a-1) + "*" * i)
    a -= 1

for i in range (2*A-3, 0, -2) :
    print (" " * (a+1) + "*" * i)
    a += 1
