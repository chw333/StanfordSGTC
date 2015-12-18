def split(inF):
    inFile = open(inF)
    ouFile1 = open(inF.split('.txt')[0] + '.intron.txt', 'w')
    ouFile2 = open(inF.split('.txt')[0] + '.other.txt', 'w')
    head = inFile.readline()
    ouFile1.write(head)
    ouFile2.write(head)
    for line in inFile:
        fields = line.split('\t')
        if fields[5] == 'intronic':
            ouFile1.write(line)
        else:
            ouFile2.write(line)
    
    inFile.close()
    ouFile1.close()
    ouFile2.close()

split('AnnotSNP.hg19_multianno_gene_only.txt')
