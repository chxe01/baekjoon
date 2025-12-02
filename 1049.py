import math

a, b = map(int,input().split())
A_list = []
B_list = []
li = []

for i in range (b):
    A, B = map(int,input().split())
    A_list.append (A)
    B_list.append (B)
    
if a <= 6 :
    for i in A_list:
        li.append (i)
    for i in B_list:
        li.append (i * a) 


else :
    for i in A_list:
        li.append (i * math.ceil(a / 6))

    for i in B_list:
        li.append (i * a)

    for i in range (b) :
        for j in range (b) :
            li.append (A_list[i] * (a // 6) + B_list[j] * (a % 6))

print (min(li))
