def sortN(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF + '.sorted', 'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')

            ch1 = fields1[2]
            query_start1 = int(fields1[7])
            query_end1 = int(fields1[8])
            subject_start1 = int(fields1[9])
            subject_end1 = int(fields1[10])

            ch2 = fields2[2]
            query_start2 = int(fields2[7])
            query_end2 = int(fields2[8])
            subject_start2 = int(fields2[9])
            subject_end2 = int(fields2[10])
    
            if (query_start1 + query_end1) <= (query_start2 + query_end2):
                #point = subject_end1
                k1 = ch1 + ':' + str(subject_end1) + ':' + ch2 + ':' + str(subject_start2)
                k2 = ch2 + ':' + str(subject_start2) + ':' + ch1 + ':' + str(subject_end1)  
            else:
                #point = subject_end2
                k1 = ch1 + ':' + str(subject_start1) + ':' + ch2 +':'+ str(subject_end2)
                k2 = ch2 +':'+ str(subject_end2) + ':' + ch1 + ':' + str(subject_start1) 
            #k = ch2 + ':' + str(point)
            if k1 not in D and k2 not in D:
                D.setdefault(k1, [])
                D[k1].append(line1)
                D[k1].append(line2)
            elif k1 in D:
                D.setdefault(k1, [])
                D[k1].append(line1)
                D[k1].append(line2)
            elif k2 in D:
                D.setdefault(k2, [])
                D[k2].append(line1)
                D[k2].append(line2)
        else:
            break
    d = D.items()
    d.sort(cmp = lambda x,y:cmp(len(x[1]), len(y[1])), reverse = True)
    for item in d:
        for i in range(0, len(item[1]),2):
            ouFile.write(item[0] + '\t' + str(len(item[1])/2) + '\t' + item[1][i] + '\n')
            ouFile.write(item[0] + '\t' + str(len(item[1])/2) + '\t' + item[1][i + 1] + '\n')

    inFile.close()
    ouFile.close()

sortN('SRR1258471-soft-filtered.fa.blated.filtered.seq.classified.gene')
sortN('SRR1258470-soft-filtered.fa.blated.filtered.seq.classified.gene')
