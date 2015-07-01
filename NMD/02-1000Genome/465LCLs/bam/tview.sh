bam=NA12761.6.M_120119_2.bam
chr=chr17
pos=59667953
p=`expr $pos - 20`

samtools tview -d T  -p ${chr}:${p}  ${bam} $hg19 
