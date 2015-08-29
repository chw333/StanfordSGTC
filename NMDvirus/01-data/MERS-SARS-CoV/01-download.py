### /sra/sra-instant/reads/ByRun/sra/{SRR|ERR|DRR}/<first 6 characters of accession>/<accession>/<accession>.sra
### ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR119/SRR1192353/SRR1192353.sra
### or use fastq-dump [--split-files] SRR
import subprocess

inFile = open('SampleInfo')
ouFile = open('SampleInfo.txt', 'w')
ouFile2 = open('01-download.sh', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gsm = fields[0]
    if gsm[0] != '#':
        L = []
        sp = subprocess.Popen('esearch -db gds -query "%s"|efetch -format docsum|xtract -pattern ExtRelation -element TargetObject'%gsm, shell=True, stdout=subprocess.PIPE)
        
        for item in sp.stdout:
            item = item.strip()
            if item.find('SRX') == 0:
                sp2 = subprocess.Popen('esearch -db sra -query "%s" | efetch -format docsum | xtract  -element Runs'%item, shell=True, stdout=subprocess.PIPE)
                for im in sp2.stdout:
                    im = im.strip().split('"')
                    srr = im[1]
                    L.append(srr)
        ouFile.write('\t'.join(fields) + '\t' + '\t'.join(L) + '\n')

        for x in L:
            ouFile2.write('fastq-dump --split-files ' + x + '\n')

inFile.close()
ouFile.close()
ouFile2.close()
