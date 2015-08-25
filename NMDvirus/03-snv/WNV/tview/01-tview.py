import subprocess
inFile = open('WNV-Stopgain')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    sample = fields[0]
    bam = 
    gene = fields[1]
    h = fields[9]
    ch = fields[4]
    pos = fields[5]
    subprocess(['samtools','tview','-d','T','-p',ch+':'+pos,'','',''])




inFile.close()
