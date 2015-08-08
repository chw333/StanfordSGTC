import os

DIR = '/mnt/larsix/projects/NMD/hansun/NMD/02-1000Genome/465LCLs'
Fs = os.listdir(DIR)
D = {}
for F in Fs:
    if F[-4:] == '.vcf':
        inFile = open(DIR + '/' + F)
        for line in inFile:
            line = line.strip()
            if line.find('##') == 0:
                pass
            elif line.find('#CHROM') == 0:
                head = line.split('\t')
            else:
                fields = line.split('\t')
                snp = fields[2]
                if len(head) == len(fields):
                    for i in range(9,len(head)):
                        k = head[i] + ':' + snp
                        D[k] = fields[i]
        inFile.close()

#inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated')
inFile = open('x')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    for item in fields[2:]:
        fds = item.split('+')
        for fd in fds:
            ims = fd.split(':')
            snp = ims[0]
            if snp.find('#') != -1:
                snp = snp.split('#')[1]
            g = ims[6]
            k = sample + ':'  + snp
            if D[k] != g:
                print(sample + ':' + snp)
                print(g)

inFile.close()
