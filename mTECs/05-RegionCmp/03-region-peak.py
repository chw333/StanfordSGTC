#Sample = ['Tspan8_negative_MHCII_high_rep1.Cov','Tspan8_negative_MHCII_high_rep2.Cov','Tspan8_negative_MHCII_low_rep1.Cov','Tspan8_negative_MHCII_low_rep2.Cov']
#Sample = ['Tspan8_positive_MHCII_high_rep1.Cov','Tspan8_positive_MHCII_high_rep2.Cov','Tspan8_positive_MHCII_low_rep1.Cov','Tspan8_positive_MHCII_low_rep2.Cov']
Sample = ['Tspan8_positive_MHCII_high_rep1.Cov','Tspan8_positive_MHCII_high_rep2.Cov','Tspan8_negative_MHCII_high_rep1.Cov','Tspan8_negative_MHCII_high_rep2.Cov']
#Sample = ['Tspan8_positive_MHCII_low_rep1.Cov','Tspan8_positive_MHCII_low_rep2.Cov','Tspan8_negative_MHCII_low_rep1.Cov','Tspan8_negative_MHCII_low_rep2.Cov']


RegionLen = 100
nSample = len(Sample)

def dict_key(n, ch, chLen):
    if n == 0:
        start = RegionLen * n + 1
    else:
        start = RegionLen * n
    if (n+1)*RegionLen >= chLen:
        end = chLen
    else:
        end = (n+1)*RegionLen - 1
    k = ':'.join([ch, str(start), str(end)])
    return k

def data_structure(inF):
    D = {}
    L = []
    CH_LEN = {}
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split()
        ch = fields[0]
        chLen = int(fields[1])
        CH_LEN[ch] = chLen
        for n in range(chLen/RegionLen + 1):
            k = dict_key(n, ch, chLen)
            D[k] = [0]*nSample
            L.append(k)
    inFile.close()
    return(D, L, CH_LEN)

def read_data(Sample):
    for isa, sa in enumerate(Sample):
        inFile = open(sa)
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            ch = fields[0]
            pos = int(fields[1])
            num = int(fields[2])
            try:
                k =  dict_key(pos/RegionLen, ch, CH_LEN[ch])
                if num > D[k][isa]:
                    D[k][isa] = num
            except:
                pass
        inFile.close()

D, L, CH_LEN= data_structure('Mouse-Chr-Length')
read_data(Sample)
ouFile = open('MHCII_High_Tspan8_PositiveNegative', 'w')
ouFile.write('Region' + '\t' + '\t'.join([x.split('.Cov')[0] for x in Sample]) + '\n')
for k in L:
    ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]]) + '\n')
ouFile.close()
