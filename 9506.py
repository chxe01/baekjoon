while True :
    

    n = int(input())
    if n == -1 :
        break
    l, a, Sum = [], 0, 0
    
    for i in range (n, 1, -1) :
        if n % i == 0 :
            l.append(n//i)
            l.append ('+')
            a += 1
            Sum += n//i
            
    l.remove(l[-1])
    
    
     if n == Sum :
        print (n,'=', *l)
            
    else :
        print (f'{n} is NOT perfect.')
    