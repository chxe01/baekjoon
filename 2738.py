a, b = map(int, input().split())
n = [[0] * b for _ in range(a)]

for _ in range (2) :
    for i in range (3) :
        for j in range (3) :
            n[i][j] = int(input(), end = ' ')


for _ in range (2) :
    for i in range (3) :
        for j in range (3) :
            print (n[i][j])


