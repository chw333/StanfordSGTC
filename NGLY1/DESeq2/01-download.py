inFile = open('GEO-File')
ouFile = open('GEO-File.sh', 'w')
for line in inFile:
    line = line.strip()
    ouFile.write('wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByStudy/sra/SRP%2FSRP033%2FSRP033351/'+line+'/'+line + '.sra\n')

inFile.close()
ouFile.close()
