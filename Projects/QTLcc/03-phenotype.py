def check_gene(inF):
    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    inFile.close()
    return head
rna = check_gene('Yeast-RNA')
pL = check_gene('Yeast-ProteinLight')
pH = check_gene('Yeast-ProteinHeavy')
print(len(rna))
print(len(pL))
print(len(pH))
if rna == pL:
    print('gene: rna == proteinLight')
else:
    print('gene: rna != proteinLight')
if rna == pH:
    print('gene: rna == proteinHeavy')
else:
    print('gene: rna != proteinHeavy')
    print(set(rna) - set(pH))


def combine(inF0, inF1, inF2, inF3, ouF):
    D = {}
    H = []
    Strains = []
    inFile = open(inF0)
    for line in inFile:
        line = line.strip()
        Strains.append(line)
    inFile.close()
    print(len(Strains))

    inFile = open(inF1)
    head = inFile.readline().strip().split('\t')
    for h in head:
        H.append(h + ':' + 'RNA')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        s = fields[0]
        D[s] = fields[1:]
    inFile.close()

    inFile = open(inF2)
    head = inFile.readline().strip().split('\t')
    for h in head:
        H.append(h + ':' + 'ProteinLight')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        s = fields[0]
        D[s] += fields[1:]
    inFile.close()

    inFile = open(inF3)
    head = inFile.readline().strip().split('\t')
    for h in head:
        H.append(h + ':' + 'ProteinHeavy')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        s = fields[0]
        D[s] += fields[1:]
    inFile.close()

    ouFile = open(ouF, 'w')
    ouFile.write('Strain' + '\t' + '\t'.join(H) + '\n')
    for st in Strains:
        if len(D[st]) == len(H):
            ouFile.write(st + '\t' + '\t'.join(D[st]) + '\n')
        else:
            print('###error###')
    ouFile.close()



combine('Yeast-Strains', 'Yeast-RNA', 'Yeast-ProteinLight','Yeast-ProteinHeavy', 'Yeast-Phenotype')




