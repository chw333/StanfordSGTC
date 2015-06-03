def plot(inF):
    L = []
    inFile =  open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        L.append(int(fields[-1]))
    inFile.close()

