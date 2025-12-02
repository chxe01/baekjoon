a = int(input())
A = []
for i in range (14) :
    b = input()

    if len(b) == 6 :
        A.append(int(b[-1]))

    elif len(b) == 5 :
        if len(A) == 0 :
            print (1)

        else :
            print (0)
            
    elif len(b) == 4 :
        print(len(A))

    elif len(b) == 3 :
        if b == 'top' :
            if A[-1] > 0 :
                print (A[-1])

            else :
                print (-1)

        elif b == 'pop' :
            A.remove(A[-1])

            if A[-1] >= 0 :
                print (A[-1])

            else :
                print (-1)
                
