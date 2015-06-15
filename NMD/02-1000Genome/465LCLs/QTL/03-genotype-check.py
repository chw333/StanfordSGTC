import numpy as np
def check(inF):
    ###   all genotype
    L = []
    inFile = open(inF)
    ouFile = open(inF + '-checked', 'w')
    head = inFile.readline().strip('\n').split()
    n = len(head[1:])
    for line in inFile:
        line = line.strip()
        fields = line.split()
        g = fields.count('1') + fields.count('2') + fields.count('0')
        L.append([fields[0], g])
    inFile.close()

    L.sort(cmp = lambda x,y:cmp(x[1], y[1]))

    for x in L:
        ouFile.write(x[0] + '\t' + str(x[1]) + '\n')
    ouFile.write('Total\t' + str(n) + '\n')
    ouFile.close()

def check2(inF):
    ### mutated snp + indel
    L = []
    inFile = open(inF)
    ouFile = open(inF + '-checked2', 'w')
    head = inFile.readline().strip('\n').split()
    n = len(head[1:])
    for line in inFile:
        line = line.strip()
        fields = line.split()
        #g = fields.count('1') + fields.count('2') + fields.count('0')
        g = fields.count('1') + fields.count('2')
        L.append([fields[0], g])
    inFile.close()

    L.sort(cmp = lambda x,y:cmp(x[1], y[1]))

    for x in L:
        ouFile.write(x[0] + '\t' + str(x[1]) + '\n')
    #ouFile.write('Total\t' + str(n) + '\n')
    ouFile.close()

def check3(inF):
    ### mutated snp
    L = []
    inFile = open(inF)
    ouFile = open(inF + '-checked3', 'w')
    head = inFile.readline().strip('\n').split()
    n = len(head[1:])
    for line in inFile:
        line = line.strip()
        fields = line.split()
        g = 0
        for i in range(1, len(head)):
            if head[i].find('snp') != -1:
                if fields[i] == '1' or fields[i] == 2:
                    g += 1
        L.append([fields[0], g])
    inFile.close()

    L.sort(cmp = lambda x,y:cmp(x[1], y[1]))

    for x in L:
        ouFile.write(x[0] + '\t' + str(x[1]) + '\n')
    #ouFile.write('Total\t' + str(n) + '\n')
    ouFile.close()

#check2('1000Genome-465LCLs-Genotype')
check3('1000Genome-465LCLs-Genotype')

