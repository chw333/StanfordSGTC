import numpy as np

def filter(inF):
    ouFile = open(inF + '-filtered', 'w')
    data = np.loadtxt(inF, dtype='str')
    dataT = data.T
    L = [dataT[0]]
    for x in dataT[1:]:
        if '-1' in x:
            pass
        else:
            L.append(x)
    L = np.array(L)
    LT = L.T
    for x in LT:
        ouFile.write('\t'.join(x) + '\n')
    ouFile.close()


###filter('1000Genome-465LCLs-Genotype')

def filter_transform_legacy(inF):
    #### same function as filter_transform
    ouFile = open(inF + '-FiltTrans', 'w')
    #data = np.loadtxt(inF, dtype='str')
    data = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        data.append(fields)
    inFile.close()
    data = np.array(data)

    dataT = data.T
    L = [dataT[0]]
    for x in dataT[1:]:
        #if x[0].find('snp') != -1:
        if '-1' in x:
            pass
        else:
            L.append(x)
    #L = np.array(L)
    #LT = L.T
    for x in L:
        ouFile.write('\t'.join(x) + '\n')
    ouFile.close()

def filter_transform(inF):
    ouFile = open(inF + '-FiltTrans', 'w')
    #data = np.loadtxt(inF, dtype='str')
    data = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        data.append(fields)
    inFile.close()
    data = np.array(data)
    #dataT = data.T
    #L = [dataT[0]]
    #for x in dataT[1:]:
        #if x[0].find('snp') != -1:
    for i in range(data.shape[1]):
        x = data[:,i]
        if '-1' in x:
            pass
        else:
            ouFile.write('\t'.join(x) + '\n')
            #L.append(x)
    #L = np.array(L)
    #LT = L.T
    #for x in L:
    ouFile.close()

def transform(inF):
    ouFile = open(inF + '-Trans', 'w')
    #data = np.loadtxt(inF, dtype='str')
    data = []
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        data.append(fields)
    inFile.close()
    data = np.array(data)
    for i in range(data.shape[1]):
        x = data[:,i]
        ouFile.write('\t'.join(x) + '\n')


#filter_transform('1000Genome-465LCLs-Genotype')
#filter_transform('1000Genome-465LCLs-Genotype')
#transform('1000Genome-465LCLs-Genotype-FiltTrans-Ref')
#transform('1000Genome-462LCLs-Genotype')
transform('1000Genome-462LCLs-Phenotype')
