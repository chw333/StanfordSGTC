def format(inF):
    Samples = []
    inFile = open('1000Genome-462LCLs-Samples')
    for line in inFile:
        line = line.strip()
        Samples.append(line)
    inFile.close()

    D = {}
    inFile = open(inF)
    ouFile = open('1000Genome-462LCLs-Genotype', 'w')
    ouFile2 = open('1000Genome-462LCLs-Position', 'w')
    head = inFile.readline().strip()
    ouFile.write(head + '\n')
    for line in inFile:
        L = []
        line = line.strip()
        fields = line.split('\t')
        s = fields[0]
        for x in fields[1:]:
            if x == '1':
                L.append('1')
            elif x == '2':
                L.append('1')
            elif x == '0':
                L.append('0')
            else:
                print(x)
        D.setdefault(s, L)
    for sample in Samples:
        if sample in D:
            ouFile.write(sample + '\t' + '\t'.join(D[sample]) + '\n')
    

    hds = head.split('\t')
    for hd in hds[1:]:
        hs = hd.split('_')
        try:
            ouFile2.write('chr' + hs[-2] + '\t' + hs[-1] + '\n')
        except:
            print(hs)
            
    
    inFile.close()
    ouFile.close()
    ouFile2.close()


#format('1000Genome-465LCLs-Genotype')
#format('1000Genome-465LCLs-Genotype-Filt')
format('1000Genome-465LCLs-Genotype-FiltTrans-Ref-Trans')
