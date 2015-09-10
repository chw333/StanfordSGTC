import os
ouFile = open('01-format.sh', 'w')
Fs = os.listdir('.')
for F in Fs:
    if F[-4:] == '.vcf':
        anno = F.split('.vcf')[0] + '.anno'
        ouFile.write('convert2annovar.pl -format vcf4 %s -outfile %s\n'%(F,anno))
ouFile.close()

