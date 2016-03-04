import urllib2
import json

def probe2gene():
    D = {}
    inFile = open('ProbSetID-Ensembl-GeneSymbol-HG-U133A_2.na34.annot.txt')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D[fields[0]] = '|'.join(fields[1].split(' /// '))
    inFile.close()
    return D
PG = probe2gene()

        


def query(drug):
    ouFile = open(drug + '_cell_gene', 'w')
    f = urllib2.urlopen('http://api.lincscloud.org/a2/siginfo?q={"pert_desc":"%s"}&user_key=lincsdemo'%drug)
    s = f.read()
    sj = json.loads(s)
    for i in range(len(sj)):
        cell_id = sj[i]['cell_id']

        up100_full = sj[i]['up100_full']
        dn100_full = sj[i]['dn100_full']

        up100_full_gene = [PG[x] for x in up100_full if PG[x] != '---' and PG[x].find('|') == -1]
        dn100_full_gene = [PG[x] for x in dn100_full if PG[x] != '---' and PG[x].find('|') == -1]

        ouFile.write(drug + '\t' + cell_id + '\t' + ' '.join(up100_full_gene) + '\t' + ' '.join(dn100_full_gene) + '\n')


    ouFile.close()

query('digoxin')

