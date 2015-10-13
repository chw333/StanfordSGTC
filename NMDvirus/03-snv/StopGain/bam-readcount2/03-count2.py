D = {}
L = []
S = []
def count(inF):
    S.append(inF)
    D.setdefault(inF, {})
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = fields[0] + '\t' + fields[1]
        ref = fields[2]
        if inF == 'Mock-rep1.bam.Count':
            L.append(k)
        A = int(fields[5].split(':')[1])
        C = int(fields[6].split(':')[1])
        G = int(fields[7].split(':')[1])
        T = int(fields[8].split(':')[1])
        if ref == 'A':
            ref_num = A
            ALT = [C, G, T]
            alt_num = sorted(ALT)[-1]
        elif ref == 'C':
            ref_num = C
            ALT = [A, G, T]
            alt_num = sorted(ALT)[-1]
        elif ref == 'G':
            ref_num = G
            ALT = [A, C, T]
            alt_num = sorted(ALT)[-1]
        elif ref == 'T':
            ref_num = T
            ALT = [A, C, G]
            alt_num = sorted(ALT)[-1]
        #D[inF][k] = [ref_num, alt_num]
        D[inF][k] = str(ref_num) + ':' + str(alt_num) + ':' + str((alt_num + 1.0) / (ref_num + 1.0))
    inFile.close()

count('Mock-rep1.bam.Count')
count('Mock-rep2.bam.Count')
count('RSV_M3-rep1.bam.Count')
count('RSV_M3-rep2.bam.Count')

G = {}
inFile = open('RSV2-Stopgain-SNV')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    G[fields[4] + '\t' + fields[5]] = fields[1]
inFile.close()


ouFile = open('RSV2-Stopgain-SNV-ReadCount', 'w')
for k in L:
    V = []
    for s in S:
        V.append(str(D[s].get(k, -1)))
    ouFile.write(G[k] + '\t' + k + '\t' + '\t'.join(V) + '\n')
        
ouFile.close()
