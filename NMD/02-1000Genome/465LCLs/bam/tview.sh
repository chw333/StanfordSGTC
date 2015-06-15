bam=NA20512.6.M_120119_6.bam
chr=chr6
pos=31124849
p=`expr $pos - 20`

samtools tview -d T  -p ${chr}:${p}  ${bam} $hg19 
