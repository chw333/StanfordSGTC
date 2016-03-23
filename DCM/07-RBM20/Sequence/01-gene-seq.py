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
    s = D[gene[0]][gene[1]-1-1000:gene[2]]
    #s = D[gene[0]][gene[1]-1:gene[2]]
    print(s)

gene = ['10',112404154, 112599229]
seq(gene)
