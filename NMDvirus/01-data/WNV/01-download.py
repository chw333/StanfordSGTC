inFile = open('downloadFile.txt')
ouFile = open('01-download.sh', 'w')
for line in inFile:
    line = line.strip()
    ouFile.write('wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP%2FSRP015%2FSRP015670/'+line+'/'+line+'.sra\n')
inFile.close()
ouFile.close()
