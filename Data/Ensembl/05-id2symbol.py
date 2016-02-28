def id2symbol(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF.split('.gtf')[0] + '.gene', 'w')
    for line in inFile:
        if line[0] != '#':
            fields = line.split('\t')
            if fields[2] == 'gene':
                info = fields[8].split(';')
                for item in info:
                    if item.find('gene_id') != -1:
                        gene_id = item.split('"')[1]
                    elif item.find('gene_name') != -1:
                        gene_name = item.split('"')[1]
                D.setdefault(gene_id, [])
                D[gene_id].append(gene_name)
    inFile.close()
    d = D.items()
    d.sort(cmp =lambda x,y:cmp(x[0], y[0]))
    for item in d:
        if len(set(item[1])) != 1:
            print('Warning:gene_id to multiple gene_name')
        else:
            ouFile.write(item[0] + '\t' + item[1][0] + '\n')

    ouFile.close()

#id2symbol('Homo_sapiens.GRCh37.75.gtf')
id2symbol('Homo_sapiens.GRCh38.81.gtf')
