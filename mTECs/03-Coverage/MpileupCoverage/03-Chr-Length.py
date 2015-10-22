import subprocess
CH = [str(x) for x in range(1, 20)] + ['X','Y','MT']
D = {}
ouFile = open('Mouse-Chr-Length', 'w')
F = 'Tspan8_negative_MHCII_high_rep1_HQ.bam'
p = subprocess.Popen(['samtools','idxstats',F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in p.stdout:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    ch_len = int(fields[1])
    D[ch] = ch_len
for ch in CH:
    ouFile.write(ch + '\t' + str(D[ch]) + '\n')
ouFile.close()
    
    

