def mkfa(inF):
    inFile = open(inF)
    ouFile = open(inF + '.fa', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        seq = fields[9]
        name = fields[0]
        ouFile.write('>' + name + '\n')
        ouFile.write(seq + '\n')
    inFile.close()
    ouFile.close()

#mkfa('SRR1258470-unmapped')
#mkfa('SRR1258471-unmapped')
#mkfa('SRR1258533-unmapped')
#mkfa('SRR1258534-unmapped')
#mkfa('SRR1258535-unmapped')
#mkfa('SRR1258536-unmapped')
#mkfa('SRR1258537-unmapped')
#mkfa('SRR1258538-unmapped')
#mkfa('SRR1258539-unmapped')
#mkfa('SRR1258540-unmapped')
#mkfa('SRR1258541-unmapped')
#mkfa('SRR1258542-unmapped')
#mkfa('SRR1258543-unmapped')
#mkfa('SRR1258544-unmapped')
#mkfa('SRR1258470-soft-filtered')
mkfa('SRR1258471-soft-filtered')
