n = int(input())
s = list(map(int,input().split()))
li = []

for i in range (n) :
    num = 0
    
    for j in range (1, s[i]+1) :
        if s[i] % j == 0 :
            num += 1

    if num == 2 :
        li.append(s[i])

print (len(li))
