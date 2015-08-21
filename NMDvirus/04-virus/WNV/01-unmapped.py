import os
import subprocess

Fs = os.listdir('.')

for F in Fs:
    if F.find('.all.bam') != -1:
        ouFile = open(F.split('.all.bam')[0] + '-unmapped.fq', 'w')
        p = subprocess.Popen(['samtools','view', F], stdout=subprocess.PIPE)
        for line in p.stdout:
            line = line.strip()
            fields = line.split('\t')
            rd = fields[0]
            flag = fields[1]
            seq = fields[9]
            seqQ = fields[10]
            ### 0,16 mapped, 4 unmapped
            if flag == '4':
                if seq.find('N') == -1:
                    ouFile.write('@' + rd + '\n')
                    ouFile.write(seq + '\n')
                    ouFile.write('+' + rd + '\n')
                    ouFile.write(seqQ + '\n')


ouFile.close()
