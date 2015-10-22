RegionLen = 100
nSample = 4
def data_structure(inF):
    D = {}
    L = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        ch = fields[0]
        chLen = int(fields[1])
        for n in range(chLen/RegionLen + 1):
            if n == 0:
                start = RegionLen * n + 1
            else:
                start = RegionLen * n
            if (n+1)*RegionLen >= chLen:
                end = chLen
            else:
                end = (n+1)*RegionLen - 1
            k = ':'.join([ch, str(start), str(end)])
            D[k] = [0]*nSample
            L.append(k)
    inFile.close()
    return(D, L)
D, L = data_structure('test')

print(D)

