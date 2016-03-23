#gene = ['RBM20', 'chr10', 112404154, 112599229, '+']
#gene = ['EGR1','chr5',137801180,137805004, '+' ]
gene = ['ZBTB7A','chr19',4045215,4066816, '-']
def tf2(gene):
    D = {}
    inFile = open(gene[0]+'_GRCh37_AnnotatedFeatures')
    ouFile2 = open(gene[0]+'_GRCh37_AnnotatedFeatures_Promoter_TF', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[2].find('TF_binding') != -1:
            if gene[4] == '+':
                if gene[2]-1000 < int(fields[3]) <  gene[2] or gene[2]-1000 < int(fields[4]) <  gene[2]:
                    tf = fields[8].split(';')[0].split('Name=')[1]
                    D.setdefault(tf, [])
                    D[tf].append(line)
            else:
                if gene[3] < int(fields[3]) <  gene[3]+1000 or gene[3] < int(fields[4]) <  gene[3] + 1000:
                    tf = fields[8].split(';')[0].split('Name=')[1]
                    D.setdefault(tf, [])
                    D[tf].append(line)
    inFile.close()
    for k in D:
        ouFile2.write(k + '\t' + '\t'.join(D[k]) + '\n')
    
    ouFile2.close()


def tf1(gene):
    D = {}
    inFile = open(gene[0] + '_GRCh37_AnnotatedFeatures')
    ouFile = open(gene[0] + '_GRCh37_AnnotatedFeatures_TF', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[2].find('TF_binding') != -1:
            if gene[4] == '+':
                if gene[2] -1000 < int(fields[3]) <  gene[3] + 1000 or gene[2] - 1000 < int(fields[4]) <  gene[3] + 1000:
                    tf = fields[8].split(';')[0].split('Name=')[1]
                    D.setdefault(tf, [])
                    D[tf].append(line)
            else:
                if gene[2] -1000 < int(fields[3]) <  gene[3] + 1000 or gene[2] - 1000 < int(fields[4]) <  gene[3] + 1000:
                    tf = fields[8].split(';')[0].split('Name=')[1]
                    D.setdefault(tf, [])
                    D[tf].append(line)
    inFile.close()
    for k in D:
        ouFile.write(k + '\t' + '\t'.join(D[k]) + '\n')

    ouFile.close()

tf1(gene)
tf2(gene)

