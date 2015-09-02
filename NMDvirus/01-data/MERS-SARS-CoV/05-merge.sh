samtools merge -r -@ 8 MOCK_MRC5_1.bam SRR1192354.bam SRR1192353.bam
samtools index MOCK_MRC5_1.bam
samtools merge -r -@ 8 MOCK_MRC5_2.bam SRR1192370.bam SRR1192371.bam
samtools index MOCK_MRC5_2.bam
samtools merge -r -@ 8 MOCK_MRC5_3.bam SRR1192399.bam SRR1192398.bam
samtools index MOCK_MRC5_3.bam
samtools merge -r -@ 8 MERS_MRC5lowMOI_24hr_1.bam SRR1191914.bam SRR1191915.bam
samtools index MERS_MRC5lowMOI_24hr_1.bam
samtools merge -r -@ 8 MERS_MRC5lowMOI_24hr_2.bam SRR1191953.bam SRR1191954.bam
samtools index MERS_MRC5lowMOI_24hr_2.bam
samtools merge -r -@ 8 MERS_MRC5lowMOI_24hr_3.bam SRR1191990.bam SRR1191991.bam
samtools index MERS_MRC5lowMOI_24hr_3.bam
samtools merge -r -@ 8 MERS_MRC5HighMOI_24hr_1.bam SRR1192166.bam SRR1192167.bam
samtools index MERS_MRC5HighMOI_24hr_1.bam
samtools merge -r -@ 8 MERS_MRC5HighMOI_24hr_2.bam SRR1191668.bam SRR1191667.bam
samtools index MERS_MRC5HighMOI_24hr_2.bam
samtools merge -r -@ 8 MERS_MRC5HighMOI_24hr_3.bam SRR1191673.bam SRR1191672.bam
samtools index MERS_MRC5HighMOI_24hr_3.bam
samtools merge -r -@ 8 MERS_MRC5lowMOI_48hr_1.bam SRR1192017.bam SRR1192016.bam
samtools index MERS_MRC5lowMOI_48hr_1.bam
samtools merge -r -@ 8 MERS_MRC5lowMOI_48hr_2.bam SRR1192072.bam SRR1192073.bam
samtools index MERS_MRC5lowMOI_48hr_2.bam
mv SRR1192321.bam MERS_MRC5lowMOI_48hr_3.bam
samtools index MERS_MRC5lowMOI_48hr_3.bam
samtools merge -r -@ 8 MERS_MRC5HighMOI_48hr_1.bam SRR1191695.bam SRR1191694.bam
samtools index MERS_MRC5HighMOI_48hr_1.bam
mv SRR1191783.bam MERS_MRC5HighMOI_48hr_2.bam
samtools index MERS_MRC5HighMOI_48hr_2.bam
mv SRR1191876.bam MERS_MRC5HighMOI_48hr_3.bam
samtools index MERS_MRC5HighMOI_48hr_3.bam
samtools merge -r -@ 8 SARS_MRC5lowMOI_24hr_1.bam SRR1193199.bam SRR1193197.bam SRR1193198.bam
samtools index SARS_MRC5lowMOI_24hr_1.bam
samtools merge -r -@ 8 SARS_MRC5lowMOI_24hr_2.bam SRR1193405.bam SRR1193403.bam SRR1193404.bam
samtools index SARS_MRC5lowMOI_24hr_2.bam
samtools merge -r -@ 8 SARS_MRC5lowMOI_24hr_3.bam SRR1193522.bam SRR1193523.bam SRR1193524.bam
samtools index SARS_MRC5lowMOI_24hr_3.bam
samtools merge -r -@ 8 SARS_MRC5HighMOI_24hr_1.bam SRR1193013.bam SRR1193014.bam SRR1193015.bam
samtools index SARS_MRC5HighMOI_24hr_1.bam
samtools merge -r -@ 8 SARS_MRC5HighMOI_24hr_2.bam SRR1193016.bam SRR1193018.bam SRR1193017.bam
samtools index SARS_MRC5HighMOI_24hr_2.bam
samtools merge -r -@ 8 SARS_MRC5HighMOI_24hr_3.bam SRR1193101.bam SRR1193102.bam SRR1193100.bam
samtools index SARS_MRC5HighMOI_24hr_3.bam
samtools merge -r -@ 8 SARS_MRC5lowMOI_48hr_2.bam SRR1195619.bam SRR1195621.bam SRR1195620.bam
samtools index SARS_MRC5lowMOI_48hr_2.bam
samtools merge -r -@ 8 SARS_MRC5lowMOI_48hr_3.bam SRR1193638.bam SRR1193639.bam
samtools index SARS_MRC5lowMOI_48hr_3.bam
samtools merge -r -@ 8 SARS_MRC5HighMOI_48hr_2.bam SRR1193103.bam SRR1193104.bam
samtools index SARS_MRC5HighMOI_48hr_2.bam
samtools merge -r -@ 8 SARS_MRC5HighMOI_48hr_3.bam SRR1193106.bam SRR1193105.bam
samtools index SARS_MRC5HighMOI_48hr_3.bam
