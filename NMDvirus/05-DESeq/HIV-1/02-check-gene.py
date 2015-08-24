D = {}
inFile = open('deHIV1_24h_sig_proteincoding.txt')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[7]
    D.setdefault(gene, [])
    D[gene].append(line)
inFile.close()


def check(Gene):
    for g in Gene:
        for k in D:
            if k.find(g) == 0:
                print('\n'.join(D[k]))
    print('#####')

G = ['UPF']
check(G)
G = ['SMG']
check(G)
G = ['SRSF2', 'ASNS', 'CARS']
check(G)
