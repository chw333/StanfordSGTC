### DCM-LibrarySize 
s635a_lib =  64186128
cp1_lib =  72360066
cp2_lib =  75713112
READS_MIN = 100

inFile = open('DCM-GeneCountSymbol')
ouFile1 = open('DCM-GeneCountSymbol-S635A_CP1_up', 'w')
ouFile2 = open('DCM-GeneCountSymbol-S635A_CP1_down', 'w')
ouFile3 = open('DCM-GeneCountSymbol-S635A_CP2_up', 'w')
ouFile4 = open('DCM-GeneCountSymbol-S635A_CP2_down', 'w')
ouFile5 = open('DCM-GeneCountSymbol-CP1_CP2_up', 'w')
ouFile6 = open('DCM-GeneCountSymbol-CP2_CP2_down', 'w')

ouFile7 = open('DCM-GeneCountSymbol-S635A_CP1CP2_up', 'w')
ouFile8 = open('DCM-GeneCountSymbol-S635A_CP1CP2_down', 'w')

### expressed genes
ouFile9 = open('DCM-GeneCountSymbol-expressed', 'w')




head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene_name = fields[0]
    gene_id = fields[1]
    s635a = float(fields[2])
    cp1 = float(fields[3])
    cp2 = float(fields[4])

    ### s635a vs cp1
    if s635a >= READS_MIN and cp1 >= READS_MIN:
        fc = (s635a/s635a_lib)/(cp1/cp1_lib)
        if fc > 2:
            ouFile1.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp1) + '\t' + str(fc) + '\n')
        elif fc < 0.5:
            ouFile2.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp1) + '\t' + str(fc) + '\n')

    ### s635a vs cp2
    if s635a >= READS_MIN and cp2 >= READS_MIN:
        fc = (s635a/s635a_lib)/(cp2/cp2_lib)
        if fc > 2:
            ouFile3.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp2) + '\t' + str(fc) + '\n')
        elif fc < 0.5:
            ouFile4.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp2) + '\t' + str(fc) + '\n')

    ### cp1 vs cp2
    if cp1 >= READS_MIN and cp2 >= READS_MIN:
        fc = (cp1/cp1_lib)/(cp2/cp2_lib)
        if fc > 2:
            ouFile5.write(gene_name + '\t' + gene_id + '\t' + str(cp1) + '\t' + str(cp2) + '\t' + str(fc) + '\n')
        elif fc < 0.5:
            ouFile6.write(gene_name + '\t' + gene_id + '\t' + str(cp1) + '\t' + str(cp2) + '\t' + str(fc) + '\n')

    #s635a vs cp1, cp2
    if s635a >= READS_MIN and cp1 >= READS_MIN and cp2 >= READS_MIN:
        ouFile9.write(gene_name + '\n')
        fc1 = (s635a/s635a_lib)/(cp1/cp1_lib)
        fc2 = (s635a/s635a_lib)/(cp2/cp2_lib)
        if fc1 > 2 and fc2 > 2:
            ouFile7.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp1) + '\t' + str(cp2) + '\t' + str(fc1) + '\t' + str(fc2) + '\n')
        elif fc1 < 0.5 and fc2 < 0.5:
            ouFile8.write(gene_name + '\t' + gene_id + '\t' + str(s635a) + '\t' + str(cp1) + '\t' + str(cp2) + '\t' + str(fc1) + '\t' + str(fc2) + '\n')



inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()
ouFile5.close()
ouFile6.close()
ouFile7.close()
ouFile8.close()
ouFile9.close()
