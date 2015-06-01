import pandas
import scipy as sp
import h5py
C = pandas.io.parsers.read_csv('Yeast-Phenotype-Formated',header=0,index_col=0,sep='\t')
matrix = sp.array(C.values,dtype='float')
sample_IDs = sp.array(C.index,dtype='str')
pheno_IDs  = sp.array(C.columns.values,dtype='str')
hdf = h5py.File('Yeast-Phenotype.hdf5', 'w')
if 'phenotype' in hdf.keys():
    del(hdf['phenotype'])
phenotype = hdf.create_group('phenotype')
col_header = phenotype.create_group('col_header')
row_header = phenotype.create_group('row_header')
phenotype.create_dataset(name='matrix',data=matrix)
row_header.create_dataset(name='sample_ID',data=sample_IDs)
col_header.create_dataset(name='phenotype_ID',data=pheno_IDs)
