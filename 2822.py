S1, S2 = [], []

for i in range (8) :
    score = int(input())
    S1.append(score)
    S2.append(score)

S2.sort(reverse = True)
n = 0
N = []

for i in range (5):
    N.append(S1.index(S2[i]) + 1)
    n += S2[i]

print (n)
N.sort()
print (*N)
