sn, n, mon = map(int, input().split())

if sn * n <= mon:
    print (0)

else:
    print (sn * n - mon)