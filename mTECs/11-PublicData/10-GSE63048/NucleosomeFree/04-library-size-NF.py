import subprocess
CH = [str(x) for x in range(1, 20)] + ['X','Y']

Sample = ['P10.5_Morc1_het_Rep1_NF.bam','P10.5_Morc1_KO_Rep1_NF.bam','E16.5_Morc1_het_Rep1_NF.bam','E16.5_Morc1_KO_Rep1_NF.bam']
ouFile = open('Mouse-Sample-LibrarySize-NF', 'w')
for F in Sample:
    p = subprocess.Popen(['samtools','idxstats',F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    total_num = 0
    for line in p.stdout:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[0]
        ch_num = int(fields[2])
        rt = total_num/20000000.0
        if ch in CH:
            total_num += ch_num
    #ouFile.write(F.split('_NF.bam')[0] + '\t' + str(total_num) + '\t' + '%.4f'%rt + '\n')
    ouFile.write(F.split('_NF.bam')[0] + '\t' + str(total_num) + '\n')
ouFile.close()
    
    

