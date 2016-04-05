# coding: utf-8
import pandas as pd
df = pd.read_table('mTECs_Gene_Promoter_Cov_ProteinCoding', header=0)
df2 = df.ix[:,[0,1,2,3]]
#df2 = df2.copy()
df2['Tspan8_negative_MHCII_low'] = df['Tspan8_negative_MHCII_low_rep1'] + df['Tspan8_negative_MHCII_low_rep2']
