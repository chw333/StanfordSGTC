import pandas as pd
Sample = ['Tspan8_positive_MHCII_high_rep1.NF.num','Tspan8_positive_MHCII_high_rep2.NF.num','Tspan8_negative_MHCII_high_rep1.NF.num','Tspan8_negative_MHCII_high_rep2.NF.num','Tspan8_positive_MHCII_low_rep1.NF.num','Tspan8_positive_MHCII_low_rep2.NF.num','Tspan8_negative_MHCII_low_rep1.NF.num','Tspan8_negative_MHCII_low_rep2.NF.num']

ouFile = open('mTECs-NF-TSS-Peak', 'w')
for S in Sample:
    df = pd.read_table(S, header=None)
    ouFile.write(S.split('.NF.num')[0] + '\t' + str(max(df[0])) + '\n')

ouFile.close()

