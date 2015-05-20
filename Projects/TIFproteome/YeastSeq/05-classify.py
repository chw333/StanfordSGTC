import sys
def classify(inF):
    inFile = open(inF)
    ouF = inF.split('.sam')[0]
    ouFile1 = open(ouF + '-soft','w')
    ouFile2 = open(ouF + '-unmapped','w')
    for n in range(18):
        inFile.readline()
    for line in inFile:
        fields = line.split('\t')
        if int(fields[1]) == 4:
            ouFile2.write(line)
        else:
            if fields[5].find('S')!=-1:
                ouFile1.write(line)
    inFile.close()
    ouFile1.close()
    ouFile2.close()


#classify('SRR1258470.sam')
#classify('SRR1258471.sam')
#classify('SRR1258533.sam')
#classify('SRR1258534.sam')
#classify('SRR1258535.sam')
#classify('SRR1258536.sam')
#classify('SRR1258537.sam')
#classify('SRR1258538.sam')
#classify('SRR1258539.sam')
classify('SRR1258540.sam')
classify('SRR1258541.sam')
classify('SRR1258542.sam')
classify('SRR1258543.sam')
classify('SRR1258544.sam')
