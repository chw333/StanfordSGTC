import os
import subprocess

Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.bam':
        ouF_Name = F.split('.bam')[0] + '.sam'
        ouFile = open(ouF_Name, 'w')
        p = subprocess.Popen(['samtools','view', '-h', F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stdout:
            if line[0] == '@':
                ouFile.write(line)
            else:
                fields = line.split('\t')
                if int(fields[8]) > 180:
                    TLEN = int(fields[8])
                    cigar = str(TLEN) + 'M'
                    seq = 'N'*TLEN
                    seqQ = 'B'*TLEN
                    
                    ouFile.write('\t'.join(fields[0:5] + [cigar] + fields[6:9] + [seq, seqQ] + fields[11:]))
        ouFile.close()
        p = subprocess.call(['samtools','view', '-b', ouF_Name, '-o', ouF_Name.split('.sam')[0]+'_NS.bam'])
        os.remove(ouF_Name)
