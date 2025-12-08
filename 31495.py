a = input()
l = len(a)

if l > 2 and a[0] == '"' and a[-1] == '"' :
    print (a[1:l-1])

elif l > 2 and a[0] == "'" and a[-1] == "'" :
    print (a[1:l-1])
    
else :
    print ('CE')
