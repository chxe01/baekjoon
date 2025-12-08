import sys
input = sys.stdin.readline

a = int(input())
c = []
for i in range (1, a+1):
    b = int(input())
    c.append(b)
c.sort()
for j in range (len(c)):
    print(c[j])
