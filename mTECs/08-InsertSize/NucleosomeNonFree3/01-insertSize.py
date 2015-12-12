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
                if  int(fields[8]) > 180 or int(fields[8]) < -180:
                    ouFile.write(line)
        ouFile.close()
        p = subprocess.call(['samtools','view', '-b', ouF_Name, '-o', ouF_Name.split('_HQ_RD.sam')[0]+'_NS3.bam'])
        os.remove(ouF_Name)
