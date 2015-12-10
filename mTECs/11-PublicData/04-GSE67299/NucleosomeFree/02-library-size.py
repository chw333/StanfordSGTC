import subprocess
CH = [str(x) for x in range(1, 20)] + ['X','Y']
Sample = ['SRR1930167_HQ60_RD.bam', 'SRR1930169_HQ60_RD.bam', 'SRR1930171_HQ60_RD.bam', 'SRR1930173_HQ60_RD.bam', 'SRR1930167_NF.bam', 'SRR1930169_NF.bam', 'SRR1930171_NF.bam', 'SRR1930173_NF.bam', 'SRR1930167_NF2.bam', 'SRR1930169_NF2.bam', 'SRR1930171_NF2.bam', 'SRR1930173_NF2.bam']
ouFile = open('mTECs-Sample-LibrarySize', 'w')
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
    
    

