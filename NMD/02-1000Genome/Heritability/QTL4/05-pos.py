D = {}
inFile = open('NMD-Genes-Pos')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields
inFile.close()


I = 100000

inFile = open('Single-Trait-lm-Sig-Gene-Sorted')
ouFile = open('Single-Trait-lm-Sig-Gene-Sorted-Pos', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    pos = int(fields[1])
    for k in D:
        if ch == D[k][1]:
            if int(D[k][2]) - I <= pos <= int(D[k][3]) + I:
                ouFile.write(line + '\t' + '\t'.join(D[k]) + '\n')


inFile.close()
ouFile.close()
