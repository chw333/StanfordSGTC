import subprocess

ref = '/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/Mus_musculus.GRCm38.dna.toplevel.fa'

Sample = ['Tspan8_positive_MHCII_high_rep1_HQ.bam','Tspan8_positive_MHCII_high_rep2_HQ.bam','Tspan8_negative_MHCII_high_rep1_HQ.bam','Tspan8_negative_MHCII_high_rep2_HQ.bam','Tspan8_positive_MHCII_low_rep1_HQ.bam','Tspan8_positive_MHCII_low_rep2_HQ.bam','Tspan8_negative_MHCII_low_rep1_HQ.bam','Tspan8_negative_MHCII_low_rep2_HQ.bam']

for i in range(6,8):
    F = Sample[i]
    ouFile = open(F.split('_HQ.bam')[0] + '.Cov', 'w')
    p = subprocess.Popen(['samtools','mpileup', '-uvf', ref, F], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in p.stdout:
        if line[0] != '#':
            fields = line.split('\t')
            info = fields[7]
            if info[0:3] == 'DP=':
                DP = info.split(';')[0].split('DP=')[1]
                ouFile.write('\t'.join([fields[0], fields[1], DP]) + '\n')
    ouFile.close()
