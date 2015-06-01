#!/usr/bin/env python
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

ouFile1=open(sys.argv[1].split('.fasta')[0]+'.fa','w')

for item in list1 :
    ouFile1.write(item[0]+'\n')
    ouFile1.write(''.join(item[1:])+'\n')

ouFile1.close()
