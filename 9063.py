n = int(input())
li_x = []
li_y = []

for i in range (n) :
    x, y = map(int,input().split())
    li_x.append (x)
    li_y.append (y)
    
X = max(li_x) - min(li_x)
Y = max(li_y) - min(li_y)

print (X * Y)
