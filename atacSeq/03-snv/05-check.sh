samtools tview S96a.bam $yeast -d C -p $1:`expr $2 - 100`
samtools tview S96b.bam $yeast -d C -p $1:`expr $2 - 100`
samtools tview YJM789a.bam $yeast -d C -p $1:`expr $2 - 100`
samtools tview YJM789b.bam $yeast -d C -p $1:`expr $2 - 100`
samtools tview 5a.bam $yeast -d C -p $1:`expr $2 - 100`
samtools tview 5b.bam $yeast -d C -p $1:`expr $2 - 100`
