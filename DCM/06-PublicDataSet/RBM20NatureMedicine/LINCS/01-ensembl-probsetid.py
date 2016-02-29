inFile = open('ProbSetID-Ensembl-GeneSymbol-HG-U133A_2.na34.annot.txt')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = []
    x = fields[1].split('///')
    for y in x:
        D[fields[0]].append(y.strip())
    x = fields[2].split('///')
    for y in x:
        D[fields[0]].append(y.strip())
inFile.close()

def cmp(upF, downF):

    inFile = open(upF)
    ouFile = open(upF + '-ProbSetID', 'w')
    ouFile2 = open(upF + '-ProbSetID.grp', 'w')
    for line in inFile:
        ensembl = line.split('\t')[1]
        flag = 0
        for k in D:
            if ensembl in D[k]:
                ouFile.write(ensembl + '\t' + k + '\n')
                ouFile2.write(k + '\n')
                flag = 1
        if flag == 0:
            print(ensembl + '\t' + 'NA' + '\n')
    
    inFile.close()
    ouFile.close()
    ouFile2.close()
    
    
    inFile = open(downF)
    ouFile = open(downF + '-ProbSetID', 'w')
    ouFile2 = open(downF + '-ProbSetID.grp', 'w')
    for line in inFile:
        ensembl = line.split('\t')[1]
        flag = 0
        for k in D:
            if ensembl in D[k]:
                ouFile.write(ensembl + '\t' + k + '\n')
                ouFile2.write(k + '\n')
                flag = 1
        if flag == 0:
            print(ensembl + '\t' + 'NA' + '\n')
    
    inFile.close()
    ouFile.close()
    ouFile2.close()
cmp('DCM-GeneCountSymbol-S635A_CP1CP2_up', 'DCM-GeneCountSymbol-S635A_CP1CP2_down')
