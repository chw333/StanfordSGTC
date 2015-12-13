#htseq-count -f bam -s no PV_Neurons_rep2_NF.bam Mouse_Gene_Promoter.gtf > PV_Neurons_rep2_NF.count
#htseq-count -f bam -s no Excitatory_Neurons_rep1_NF.bam Mouse_Gene_Promoter.gtf > Excitatory_Neurons_rep1_NF.count
#htseq-count -f bam -s no Excitatory_Neurons_rep2_NF.bam Mouse_Gene_Promoter.gtf > Excitatory_Neurons_rep2_NF.count
#htseq-count -f bam -s no PV_Neurons_rep1_NF.bam Mouse_Gene_Promoter.gtf > PV_Neurons_rep1_NF.count
htseq-count -f bam -s no VIP_Neurons_rep1_NF.bam Mouse_Gene_Promoter.gtf > VIP_Neurons_rep1_NF.count
htseq-count -f bam -s no VIP_Neurons_rep2_NF.bam  Mouse_Gene_Promoter.gtf > VIP_Neurons_rep2_NF.count
