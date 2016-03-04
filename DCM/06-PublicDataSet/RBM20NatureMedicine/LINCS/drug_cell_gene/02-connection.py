def connection():
    UP = []
    DN = []

    inFile = open('DCM-GeneCountSymbol-S635A_CP1CP2_up_gene_filtered')
    for line in inFile:
        line = line.strip()
        UP.append(line)
    inFile.close()

    inFile = open('DCM-GeneCountSymbol-S635A_CP1CP2_down_gene_filtered')
    for line in inFile:
        line = line.strip()
        DN.append(line)
    inFile.close()

    UPDN = []
    for x in UP:
        UPDN.append(1)
    for x in DN:
        UPDN.append(2)

    print(''.join([str(x) for x in UPDN]))

    inFile = open('digoxin_cell_gene')
    for line in inFile:
        L = []
        line = line.strip()
        fields = line.split('\t')
        up = fields[2].split()
        dn = fields[3].split()
        for x in UP:
            if x in up:
                L.append(1)
            elif x in dn: 
                L.append(2)
            else:
                L.append(0)
        for x in DN:
            if x in up:
                L.append(2)
            elif x in dn: 
                L.append(1)
            else:
                L.append(0)

        print(''.join([str(x) for x in L]))

    inFile.close()


connection()
