def exp(inF):
    inFile = open(inF)
    ouFile = open(inF+'-Formated', 'w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if len(fields) > 2:
            sample = fields[0]
            num = fields[1]
            LS = []
            for item in fields[2:]:
                ims = item.split('+')
                stopgain = ims[0]
                gt = stopgain.split(':')[-3]
                ase = stopgain.split(':')[-2:]
                if gt == '0|1':
                    L = [stopgain+'#'+ase[0]+':'+ase[1]]
                    for im in ims[1:]:
                        gt = im.split(':')[-3]
                        ase = im.split(':')[-2:]
                        if gt == '0|1':
                            L.append(im + '#' + ase[0] + ':' + ase[1])
                        elif gt == '1|0':
                            L.append(im + '#' + ase[1] + ':' + ase[0])
                        else:
                            print('Warning')
                elif gt == '1|0':
                    L = [stopgain+'#'+ase[0]+':'+ase[1]]
                    for im in ims[1:]:
                        gt = im.split(':')[-3]
                        ase = im.split(':')[-2:]
                        if gt == '1|0':
                            L.append(im + '#' + ase[0] + ':' + ase[1])
                        elif gt == '0|1':
                            L.append(im + '#' + ase[1] + ':' + ase[0])
                        else:
                            print('Warning')
                LS.append('+'.join(L))
            ouFile.write(sample + '\t' + num + '\t' + '\t'.join(LS) + '\n')

                
                





    inFile.close()
    ouFile.close()


exp('G462-Sample-Stopgain-Linkage-TranscriptLevel-Sample-Genotype-Expressed')
