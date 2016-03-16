Qsig = 0.2
def sig(gene, inF):
    inFile = open(inF)
    head = inFile.readline().strip().split('\t')
    ouFile = open(inF+'_'+gene, 'w')
    ouFile.write('\t'.join(['Gene','Compound','Corr_coeff','Pval_left','Qval_left','Pval_right', 'Qval_right'])+'\n')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0] == gene:
            for i in range(1, len(head), 5):
                ### Qval sig
                if float(fields[i + 2]) < Qsig or float(fields[i + 4]) < Qsig:
                    ouFile.write(gene + '\t' +head[i].split('_')[0]+ '\t'+'\t'.join(fields[i:i+5]) + '\n')
    inFile.close()
    ouFile.close()

sig('RBM20', 'PRISM_GeneExpression_Compound_Matrix')
sig('RBM20', 'PRISM_CopyNumber_Compound_Matrix')

sig('NGLY1', 'PRISM_GeneExpression_Compound_Matrix')
sig('NGLY1', 'PRISM_CopyNumber_Compound_Matrix')
