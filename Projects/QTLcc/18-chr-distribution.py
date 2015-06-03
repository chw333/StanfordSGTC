D = {}
inFile = open('YeastGenome.fa')
CH = ['chrI','chrII','chrIII','chrIV','chrV','chrVI','chrVII','chrVIII','chrIX','chrX','chrXI','chrXII','chrXIII','chrXIV','chrXV','chrXVI']
CHH = {}
CHH['chr01'] = 'chrI'
CHH['chr02'] = 'chrII'
CHH['chr03'] = 'chrIII'
CHH['chr04'] = 'chrIV'
CHH['chr05'] = 'chrV'
CHH['chr06'] = 'chrVI'
CHH['chr07'] = 'chrVII'
CHH['chr08'] = 'chrVIII'
CHH['chr09'] = 'chrIX'
CHH['chr10'] = 'chrX'
CHH['chr11'] = 'chrXI'
CHH['chr12'] = 'chrXII'
CHH['chr13'] = 'chrXIII'
CHH['chr14'] = 'chrXIV'
CHH['chr15'] = 'chrXV'
CHH['chr16'] = 'chrXVI'

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1[1:]] = len(line2)
    else:
        break
inFile.close()

ouFile = open('Yeast-Chr-Region', 'w')

R = 10000
n = 0
CHR = []
CX = {}
for c in CH:
    n += 1
    length = D[c]
    for i in range(1, length+1, R):
        #ouFile.write(c + '\t' + str(i) + '\t' + str(i + R) + '\t' + str(n) + '\n')
        k = c + '\t' + str(i) + '\t' + str(i + R) + '\t' + str(n)
        CX.setdefault(k, 0)
        CHR.append(k)
ouFile.close()

def qtl(inF):
    inFile = open(inF)
    ouFile = open(inF + '-chr', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = CHH[fields[1]]
        pos = int(fields[2])
        for k in CX:
            ks = k.split('\t')
            c = ks[0]
            st = int(ks[1])
            ed = int(ks[2])
            if ch == c and st<= pos <= ed:
                CX[k] += 1
    inFile.close()
    for k in CHR:
        ouFile.write(k + '\t' + str(CX[k]) + '\n')
    ouFile.close()

qtl('Yeast-RNA-ProteinLight-CommonEffect-Sig-noCov-Merged')
qtl('Yeast-Single-Trait-Merged-ProteinLightSpecific')

