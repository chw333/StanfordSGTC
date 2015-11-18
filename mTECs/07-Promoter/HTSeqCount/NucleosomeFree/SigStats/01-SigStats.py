Condition = ['Tspan8_positive_MHCII_HighLow_sig.txt', 'Tspan8_negative_MHCII_HighLow_sig.txt', 'MHCII_high_Tspan8_PositiveNegative_sig.txt', 'MHCII_low_Tspan8_PositiveNegative_sig.txt']
ouFile = open('mTECs-Sig-Stats', 'w')

ouFile.write('\t'.join(['Codition', 'no.Sig', 'no.Sig.up', 'no.Sig.down', 'no.Sig.pCoding', 'no.Sig.npCoding', 'no.Sig.up.pCoding', 'no.Sig.up.npCoding', 'no.Sig.down.pCoding', 'no.Sig.down.npCoding']) + '\n')

D = {}
inFile = open('../Mouse_Gene_Promoter.bed2')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '_'.join(fields[3:4]+fields[0:3])
    D[k] = fields[4]
inFile.close()

for ic, con in enumerate(Condition):
    n = 0
    up = 0
    down = 0
    protein_coding = 0
    protein_coding_non = 0
    up_protein_coding = 0
    up_protein_coding_non = 0
    down_protein_coding = 0
    down_protein_coding_non = 0

    inFile = open(con)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        n += 1
        if float(fields[2]) < 0:
            down += 1
            if D[k] == 'protein_coding':
                down_protein_coding += 1
            else:
                down_protein_coding_non += 1


        else:
            up += 1
            if D[k] == 'protein_coding':
                up_protein_coding += 1
            else:
                up_protein_coding_non += 1
        k = fields[0]
        if D[k] == 'protein_coding':
            protein_coding += 1
        else:
            protein_coding_non += 1
            
    inFile.close()
    L = [con, n, up, down, protein_coding, protein_coding_non, up_protein_coding, up_protein_coding_non, down_protein_coding, down_protein_coding_non]
    ouFile.write('\t'.join([str(x) for x in L]) + '\n')
