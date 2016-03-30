def link(inF1, inF2, ouF, Score):
    D = {}
    inFile = open(inF1)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = fields[1]
    inFile.close()
    
    inFile = open(inF2)
    ouFile = open(ouF, 'w')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split()
        p1 = fields[0].split('.')[1]
        p2 = fields[1].split('.')[1]
        s = int(fields[2])
        if p1 in D and p2 in D:
            if s >= Score:
                if D[p1] != D[p2]:
                    ouFile.write(D[p1] + '\t' + D[p2] + '\t' + str(s) + '\n')
    inFile.close()
    ouFile.close()

link('Homo_sapiens.GRCh38.81.protein','9606.protein.links.v10.txt','String-human-protein-links-Score400',400)
