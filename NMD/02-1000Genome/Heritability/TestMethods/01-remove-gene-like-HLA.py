inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
ouFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Gene', 'w')
LS = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L = [fields[0]]
    for item in fields[2:]:
        gene = item.split(':')[1]
        if gene.find('-') == -1:
            L.append(item)
        else:
            print(gene)
    LS.append(L)
LS.sort(cmp = lambda x,y:cmp(len(x), len(y)), reverse=True)

for item in LS:
    if len(item) > 1:
        ouFile.write(item[0] + '\t' + str(len(item[1:])) + '\t' + '\t'.join(item[1:]) + '\n')

inFile.close()
ouFile.close()
