D = {}
inFile = open('RBM20_RCh37_AnnotatedFeatures')
#ouFile = open('RBM20_RCh37_AnnotatedFeatures_TF', 'w')
ouFile2 = open('RBM20_RCh37_AnnotatedFeatures_Promoter_TF', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[2].find('TF_binding') != -1:
        if 112403155 < int(fields[3]) <  112404155 or 112403155 < int(fields[4]) <  112404155:
        #if 112404155 - 2000 < int(fields[3]) <  112404155 + 1000 or 112404155 - 2000 < int(fields[4]) <  112404155 + 1000:
            tf = fields[8].split(';')[0].split('Name=')[1]
            D.setdefault(tf, [])
            D[tf].append(line)
inFile.close()
for k in D:
    ouFile2.write(k + '\t' + '\t'.join(D[k]) + '\n')
    #ouFile.write(k + '\t' + '\t'.join(D[k]) + '\n')

#ouFile.close()
ouFile2.close()

