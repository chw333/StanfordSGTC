import subprocess
inFile = open('WNV-Stopgain')
fa = '/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa'

ouF = 'WNV-Stopgain-tview'
ouFile = open(ouF, 'w')
ouFile.close()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    gene = fields[1]
    h = fields[9]
    ch = fields[4]
    pos = fields[5]
    
    if sample[-3:] == 'WNV':
        sample = fields[0]
        bam = sample + '.bam'

        ouFile = open(ouF, 'a')
        ouFile.write('>' + sample + '\t' + gene + '\t' + ch + ':' + pos  + '\t' + fields[9]  + '\t' +  '\t'.join(fields[7:9])+ '\t' + '\n')
        ouFile.close()
        subprocess.call('samtools tview -d T -p %s:%s %s %s >>%s'%(ch, int(pos)-40, bam, fa, ouF), shell=True)

        sample = fields[0].split('-WNV')[0] + '-Mock'
        bam = sample + '.bam'
        ouFile = open(ouF, 'a')
        ouFile.write('>' + sample + '\t' + gene + '\t' + ch + ':' + pos  + '\t' + 'Unknown' + '\t' +  '\t'.join(fields[7:9]) + '\t' + '\n')
        ouFile.close()
        subprocess.call('samtools tview -d T -p %s:%s %s %s >>%s'%(ch, int(pos)-40, bam, fa, ouF), shell=True)

    elif sample[-4:] == 'Mock':
        sample = fields[0].split('-Mock')[0] + '-WNV'
        bam = sample + '.bam'
        ouFile = open(ouF, 'a')
        ouFile.write('>' + sample + '\t' + gene + '\t' + ch + ':' + pos  + '\t' + 'Unknown' + '\t' +  '\t'.join(fields[7:9]) + '\t' + '\n')
        ouFile.close()
        subprocess.call('samtools tview -d T -p %s:%s %s %s >>%s'%(ch, int(pos)-40, bam, fa, ouF), shell=True)

        sample = fields[0]
        bam = sample + '.bam'
        ouFile = open(ouF, 'a')
        ouFile.write('>' + sample + '\t' + gene + '\t' + ch + ':' + pos  + '\t' + fields[9] + '\t' +  '\t'.join(fields[7:9]) + '\t' + '\n')
        ouFile.close()
        subprocess.call('samtools tview -d T -p %s:%s %s %s >>%s'%(ch, int(pos)-40, bam, fa, ouF), shell=True)





inFile.close()
