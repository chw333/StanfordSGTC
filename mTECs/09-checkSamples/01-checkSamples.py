import os
import subprocess

D = {}
Fs = os.listdir('.')
for F in Fs:
    if F[-6:] == '.fastq':
        inFile = open(F)
        while True:
            line1 = inFile.readline()
            line2 = inFile.readline()
            line3 = inFile.readline()
            line4 = inFile.readline()
            if line1:
                name = line1.split()[0][1:]
                D[name] = F
            else:
                break
        inFile.close()

D2 = {}
for F in Fs:
    if F[-4:] == '.bam':
        p = subprocess.Popen(['samtools','view', F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stdout:
            fields = line.split('\t')
            name = fields[0]
            D2.setdefault(F, set())
            if name in D:
                D2[F].add(D[name])
ouFile = open('mTECs-checkSamples', 'w')
for k in D2:
    ouFile.write(k + '\t' + '\t'.join(D2[k]) + '\n')
ouFile.close()
