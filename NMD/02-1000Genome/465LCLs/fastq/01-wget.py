import os
def bam():
    L = []
    Fs = os.listdir('../bam')
    for F in Fs:
        if F[-4:]=='.bam':
            fq = F[0:-4]
            L.append(fq + '_1')
            L.append(fq + '_2')
    return L
fq = bam()

inFile = open('ERP001942.text')
ouFile = open('ERP001942.sh', 'w')
head = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    fastq = fields[12].split(';')
    fq0 = fastq[0].split('/')[-1].split('.fastq.gz')[0]
    fq1 = fastq[1].split('/')[-1].split('.fastq.gz')[0]
    if fq0 in fq:
        ouFile.write('wget ' + fastq[0] + '\n')
    if fq1 in fq:
        ouFile.write('wget ' + fastq[1] + '\n')

inFile.close()
ouFile.close()
