a = int(input())

for i in range (a):
    if a == 0 :
        break
    y, k = 0, 0
    
    for j in range (9) :
        
        Y, K = map(int,input().split())
        y += Y
        k += K

    if y > k :
        print ("Yonsei")

    elif y < k :
        print ("Korea")

    else :
        print ("Draw")
