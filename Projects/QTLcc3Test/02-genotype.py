def strain(inF):
    S = []
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        st = fields[0]
        S.append(st)
    inFile.close()
    return S

geno = strain('Yeast-Genotype')
rna = strain('Yeast-RNA')
proteinLight = strain('Yeast-ProteinLight')
proteinHeavy = strain('Yeast-ProteinHeavy')
print(len(geno))
print(len(rna))
print(len(proteinLight))
print(len(proteinHeavy))

print(len(set(geno)))
print(len(set(rna)))
print(len(set(proteinLight)))
print(len(set(proteinHeavy)))


if rna == proteinLight:
    print('strain: rna == proteinLight')
if rna == proteinHeavy:
    print('strain: rna == proteinHeavy')

Strains = set(geno) & set(rna)  
ouFile = open('Yeast-Strains', 'w')
for x in Strains:
    ouFile.write(x + '\n')
ouFile.close()

def format(inF):
    D = {}
    ouFile = open(inF + '-Formated', 'w')
    inFile = open(inF)
    head = inFile.readline().strip()
    ouFile.write('Strain\t' + head + '\n')
    for line in inFile:
        L = []
        line = line.strip()
        fields = line.split('\t')
        st = fields[0]
        for x in fields[1:]:
            g = int(x) - 1
            #g = int(x)
            L.append(str(g))
            if g != 0 and g != 1:
                print(g)
        D[st] = L
    for st in Strains:
        ouFile.write(st + '\t' + '\t'.join(D[st]) + '\n')
    inFile.close()
    ouFile.close()
format('Yeast-Genotype')

def pos(inF):
    D = {}
    inFile = open('Yeast-Mark-Pos')
    ouFile = open('Yeast-Position', 'w')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        mrk = fields[0]
        ch = fields[1]
        start = int(float(fields[2]))
        end = int(float(fields[3]))
        center = int((start + end)/2)
        D[mrk] = [ch, center]
    inFile.close()
    inFile = open(inF)
    head = inFile.readline().strip()
    fields = head.split('\t')
    print(len(fields))
    for item in fields:
        ouFile.write(D[item][0] + '\t' + str(D[item][1]) + '\n')
    inFile.close()
    ouFile.close()

pos('Yeast-Genotype')


