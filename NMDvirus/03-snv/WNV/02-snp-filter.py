import os
Fs = os.listdir('.')
for F in Fs:
    if F[-8:] == '.raw.vcf':
        pre = F.split('.raw.vcf')[0]
        ouF = pre + '.flt.vcf'
        inFile = open(F)
        ouFile = open(ouF, 'w')
        for line in inFile:
            line = line.strip()
            if line[0:2] == '##':
                ouFile.write(line + '\n')
            else:
                DP = -1
                VDB = -1
                RPB = -1
                MQSB = -1
                DP4 = -1
                filtered = 0

                info = line.split('\t')[7].split(';')
                for x in info:
                    if x.find('DP=') == 0:
                        DP = int(x.split('DP=')[1])
                    elif x.find('VDB') == 0:
                        VDB = float(x.split('VDB=')[1])
                    elif x.find('RPB') == 0:
                        RPB = float(x.split('RPB=')[1])
                    elif x.find('MQSB') == 0:
                        MQSB = float(x.split('MQSB=')[1])
                    elif x.find('DP4') == 0:
                        DP4 = x.split('DP4=')[1].split(',')
                        DP4ref = int(DP4[0]) + int(DP4[1])
                        DP4alt = int(DP4[2]) + int(DP4[3])

                    if DP != -1:
                        if 10 < DP < 500:
                            pass
                        else:
                            filtered = 1
                    if VDB != -1 and VDB < 0.0001:
                        filtered = 1
                    #if RPB != -1 and RPB < 0.05:
                    #    filtered = 1
                    #if MQSB != -1 and MQSB < 0.05:
                    #    filtered = 1
                    #if DP4 != -1:
                    #    if DP4ref == 0:
                    #        if DP4alt >= 5:
                    #            pass
                    #        else:
                    #            filtered = 1
                    #    else:
                    #        if DP4ref >= 5 and DP4alt >= 5:
                    #            pass
                    #        else:
                    #            filtered = 1
                if not filtered:
                    ouFile.write(line + '\n')
                
        inFile.close()
        ouFile.close()
