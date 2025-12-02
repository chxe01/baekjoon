a = int(input())
b = list(input().split())
c, d = [], []
n = int(input())
for i in range (n) :
    A,B = map(int,input().split())
    
    for j in range(A-1,B) :
        c.append(b[j])

    for k in range(B-1, A, -1):
        d.append(b[k])
        
    for _ in range (len(b)) :
        if c[_] == d[_] :
            print (1)

        else :
            print (0)
