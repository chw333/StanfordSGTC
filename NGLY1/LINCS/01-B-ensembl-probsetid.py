def conflict(inF1, inF2, inF3):
    D = {}
    inFile = open(inF3)
    for line in inFile:
        line = line.strip()
        x = line.split("'")[1]
        D[x] = 1
    inFile.close()

    inFile = open(inF1)
    ouFile = open(inF1.split('.grp')[0] + '.nonconflict.grp', 'w')
    for line in inFile:
        line = line.strip()
        if line not in D:
            ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

    inFile = open(inF2)
    ouFile = open(inF2.split('.grp')[0] + '.nonconflict.grp', 'w')
    for line in inFile:
        line = line.strip()
        if line not in D:
            ouFile.write(line + '\n')
    inFile.close()
    ouFile.close()

    
conflict('de_CP1-B_MCP1-B.sig.up.txt-ProbSetID.grp', 'de_CP1-B_MCP1-B.sig.down.txt-ProbSetID.grp', 'de_CP1-B_MCP1-B_conflict')
conflict('de_CP3-B_Ctrl-B.sig.up.txt-ProbSetID.grp', 'de_CP3-B_Ctrl-B.sig.down.txt-ProbSetID.grp', 'de_CP3-B_Ctrl-B_conflict')
