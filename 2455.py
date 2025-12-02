P, p = [], 0
S, T = [], []
for i in range (4) :
    s, t = map(int,input().split())
    S.append(s)
    T.append(t)

p = S[0] + T[0]
P.append(p)

for i in range (1,3):

    p -= S[i]
    P.append(p)

    p += T[i]
    P.append(p)


print (max(P))
