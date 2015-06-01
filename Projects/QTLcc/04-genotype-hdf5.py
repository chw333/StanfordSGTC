import h5py
import scipy as sp
def g01tohdf5(g01_file):
    hdf = h5py.File('Yeast-Genotype.hdf5', 'w')
    genotype = hdf.create_group('genotype')
    col_header = genotype.create_group('col_header')
    row_header = genotype.create_group('row_header')
    #load position and meta information
    indv_file = 'Yeast-Strains'
    pos_file  = 'Yeast-Position'
    sample_ID = sp.loadtxt(indv_file,dtype='str')
    pos  = sp.loadtxt(pos_file,dtype='str')
    chrom = pos[:,0]
    pos   = sp.array(pos[:,1],dtype='int')

    row_header.create_dataset(name='sample_ID',data=sample_ID)
    col_header.create_dataset(name='chrom',data=chrom)
    col_header.create_dataset(name='pos',data=pos)
    M = sp.loadtxt(g01_file,dtype='string')
    snps = M[1:,1::]
    snps = snps.astype('uint8')
    print(len(snps))
    print(len(snps[0]))
    genotype.create_dataset(name='matrix',data=snps,chunks=(snps.shape[0],min(10000,snps.shape[1])),compression='gzip')

g01tohdf5('Yeast-Genotype-Formated')

