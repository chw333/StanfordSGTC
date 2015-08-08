S1 = set()
inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    S1.add(fields[0])
inFile.close()
print(len(S1))

import os
S2 = set()
Fs = os.listdir('/mnt/larsix/projects/NMD/hansun/NMD/02-1000Genome/465LCLs/bam')
for F in Fs:
    if F[-4:] == '.bam':
        S2.add(F.split('.')[0])
print(len(S2))

print(S1 - S2)
