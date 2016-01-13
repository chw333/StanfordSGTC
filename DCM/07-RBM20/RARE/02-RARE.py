import re 
inFile = open('RBM20.fasta')
head = inFile.readline()
seq = inFile.readline().strip()
inFile.close()

#p1 = 'GGTCA'
#p2 = 'GGTGA'

p1 = 'GGTGA'
p2 = 'GGTCA'
s1 = [x.start() for x in re.finditer(p1, seq)]
s2 = [x.start() for x in re.finditer(p2, seq)]
s = list(set(s1 + s2))
s.sort()
for i in range(1, len(s) - 1):
    if 4 <= s[i] - s[i-1] - len(p1) <= 6:
        print(s[i-1])
