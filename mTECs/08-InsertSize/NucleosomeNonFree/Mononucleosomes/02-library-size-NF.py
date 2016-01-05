import subprocess
CH = [str(x) for x in range(1, 20)] + ['X','Y']
Sample = ['Tspan8_positive_MHCII_high_rep1_Mono.bam','Tspan8_positive_MHCII_high_rep2_Mono.bam','Tspan8_negative_MHCII_high_rep1_Mono.bam','Tspan8_negative_MHCII_high_rep2_Mono.bam','Tspan8_positive_MHCII_low_rep1_Mono.bam','Tspan8_positive_MHCII_low_rep2_Mono.bam','Tspan8_negative_MHCII_low_rep1_Mono.bam','Tspan8_negative_MHCII_low_rep2_Mono.bam']
ouFile = open('mTECs-Sample-LibrarySize-Mono', 'w')
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
    
    

