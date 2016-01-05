import subprocess
CH = ['chr'+str(x) for x in range(1, 20)] + ['chrX','chrY']
Sample=['K562_WT_Recalibrated.bam','K562_K8_Recalibrated.bam','K562_K15_Recalibrated.bam','K562_K20_Recalibrated.bam']

ouFile = open('Sample-LibrarySize', 'w')
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
    #ouFile.write(F.split('.bam')[0] + '\t' + str(total_num) + '\t' + '%.4f'%rt + '\n')
    ouFile.write(F.split('.bam')[0] + '\t' + str(total_num) + '\n')
ouFile.close()
    
    

