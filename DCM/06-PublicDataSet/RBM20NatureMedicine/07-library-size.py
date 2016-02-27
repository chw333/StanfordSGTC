import subprocess
CH = [str(x) for x in range(1, 23)] + ['X','Y']
Sample = ['S635A.bam','CP1.bam','CP2.bam']
ouFile = open('DCM-LibrarySize', 'w')
for F in Sample:
    p = subprocess.Popen(['samtools','idxstats',F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    total_num = 0
    for line in p.stdout:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[0]
        ch_num = int(fields[2])
        rt = total_num/50000000.0
        if ch in CH:
            total_num += ch_num
    ouFile.write(F.split('_HQ.bam')[0] + '\t' + str(total_num) + '\t' + '%.4f'%rt + '\n')
ouFile.close()
    
    

