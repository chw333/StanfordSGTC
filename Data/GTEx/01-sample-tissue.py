def sample2tissue(inF, ouF):
    T = {}
    inFile = open(inF)
    ouFile = open(ouF, 'w')
    head = inFile.readline()
    for line in inFile:
        fields = line.split('\t')
        sample = fields[0]
        tissue = fields[6]
        ouFile.write(sample + '\t' + tissue + '\n')
        T[tissue] = 1
    inFile.close()
    ouFile.close()

    for k in T:
        print(k)

sample2tissue('GTEx_Data_V6_Annotations_SampleAttributesDS.txt', 'GTEx_Sample2Tissue')
