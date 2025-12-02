import math

n = 0

while True : 
    
    a, b, c = map(int,input().split())
    n += 1

    if a == b == c == 0 :
        break

    if c != -1 and a > c :
        print (F'Triangle #{n}')
        print ('Impossible.')
        print()
        continue

    elif c != -1 and b > c :
        print (F'Triangle #{n}')
        print ('Impossible.')
        print()
        continue

        
    
    if a == -1 :
        a = (c ** 2) - (b ** 2) 
        print (F'Triangle #{n}')

        
        if a <= 0 :
            print ('Impossible.')
            print()
            
        else :
            A = math.sqrt(a)
            print (f"a = {A:.3f}")
            print()

    elif b == -1 :
        b = (c ** 2) - (a ** 2) 
        print (F'Triangle #{n}')
        
        if b <= 0 :
            print ('Impossible.')
            print()

        else :
            B = math.sqrt(b)
            print (f"b = {B:.3f}")
            print()
        
    elif c == -1 :
        c = (b ** 2) + (a ** 2)

        print (F'Triangle #{n}')
        
        if c <= 0 :
            print ('Impossible.')
            print()

        else :
            C = math.sqrt(c)
            print (f"c = {C:.3f}")
            print()
