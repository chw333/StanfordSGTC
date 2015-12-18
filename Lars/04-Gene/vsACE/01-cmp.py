D = {}
D2 = {}

inFile = open('AnnotSNP.hg19_multianno_gene.txt')
head1 = inFile.readline()
for line in inFile:
    fields = line.split('\t')
    k = '\t'.join(fields[0:2])
    D[k] = line
inFile.close()

'''
inFile = open('AnnotINDEL.hg19_multianno_gene.txt')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:3])
    D[k] = line
inFile.close()
'''

inFile = open('Variation-All.txt')
head3 =  inFile.readline()
for line in inFile:
    fields = line.split('\t')
    k = 'chr'+'\t'.join(fields[0:2])
    D2[k] = line
inFile.close()

ouFile1 = open('AnnotSNP.hg19_multianno_gene_only.txt','w')
ouFile2 = open('Variation-All_ACEonly.txt', 'w')
ouFile3 = open('AnnotSNP.hg19_multianno_gene_overlapped.txt','w')
ouFile1.write(head1)
ouFile2.write(head3)
ouFile3.write(head1)
for k in D:
    if k in D2:
        ouFile3.write(D[k])
    if k not in D2:
        ouFile1.write(D[k])
for k in D2:
    if k not in D:
        ouFile2.write(D2[k])
ouFile1.close()
ouFile2.close()
ouFile3.close()
