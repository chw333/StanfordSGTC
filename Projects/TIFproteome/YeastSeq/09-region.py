def region(inF):
    inFile = open(inF)
    for line in inFile:
        fields = line.split('\t')
        info = fields[5].split(':')
        ch = info[0]
        strand = info[1]
        start = info[2]
        end = info[3]
        pep = fields[7]
        ouF = '_'.join([pep, ch, start, end])
        inFile = open('SRR1258540_trimmed.sorted.mpileup')
        ouFile = open(ouF+'_SRR1258540', 'w')
        for i in range(40):
            line = inFile.readline()
        for line in inFile:
            fields = line.split('\t')
            ch_t = fields[0]
            pos_t = fields[1]
            try:
                dp_t = fields[7].split(';')[0].split('=')[1]
                if ch == ch_t:
                    if int(start) - 10000 <= int(pos_t) <= int(end) + 10000:
                        ouFile.write('\t'.join([ch_t, pos_t, dp_t]) + '\n')
            except:
                pass
        inFile.close()
        ouFile.close()
    inFile.close()

region('Yeast-Peptide-NTerminal-SixFrame-Candidates-Gene-ORF-seq-TIFSeqCoveredPep-Intergenic')
