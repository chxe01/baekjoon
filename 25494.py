n = int(input())
l = 1

for i in range (n) :
    a,b,c = map(int,input().split())

    while True :
        if (a == l or b == l or c == l) :
            for i in range (3):
                print (l, end = ' ')
                break

        else :
            l += 1
