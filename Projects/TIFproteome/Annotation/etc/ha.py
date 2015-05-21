L = []
pep = 'ABCDIIDELDD'
for i in range(len(pep)):
    if pep[i] == 'I' or pep[i] == 'L':
        L.append(i)

S = set()
S.add(pep)
for i in range(len(L)):
    S2 = set()
    for pep in S:
        n = L[i]
        pep1 = pep[0:n] + 'I' + pep[n+1:]
        pep2 = pep[0:n] + 'L' + pep[n+1:]
        S2.add(pep1)
        S2.add(pep2)
    S = S2
print(S)


