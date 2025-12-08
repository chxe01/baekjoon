a = int(input())

for i in range (a) :
    num, st = input().split()

    for j in st :
        print (j * int(num), end = '')

    print ()
