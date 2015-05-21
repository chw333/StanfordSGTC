def tview(inF, bam):
    inFile = open(inF)
    ouFile = open(inF +'-'+bam+ '-tview.sh', 'w')
    for line in inFile:
        fields = line.split('\t')
        info = fields[4].split(':')
        ch = info[0]
        start = info[2]
        end = info[3]
        ouFile.write('samtools tview -p %s:%s -d T %s Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa\n'%(ch,int(start)-20,bam))
        ouFile.write('samtools tview -p %s:%s -d T %s Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa\n'%(ch,int(end)-100,bam))
        
    inFile.close()
    ouFile.close()

tview('Yeast-Peptide-NTerminal-SixFrame-Candidates-Gene-ORF-seq-Intergenic','SRR1258542_trimmed.sorted.bam')
tview('Yeast-Peptide-NTerminal-SixFrame-Candidates-Gene-ORF-seq-Intergenic','SRR1258541_trimmed.sorted.bam')
