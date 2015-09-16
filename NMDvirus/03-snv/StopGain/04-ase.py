import os
import re
def ASE(inF):
    D = {}
    DIR = inF
    Fs = os.listdir(DIR)
    for F in Fs:
        if F.find('.flt.vcf') != -1:
            sample = F.split('.flt.vcf')[0]
            inFile = open(DIR + '/' + F)
            for line in inFile:
                line = line.strip()
                if line.find('##') != 0:
                    try:
                        fields = line.split('\t')
                        ch = fields[0]
                        pos = fields[1]
                        ref = fields[3]
                        alt = fields[4]
                        info = fields[7]
                        s=re.search('DP4=(\d+),(\d+),(\d+),(\d+);',info)
                        if s:
                            ref_num = int(s.group(1)) + int(s.group(2))
                            alt_num = int(s.group(3)) + int(s.group(4))
                            k = ':'.join([sample, ch,pos,ref,alt])
                            D[k] = [ref_num, alt_num]
                    except:
                        pass
            inFile.close()
    return(D)


def num(inF, inF2):
    D = ASE(inF2)
    inFile = open(inF)
    ouFile = open(inF + '-ase', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        sample = fields[0]
        ch = fields[4]
        pos = fields[5]
        ref = fields[7]
        alt = fields[8]
        k = ':'.join([sample,ch,pos,ref,alt])
        if k in D:
            ouFile.write(line + '\t' + str(D[k][0]) + '\t' + str(D[k][1]) + '\n')
    inFile.close()
    ouFile.close()

#num('RSV-Stopgain-SNV-het', '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/RSV')
#num('HCV-Stopgain-SNV-het' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HCV')
#num('HIV-Stopgain-SNV-het' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HIV1')
#num('HSV-Stopgain-SNV-het' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HSV1')
#num('KHSV-Stopgain-SNV-het' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/KHSV')
#num('WNV-Stopgain-SNV-het' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/WNV')

num('RSV-Stopgain-SNV-hom', '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/RSV')
num('HCV-Stopgain-SNV-hom' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HCV')
num('HIV-Stopgain-SNV-hom' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HIV1')
num('HSV-Stopgain-SNV-hom' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/HSV1')
num('KHSV-Stopgain-SNV-hom' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/KHSV')
num('WNV-Stopgain-SNV-hom' , '/mnt/larsix/projects/NMD/hansun/NMDvirus/03-snv/WNV')


