D = {}
inFile = open('NMD-Genes-Pos')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D[fields[0]] = fields
inFile.close()


I = 10000

inFile = open('1000Genome-462LCLs-Position')
ouFile = open('1000Genome-462LCLs-Position-cis', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    pos = int(fields[1])
    flag = 0
    for k in D:
        if ch == D[k][1]:
            if int(D[k][2]) - I <= pos <= int(D[k][3]) + I:
                flag = 1
                break
    if flag:
        ouFile.write(line + '\n')


inFile.close()
ouFile.close()
