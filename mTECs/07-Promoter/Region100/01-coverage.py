Sample = ['Tspan8_positive_MHCII_high_rep1_HQ.bam','Tspan8_positive_MHCII_high_rep2_HQ.bam','Tspan8_negative_MHCII_high_rep1_HQ.bam','Tspan8_negative_MHCII_high_rep2_HQ.bam','Tspan8_positive_MHCII_low_rep1_HQ.bam','Tspan8_positive_MHCII_low_rep2_HQ.bam','Tspan8_negative_MHCII_low_rep1_HQ.bam','Tspan8_negative_MHCII_low_rep2_HQ.bam']
Head = [x.split('_HQ.bam')[0] for x in Sample]


CH = [str(x) for x in range(1, 20)] + ['X','Y','MT']

ouF = 'Mouse_Gene_Promoter_Cov'

ouFile2 = open(ouF, 'w')
ouFile2.write('\t'.join(['chr', 'start', 'end', 'gene'] + Head) + '\n')
ouFile2.close()

ouFile = open(ouF + '.sh', 'w')
ouFile.write('bedtools multicov -bams ' + ' '.join(Sample) + ' -bed ' + 'Mouse_Gene_Promoter.bed' + ' >>%s\n'%ouF)
ouFile.close()

