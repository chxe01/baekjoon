s, e = map(int,input().split())

li = [True] * (e + 1)
li[0], li[1] = False, False

p = 2

while p * p <= e :
    if li[p] == True :
        for i in range(p * p, e + 1, p) :
            li[i] = False

    p += 1

for i in range (s, e+1) :
    if li[i] == True :
        print(i)