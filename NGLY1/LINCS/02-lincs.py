'''
In practice, we have found the score_best4 metric to be a reasonable compromise between too many and too few cell types over which to summarize.
The scores in these columns range from -100 (complete anti-connection) to 100 (complete connection). Positive values indicate that the pertubation gave a similar signature to the query, and negative values indicate that the pertubation gave a signature opposite to that of the query. -666 means that no information is available. We have generally found that scores with a magnitude of greater than 90 correspond to significant connections.
'''

def lincs(inF):
    D = {}
    inFile = open(inF)
    ouFile1 = open(inF.split('.txt')[0] + '_drug_connection', 'w')
    ouFile2 = open(inF.split('.txt')[0] + '_drug_anti-connection', 'w')
    ouFile3 = open(inF.split('.txt')[0] + '_geneKnockdown_connection', 'w')
    ouFile4 = open(inF.split('.txt')[0] + '_geneKnockdown_anti-connection', 'w')
    ouFile5 = open(inF.split('.txt')[0] + '_geneOverexpress_connection', 'w')
    ouFile6 = open(inF.split('.txt')[0] + '_geneOverexpress_anti-connection', 'w')
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        pert_name = fields[2]
        pert_type = fields[3]
        score2 = float(fields[6])
        score4 = float(fields[7])
        score6 = float(fields[8])
        is_expressed_4 = int(fields[9])
        is_expressed_6 = int(fields[10])
        if is_expressed_4 == 0 or is_expressed_6 == 0:
            pass
        elif score4 != '-666':
            D.setdefault(pert_type, [])
            D[pert_type].append([pert_name, score4])
    inFile.close()
    drug = D['trt_cp']
    ko = D['trt_sh.cgs']
    oe = D['trt_oe']

    drug.sort(cmp = lambda x,y: cmp(x[1], y[1]))
    ko.sort(cmp = lambda x,y: cmp(x[1], y[1]))
    oe.sort(cmp = lambda x,y: cmp(x[1], y[1]))

    for i in range(len(drug)):
        if drug[i][1] < -90:
            ouFile2.write(drug[i][0] + '\t' + str(drug[i][1]) + '\n')

    for i in range(len(drug)-1,-1,-1):
        if drug[i][1] > 90:
            ouFile1.write(drug[i][0] + '\t' + str(drug[i][1]) + '\n')

    for i in range(len(ko)):
        if ko[i][1] < -90:
            ouFile3.write(ko[i][0] + '\t' + str(ko[i][1]) + '\n')

    for i in range(len(ko)-1,-1,-1):
        if ko[i][1] > 90:
            ouFile4.write(ko[i][0] + '\t' + str(ko[i][1]) + '\n')

    for i in range(len(oe)):
        if oe[i][1] < -90:
            ouFile6.write(oe[i][0] + '\t' + str(oe[i][1]) + '\n')

    for i in range(len(oe)-1,-1,-1):
        if oe[i][1] > 90:
            ouFile5.write(oe[i][0] + '\t' + str(oe[i][1]) + '\n')



lincs('result_UPTAG_summly_n7503.txt')
