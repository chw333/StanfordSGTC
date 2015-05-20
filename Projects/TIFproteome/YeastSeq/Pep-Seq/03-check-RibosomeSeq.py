import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
D = {}
inFile = open('Yeast-peptide-sixFrame-pep')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    seq = fields[2].split(':')[-1]
    seq_rev = string.translate(seq[::-1], trans)
    D.setdefault(seq, [])
    D.setdefault(seq_rev, [])
inFile.close()

def seq(inF):
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        line3 = inFile.readline().strip()
        line4 = inFile.readline().strip()
        if line1:
            for k in D:
                if k in line2:
                    D[k].append(line1 + ':' + line2)
        else:
            break
    inFile.close()

seq('SRR1258539.noN.fastq')
seq('SRR1258540.noN.fastq')

ouFile = open('SixFrame-RibosomeSeq-pep-reads','w')
for k in D:
    ouFile.write(k +'\t'+str(len(D[k]))+ '\t' + '\t'.join(D[k]) + '\n')
ouFile.close()
