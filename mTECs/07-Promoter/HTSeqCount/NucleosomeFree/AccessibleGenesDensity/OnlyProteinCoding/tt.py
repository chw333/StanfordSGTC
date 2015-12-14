# coding: utf-8
df = pd.read_table('mTECs_Gene_Promoter_Cov_ProteinCoding', header=0)
LibSize = pd.read_table('mTECs-Sample-LibrarySize', header=None)
LS = LibSize.ix[:,1]
df.ix[:,4:12] = df.ix[:,4:12]/list(LS)*1000000
