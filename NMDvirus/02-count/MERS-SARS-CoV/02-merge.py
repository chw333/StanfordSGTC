Sample = ['MOCK_MRC5_1.count','MOCK_MRC5_2.count','MOCK_MRC5_3.count','MERS_MRC5lowMOI_24hr_1.count','MERS_MRC5lowMOI_24hr_2.count','MERS_MRC5lowMOI_24hr_3.count','MERS_MRC5lowMOI_48hr_1.count','MERS_MRC5lowMOI_48hr_2.count','MERS_MRC5lowMOI_48hr_3.count','MERS_MRC5HighMOI_24hr_1.count','MERS_MRC5HighMOI_24hr_2.count','MERS_MRC5HighMOI_24hr_3.count','MERS_MRC5HighMOI_48hr_1.count','MERS_MRC5HighMOI_48hr_2.count','MERS_MRC5HighMOI_48hr_3.count','SARS_MRC5lowMOI_24hr_1.count','SARS_MRC5lowMOI_24hr_2.count','SARS_MRC5lowMOI_24hr_3.count','SARS_MRC5lowMOI_48hr_2.count','SARS_MRC5lowMOI_48hr_3.count','SARS_MRC5HighMOI_24hr_1.count','SARS_MRC5HighMOI_24hr_2.count','SARS_MRC5HighMOI_24hr_3.count','SARS_MRC5HighMOI_48hr_2.count','SARS_MRC5HighMOI_48hr_3.count']

D = {}
for sample in Sample:
    G = []
    D.setdefault(sample, {})

    inFile = open(sample)
    for line in inFile:
        line = line.strip()
        if line.find('__') != 0:
            fields = line.split('\t')
            gene = fields[0]
            num = fields[1]
            D[sample][gene] = num
            G.append(gene)
    inFile.close()

ouFile = open('MERS_SARS-GeneCount', 'w')
ouFile.write('' + '\t' + '\t'.join([x.split('.count')[0] for x in Sample]) + '\n')

for gene in G:
    L = []
    for sample in Sample:
        L.append(D[sample][gene])
    ouFile.write(gene + '\t' + '\t'.join(L) + '\n')

ouFile.close()



