a = int(input())
b, c = 1, 0
for i in range (a, 0, -1):
    
    b *= i 

b = str(b)
for i in range (len(b)-1,-1,-1) :

    if b[i] == '0' :
        c += 1
    else :
        break

print (c)