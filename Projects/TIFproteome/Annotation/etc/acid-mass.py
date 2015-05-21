D = {}
inFile = open('Acid-Mass')
for line in inFile:
    line = line.strip()
    fields = line.split()
    print(fields)
    mass = float(fields[-1])
    D.setdefault(mass, 0)
    D[mass] += 1
inFile.close()
for k in D:
    print(str(k) + '\t' + str(D[k]))
