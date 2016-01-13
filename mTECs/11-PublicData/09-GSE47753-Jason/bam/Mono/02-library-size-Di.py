import subprocess
CH = ['chr'+str(x) for x in range(1, 23)] + ['chrX','chrY']
Sample = ['GM12878_50k_Rep1_Mono.bam','GM12878_50k_Rep2_Mono.bam','GM12878_50k_Rep3_Mono.bam','GM12878_50k_Rep4_Mono.bam']
ouFile = open('GM12878-LibrarySize-Mono', 'w')
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
    ouFile.write(F.split('_Mono.bam')[0] + '\t' + str(total_num) + '\t' + '%.4f'%rt + '\n')
ouFile.close()
    
    

