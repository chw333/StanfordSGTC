import h5py
import numpy as np


def geno2hdf5(inF, inF2):
    hdf = h5py.File(inF + '.hdf5', 'w')
    genotype = hdf.create_group('genotype')
    col_header = genotype.create_group('col_header')
    row_header = genotype.create_group('row_header')
    #load position and meta information
    #indv_file = 'Yeast-Strains'
    #sample_ID = np.loadtxt(indv_file,dtype='str')

    pos  = np.loadtxt(inF2,dtype='str')
    chrom = pos[:,0]
    pos   = np.array(pos[:,1],dtype='int')

    M = np.loadtxt(inF,dtype='string')

    row_header.create_dataset(name='sample_ID',data=M[1:,0])
    col_header.create_dataset(name='chrom',data=chrom)
    col_header.create_dataset(name='pos',data=pos)

    geno = M[0:,1:]
    geno = geno.astype('uint8')

    genotype.create_dataset(name='matrix',data=geno,chunks=(geno.shape[0],min(10000,geno.shape[1])),compression='gzip')

    print(len(geno))
    print(len(geno[0]))
 
#geno2hdf5('1000Genome-462LCLs-Genotype-Sample2', '1000Genome-462LCLs-Position')

def Pheno2hdf5(inF):
    hdf = h5py.File(inF + '.hdf5', 'w')
    phenotype = hdf.create_group('phenotype')
    col_header = phenotype.create_group('col_header')
    row_header = phenotype.create_group('row_header')

    M = np.loadtxt(inF,dtype='string')

    row_header.create_dataset(name='sample_ID',data=M[1:,0])
    col_header.create_dataset(name='phenotype_ID',data=M[0,1:])
    pheno = M[1:,1:]
    pheno = pheno.astype('float')

    phenotype.create_dataset(name='matrix',data=pheno,chunks=(pheno.shape[0],min(10000,pheno.shape[1])),compression='gzip')

    print(len(pheno))
    print(len(pheno[0]))


Pheno2hdf5('G462-Sample-Stopgain-Pheno2')

