S = set()
def mutation(inF):
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        k = '\t'.join(fields[0:3])
        S.add(k)
    inFile.close()
mutation('K562_WT.hg19_multianno_NGLY1.txt')


ouFile = open('K562_K_only', 'w')
D = {}

def KM(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = '\t'.join(fields[0:3])
        if k not in S:
            D.setdefault(k, [])
            D[k].append(line)
    inFile.close()
KM('K562_K8.hg19_multianno_NGLY1.txt')
KM('K562_K15.hg19_multianno_NGLY1.txt')
KM('K562_K20.hg19_multianno_NGLY1.txt')

for k in D:
    #ouFile.write(str(len(D[k])) + '\t'+ '\t'.join(D[k]) + '\n')
    ouFile.write(D[k][0] + '\n')

ouFile.close()
