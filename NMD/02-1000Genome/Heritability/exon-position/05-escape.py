inFile = open('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed-Formated-Sum-Escape')
L0 = []
L1 = []

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    for item in fields[1:]:
        v0 = int(item.split('&')[1].split(':')[0])
        v1 = int(item.split('&')[1].split(':')[1])
        if item.find('unEscaped') != -1: 
            L0.append((v1+1.0)/(v0+1.0))
        else:
            L1.append((v1+1.0)/(v0+1.0))
print(L0)
print(L1)

inFile.close()
