import sys
L=[]

inFile1=open(sys.argv[1])
headi=-1
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        head=line
        headi+=1
        L.append([head])
    else :
        L[headi].append(line)

inFile1.close()

ouFile1=open(sys.argv[1].split('.fasta')[0]+'.fa','w')

for item in L :
    ouFile1.write(item[0]+'\n')
    ouFile1.write(''.join(item[1:])+'\n')

ouFile1.close()
