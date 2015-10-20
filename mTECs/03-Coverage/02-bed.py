def mkbed(ch, start, end, ouFile):
    for x in range(start, end + 1):
        ouFile.write(ch + '\t' + str(x) + '\t' + str(x) + '\n')

def chrLen(inF):
    D = {}
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            ch = line1.split()[0][1:]
            D[ch] = len(line2)
        else:
            break
    inFile.close()
    return D

CH = [str(x) for x in range(1, 20)] + ['X','Y','MT']
cl = chrLen('/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/Mus_musculus.GRCm38.dna.toplevel.fa.fa')
for ch in CH:
    ouFile = open('MouseRef-'+'chr'+ ch + '.bed', 'w')
    mkbed(ch, 1, cl[ch], ouFile)
    ouFile.close()

        

