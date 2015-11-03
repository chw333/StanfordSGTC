import os
import subprocess

Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.bam':
        ouFile = open(F.split('_HQ.bam')[0] + '.ReadInfo', 'w')
        D = {}
        L = []
        p = subprocess.Popen(['samtools','view', F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stdout:
            line = line.strip()
            fields = line.split('\t')
            name = fields[0]
            ch = fields[2]
            pos = fields[3]
            read = fields[9]
            TLen = fields[8]
            read_len = str(len(read))
            D.setdefault(name, [])
            D[name].append([ch, pos, read_len, TLen, read])
            #D[name].append([ch, pos, read_len, TLen])

        for name in D:
            if len(D[name]) == 2:
                ouFile.write(name + '\t' + '\t'.join(D[name][0]) + '\t' + '\t'.join(D[name][1]) + '\n')
        ouFile.close()
    



