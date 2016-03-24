import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
D = {}
inFile = open('Homo_sapiens.GRCh37.75.dna.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        ch = line1.split()[0][1:]
        D[ch] = line2
    else:
        break
inFile.close()



def seq(gene):
    ouFile1 = open(gene[0] + '_Seq_incl_1000up', 'w')
    ouFile2 = open(gene[0] + '_Seq', 'w')
    if gene[2] == '+':
        s1 = D[gene[1]][gene[3]-1-1000:gene[4]]
        ouFile1.write(s1 + '\n')
        s2 = D[gene[1]][gene[3]-1:gene[4]]
        ouFile2.write(s2 + '\n')
    elif gene[2] == '-':
        s1 = D[gene[1]][gene[3]:gene[4]+1000]
        s1r = string.translate(s1, trans)
        ouFile1.write(s1r[::-1] + '\n')
        s2 = D[gene[1]][gene[3]-1:gene[4]]
        s2r = string.translate(s2, trans)
        ouFile2.write(s2r[::-1] + '\n')

gene = ['RBM20','10', '+', 112404154, 112599229]
seq(gene)
gene = ['EGR1','5', '+', 137801180, 137805004]
seq(gene)
gene = ['ZBTB7A','19', '-', 4045215, 4066816]
seq(gene)
