def gene_symbol(inF):
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        print(gene)
    inFile.close()

def gene_symbol_exp(inF):
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        base = float(fields[1])
        gene_type = fields[8]
        if gene_type == 'protein_coding':
            if base > 10:
                print(gene)
    inFile.close()

def gene_symbol_exp_test(inF):
    inFile = open(inF)
    head = inFile.readline()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        gene = fields[7]
        base = float(fields[1])
        gene_type = fields[8]
        try:
            log = float(fields[2])
            if gene_type == 'protein_coding':
                if base > 10:
                    if log > 2 or log < -2:
                        print(line)
        except:
            pass
    inFile.close()


#gene_symbol('deWNV_sig_proteincoding.txt')
#gene_symbol_exp('deWNV.txt')
gene_symbol_exp_test('deWNV.txt')
