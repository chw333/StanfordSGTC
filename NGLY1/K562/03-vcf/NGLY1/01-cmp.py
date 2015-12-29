S = set()
def mutation(inF):
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        k = '\t'.join(fields[0:3])
        S.add(k)
    inFile.close()
mutation('K562_K8.hg19_multianno_NGLY1.txt')
mutation('K562_K15.hg19_multianno_NGLY1.txt')
mutation('K562_K20.hg19_multianno_NGLY1.txt')


inFile = open('K562_WT.hg19_multianno_NGLY1.txt')
ouFile = open('K562_WT_only', 'w')
for line in inFile:
    fields = line.split('\t')
    k = '\t'.join(fields[0:3])
    if k not in S:
        ouFile.write(line)
inFile.close()
ouFile.close()
