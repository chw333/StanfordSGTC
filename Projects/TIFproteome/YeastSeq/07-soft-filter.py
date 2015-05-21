import re
def soft(inF):
    inFile = open(inF)
    ouFile = open(inF + '-filtered', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        soft = fields[5]
        s = re.search('(\d+)S', soft)
        if s:
            sn = int(s.group(1))
            if sn >= 30:
                ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

#soft('SRR1258470-soft')
soft('SRR1258471-soft')
