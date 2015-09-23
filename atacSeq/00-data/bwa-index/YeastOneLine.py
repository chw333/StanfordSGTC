import sys
dict1=dict()
list1=list()

inFile1=open(sys.argv[1])
headi=-1
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        head=line
        headi+=1
        list1.append([head])
    else :
        list1[headi].append(line)

inFile1.close()


CH = {}
CH['I'] = 'chr1'
CH['II'] = 'chr2'
CH['III'] = 'chr3'
CH['IV'] = 'chr4'
CH['V'] = 'chr5'
CH['VI'] = 'chr6'
CH['VII'] = 'chr7'
CH['VIII'] = 'chr8'
CH['IX'] = 'chr9'
CH['X'] = 'chr10'
CH['XI'] = 'chr11'
CH['XII'] = 'chr12'
CH['XIII'] = 'chr13'
CH['XIV'] = 'chr14'
CH['XV'] = 'chr15'
CH['XVI'] = 'chr16'
CH['M'] = 'chrM'

ouFile1=open(sys.argv[1]+'.fa','w')
for item in list1 :
    if item[0].find('location=mitochondrion') != -1:
        ch = 'M'
    else:
        ch = item[0].split('chromosome=')[1].split(']')[0]

    ouFile1.write('>' + CH[ch] +'\n')
    ouFile1.write(''.join(item[1:])+'\n')
        

ouFile1.close()
