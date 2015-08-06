G = {}
inFile = open('hg19_refGene.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[2]
    start = int(fields[4])
    end = int(fields[5])
    gene = fields[12]
    G.setdefault(gene, [])
    G[gene].append([ch,start,end])
inFile.close()

inFile = open('Single-Trait-lm-Sig2')
ouFile = open('Single-Trait-lm-Sig2-Gene', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pv = float(fields[2])
    if pv < 0.05:
        S = set()
        ch = fields[0]
        pos = int(fields[1])
        for g in G:
            for item in G[g]:
                if ch == item[0]:
                    if item[1]<= pos <= item[2]:
                        S.add(g)
        if S:
            ouFile.write(line + '\t' + ':'.join(S) + '\n')
inFile.close()
ouFile.close()
