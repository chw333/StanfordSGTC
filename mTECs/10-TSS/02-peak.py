import pandas as pd
Sample = ['Tspan8_positive_MHCII_high_rep1.num','Tspan8_positive_MHCII_high_rep2.num','Tspan8_negative_MHCII_high_rep1.num','Tspan8_negative_MHCII_high_rep2.num','Tspan8_positive_MHCII_low_rep1.num','Tspan8_positive_MHCII_low_rep2.num','Tspan8_negative_MHCII_low_rep1.num','Tspan8_negative_MHCII_low_rep2.num']

ouFile = open('mTECs-TSS-Peak', 'w')
for S in Sample:
    df = pd.read_table(S, header=None)
    ouFile.write(S.split('.num')[0] + '\t' + str(max(df[0])) + '\n')

ouFile.close()

