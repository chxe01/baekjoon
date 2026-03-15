MAX = 1000000

li = [True] * (MAX + 1)
li[0], li[1] = False, False

p = 2

while p * p <= MAX :
    if li[p] == True :
        for i in range(p * p, MAX + 1, p) :
            li[i] = False

    p += 1

while True :
    n = int(input())
    if n == 0 :
        break

    for i in range(2, n) :
        if li[i] and li[n-i] :
            if i + n-i == n :
                print (f'{n} = {i} + {n-i}')
                break

        else :
            print('Goldbach\'s conjecture is wrong.')
            break
    