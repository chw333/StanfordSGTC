import pandas as pd
Sample = ['Tspan8_positive_MHCII_high_rep1.NF.num','Tspan8_positive_MHCII_high_rep2.NF.num','Tspan8_negative_MHCII_high_rep1.NF.num','Tspan8_negative_MHCII_high_rep2.NF.num','Tspan8_positive_MHCII_low_rep1.NF.num','Tspan8_positive_MHCII_low_rep2.NF.num','Tspan8_negative_MHCII_low_rep1.NF.num','Tspan8_negative_MHCII_low_rep2.NF.num']
Sample = ['GM12878_50k_Rep1_NF.num','GM12878_50k_Rep2_NF.num','GM12878_50k_Rep3_NF.num','GM12878_50k_Rep4_NF.num']

ouFile = open('GM12878-NF-TSS-Peak', 'w')
for S in Sample:
    df = pd.read_table(S, header=None)
    ouFile.write(S.split('_NF.num')[0] + '\t' + str(max(df[0])) + '\n')

ouFile.close()

