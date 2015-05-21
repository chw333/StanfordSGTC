D = {}
inFile = open('/srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/Saccharomyces_cerevisiae.R64-1-1.79.gtf')
for n in range(5):
    head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[2] == 'gene':
        try:
            ch = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            strand = fields[6]
            fds = fields[8].split(';')
            if len(fds) == 6:
                gene_id = fds[0].split('"')[1]
                gene_name = fds[2].split('"')[1]
                gene_biotype = fds[4].split('"')[1]
            elif len(fds) == 5:
                gene_id = fds[0].split('"')[1]
                gene_name = 'NA'
                gene_biotype = fds[3].split('"')[1]
            else:
                print(line)
            D.setdefault(gene_id, [])
            D[gene_id].append([ch, strand, start, end, gene_id, gene_name, gene_biotype])
        except:
            print(line)

inFile.close()

def classify(inF):
    inFile = open(inF)
    ouFile = open(inF + '.gene', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')

            ch1 = fields1[2]
            ch2 = fields2[2]
            pos1 = float(fields1[9])
            pos2 = float(fields1[10])
            pos3 = float(fields2[9])
            pos4 = float(fields2[10])
            S = set() 
            for k in D:
                for item in D[k]:
                    if (item[0] == ch1 and (pos1 <= item[2] <= pos2 or pos1 <= item[3] <= pos2 or (item[2]<pos1 and item[3]>pos2))) or \
                            (item[0] == ch2 and (pos3 <= item[2] <= pos4 or pos3 <= item[3] <= pos4 or (item[2]<pos3 and item[3]>pos4))): 
                                S.add(k)
            if S:
                gene_id = list(S)[0]
                ouFile.write(line1 + '\t' + '\t'.join(D[gene_id][0][4:]) + '\n')
                ouFile.write(line2 + '\t' + '\t'.join(D[gene_id][0][4:]) + '\n')
            else:
                ouFile.write(line1 + '\t' + '\t'.join(['NA','NA','NA']) + '\n')
                ouFile.write(line2 + '\t' + '\t'.join(['NA','NA','NA']) + '\n')
        else:
            break
    inFile.close()
    ouFile.close()

classify('SRR1258470-soft-filtered.fa.blated.filtered.seq.classified')
#classify('SRR1258471-soft-filtered.fa.blated.filtered.seq.classified')
