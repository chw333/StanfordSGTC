import subprocess
F='Tspan8_negative_MHCII_high_rep1.bam'
ouFile1 = open(F + '19.awk', 'w')
ouFile2 = open(F + '20.awk', 'w')
ouFile3 = open(F + '34.awk', 'w')
ouFile4 = open(F + '35.awk', 'w')
p = subprocess.Popen(['samtools','view', F], stdout=subprocess.PIPE)
for line in p.stdout:
    fields = line.split('\t')
    if fields[8] == '19':
        ouFile1.write(line)
    elif fields[8] == '20':
        ouFile2.write(line)
    elif fields[8] == '34':
        ouFile3.write(line)
    elif fields[8] == '35':
        ouFile4.write(line)

ouFile1.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()
