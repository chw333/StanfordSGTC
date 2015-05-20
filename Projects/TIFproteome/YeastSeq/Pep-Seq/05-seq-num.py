import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
def seqNum(inF1, inF2):
    D = {}
    inFile = open(inF2)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = fields[1:]
    inFile.close()

    ouFile2 = open(inF2 + '-reads', 'w')
    for k in D:
        ouFile2.write('>' + k + '\n')
        for x in D[k][1:]:
            ouFile2.write(x.split('\t')[-1].split(':')[-1] + '\n')
    ouFile2.close()

    inFile = open(inF1)
    ouFile = open(inF1 + '-PolysomeSeq', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        seq = fields[3].split(':')[-1]
        seq_rev = string.translate(seq[::-1], trans)
        dna = D[seq][1:] + D[seq_rev][1:]
        num = len(dna)
        ouFile.write(str(num) + '\t' + line + '\n')
    inFile.close()
    ouFile.close()

seqNum('Yeast-peptide-sixFrame-pep-Trypsin-filtered-seq-cdna-cds-RibosomeSeq','FiveEnriched-PolysomeSeq-pep-reads')
