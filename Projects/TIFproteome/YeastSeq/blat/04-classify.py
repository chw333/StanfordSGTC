import string
trans = string.maketrans('ATCGatcg','TAGCtagc')

def mRNA(inF):
    D = {}
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            #line2_rev =  string.translate(line2[::-1], trans)
            D.setdefault(line2, [])
            #D.setdefault(line2_rev, [])
            D[line2].append(line1)
            #D[line2_rev].append(line1)
        else:
            break
    inFile.close()
    return D
MRNA = mRNA('/srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.fa')

def isSplicing(seq):
    seq_rev = string.translate(seq[::-1], trans)
    flag = 0
    for k in MRNA:
        if seq in k:
            flag += 1
            return flag
        if seq_rev in k:
            flag += 1
            return flag
    return flag
        

def classify(inF):
    inFile = open(inF)
    ouFile = open(inF + '.classified', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')

            ch1 = fields1[2]
            ch2 = fields2[2]

            qpos1 = float(fields1[7])
            qpos2 = float(fields1[8])
            pos1 = float(fields1[9])
            pos2 = float(fields1[10])

            qpos3 = float(fields2[7])
            qpos4 = float(fields2[8])
            pos3 = float(fields2[9])
            pos4 = float(fields2[10])

            mid1 = (pos1+pos2)/2
            mid2 = (pos3+pos4)/2
            qmid1 = (qpos1+qpos2)/2
            qmid2 = (qpos3+qpos4)/2

            seq = fields1[1]


            if ch1 != ch2:
                ouFile.write(line1 + '\t' + 'Translocation' + '\n')
                ouFile.write(line2 + '\t' +'Translocation' + '\n')
            elif (pos1 - pos2)*(pos3-pos4) < 0:
                ouFile.write(line1 + '\t' + 'Inversion' + '\n')
                ouFile.write(line2 + '\t' + 'Inversion' + '\n')
            else:
                if (pos1 - pos2) < 0  and (pos3 - pos4) <0 :
                    if (mid1 - mid2)*(qmid1 - qmid2) < 0:
                        ouFile.write(line1 + '\t' + 'Duplication' + '\n')
                        ouFile.write(line2 + '\t' + 'Duplication' + '\n')
                    else:
                        if isSplicing(seq):
                            ouFile.write(line1 + '\t' + 'Splicing' + '\n')
                            ouFile.write(line2 + '\t' + 'Splicing' + '\n')
                        else:
                            ouFile.write(line1 + '\t' + 'Deletion' + '\n')
                            ouFile.write(line2 + '\t' + 'Deletion' + '\n')
                            
                elif (pos1 -pos2) >0 and (pos3 - pos4) > 0:
                    if (mid1 - mid2)*(qmid1 - qmid2) > 0:
                        ouFile.write(line1 + '\t' + 'Duplication' + '\n')
                        ouFile.write(line2 + '\t' + 'Duplication' + '\n')
                    else:
                        if isSplicing(seq):
                            ouFile.write(line1 + '\t' + 'Splicing' + '\n')
                            ouFile.write(line2 + '\t' + 'Splicing' + '\n')
                        else:
                            ouFile.write(line1 + '\t' + 'Deletion' + '\n')
                            ouFile.write(line2 + '\t' + 'Deletion' + '\n')
        else:
            break
    inFile.close()
    ouFile.close()

classify('SRR1258470-soft-filtered.fa.blated.filtered.seq')
classify('SRR1258471-soft-filtered.fa.blated.filtered.seq')


