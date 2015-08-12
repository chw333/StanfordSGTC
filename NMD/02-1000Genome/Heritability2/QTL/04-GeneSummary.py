### python GenSummary.py NGLY1
import urllib2
import json
import sys

#gene = sys.argv[1]

def symbol2id():
    D = {}
    data = urllib2.urlopen('ftp://ftp.ncbi.nih.gov/refseq/H_sapiens/RefSeqGene/gene_RefSeqGene')
    for item in data:
        item = item.strip()
        fds = item.split('\t')
        D.setdefault(fds[2], [])
        D[fds[2]].append(fds[1])
    return(D)
D = symbol2id()


inFile = open('Single-Trait-lm-Sig2-Sorted-Gene')
ouFile = open('Single-Trait-lm-Sig2-Sorted-GeneSummary', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[4]
    summary = ''
    if gene in D:
        g = D[gene][0] 
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=' + g + '&retmode=json';
        data = json.load(urllib2.urlopen(url))
        summary = data['result'][str(g)]['summary'].strip()
    ouFile.write(line + '\t' + summary + '\n')
inFile.close()
ouFile.close()
