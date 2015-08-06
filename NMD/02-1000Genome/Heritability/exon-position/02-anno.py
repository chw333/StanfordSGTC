G = {}
inFile = open('hg19_refGene.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')

    nm = fields[1]
    ch = fields[2]
    strand = fields[3]
    gene_start = fields[4]
    gene_end = fields[5]
    cds_start = fields[6]
    cds_end = fields[7]
    exon_start = [int(x) for x in fields[9].split(',')[0:-1]]
    exon_end = [int(x) for x in fields[10].split(',')[0:-1]]
    gene = fields[12]

    if nm not in G:
        G[nm] = [nm, ch, strand, int(gene_start), int(gene_end), int(cds_start), int(cds_end), exon_start, exon_end, gene]
inFile.close()


def exon_pos(ch, pos, anno):
    exon_start = anno[7]
    exon_end = anno[8]
    exon_ind = -1
    offset = -1
    if anno[2] == '+':
        for i in range(len(exon_start)):
            if exon_start[i]+1 <= pos <= exon_end[i]:
                exon_ind = i + 1
                offset = exon_end[i] - pos + 1
    elif anno[2] == '-':
        for i in range(len(exon_start)):
            if exon_start[i]+1 <= pos <= exon_end[i]:
                exon_ind = len(exon_start) - i 
                offset = pos - exon_start[i]
    return([len(exon_start), exon_ind, offset])

inFile = open('G462-Sample-Stopgain-Exon')
ouFile = open('G462-Sample-Stopgain-Exon-Escape', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split(':')
    snp = fields[0]
    gene = fields[1]
    nm = fields[2]
    exon = fields[3]
    ch = 'chr' + snp.split('_')[1]
    pos = int(snp.split('_')[2])
    e = exon_pos(ch, pos, G[nm])
    escape = 'F'
    if e[0] == e[1]:
        escape = 'T'
    elif e[0] == e[1] + 1:
        if e[2] <= 55:
            escape = 'T'
    ouFile.write(snp + '\t' + '\t'.join([str(x) for x in e]) + '\t' + escape + '\n')

inFile.close()
ouFile.close()


