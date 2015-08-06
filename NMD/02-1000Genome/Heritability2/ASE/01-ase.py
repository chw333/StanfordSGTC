inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample')
ouFile2 = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Exp.sh', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    num = fields[1]
    LS = [sample, num]
    for item in fields[2:]:
        L = []
        fds = item.split('|')
        for fd in fds:
            snp = fd.split(':')[0]
            ch = snp.split('_')[1]
            pos = snp.split('_')[2]
            f = 'tview-' + sample + '-' + snp
            ouFile2.write('samtools tview -d T -p chr%s:%s /mnt/larsix/projects/NMD/hansun/NMD/02-1000Genome/465LCLs/bam/%s*.bam $hg19 >bam-ase/%s\n'%(ch,pos,sample,f))
            L.append(fd)
        LS.append('|'.join(L))

inFile.close()
