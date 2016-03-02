import urllib2
import json

def query(inF):
    inFile = open(inF)
    ouFile = open(inF + '_description', 'w')
    ouFile.write('\t'.join(['name','id','collection','vendor','pubchem_cid','url']) + '\n')
    for line in inFile:
        line = line.strip()
        f = urllib2.urlopen('http://api.lincscloud.org/a2/pertinfo?q={"pert_iname":"%s"}&user_key=lincsdemo'%line)
        s = f.read()
        sj = json.loads(s)
        if 'pert_url' in sj[0]:
            pert_url=sj[0]['pert_url']
        else:
            pert_url=''
        ouFile.write(sj[0]['pert_iname'] +'\t' + sj[0]['pert_id'] + '\t' + sj[0]['pert_collection'] +'\t'+ sj[0]['pert_vendor'] + '\t'+sj[0]['pubchem_cid'] +'\t' + pert_url+ '\n')
    inFile.close()
    ouFile.close()

query('result_UPTAG_summly_n7503_drug_anti-connection_drug_name')
query('result_UPTAG_summly_n7503_drug_connection_drug_name')
