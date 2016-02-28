D = {}
inFile = open('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh37.75.gene')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields[1]
inFile.close()

def symbol(inF):
    inFile = open(inF)
    ouFile = open(inF + 'Symbol', 'w')
    head = inFile.readline().strip()
    ouFile.write('GeneName\tGeneID\t'+head+'\n')
    for line in inFile:
        fields = line.split('\t')
        ouFile.write(D[fields[0]] + '\t' + line)

    inFile.close()
    ouFile.close()

symbol('DCM-GeneCount')
