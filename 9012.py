import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input()) 


for _ in range (n) :
    rhkf = input().strip()
    li = []


    for i in range (len(rhkf)) :
        
        if rhkf[i] == '(' :
            li.append(rhkf[i])

        else :
            if len(li) == 0 :
                write ('NO\n')
                break

            else :
                li.pop()


    else :
        if len(li) == 0 :
            write ('YES\n')
    
        else:
            write ('NO\n')