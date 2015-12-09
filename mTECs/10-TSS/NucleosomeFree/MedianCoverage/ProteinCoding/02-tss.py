import matplotlib
matplotlib.use('Agg')
import HTSeq
import numpy 
import pylab as plt
import os

CH = [str(x) for x in range(1,20)] + ['X', 'Y']

gtffile = HTSeq.GFF_Reader( "Mus_musculus.GRCm38.82.gtf" )

tsspos = set()
G = {}
for feature in gtffile:
    if feature.type == "exon" and feature.attr["exon_number"] == "1" and feature.attr["gene_biotype"] == "protein_coding":
        if feature.iv.chrom in CH:
            G.setdefault(feature.name, [])
            G[feature.name].append(feature.iv.start_d_as_pos)
            #tsspos.add( feature.iv.start_d_as_pos )
for g in G:
    gp = G[g]
    strand = gp[0].strand
    if strand == '+':
        gp.sort(cmp = lambda x,y:cmp(x.start,y.start))
    else:
        gp.sort(cmp = lambda x,y:cmp(x.end, y.end), reverse=True)
    tsspos.add(gp[0])



Fs = os.listdir('.')
for F in Fs:
    #if F[-7:] == '_NF.bam':
    if F == 'Tspan8_negative_MHCII_high_rep1_NF.bam':

        bamfile = HTSeq.BAM_Reader(F)
        halfwinwidth = 1000
        
        coverage = HTSeq.GenomicArray( "auto", stranded=False, typecode="i" )
        for almnt in bamfile:
            if almnt.aligned:
                #### method 1
                if almnt.inferred_insert_size > 0:
        
                    #iv = HTSeq.GenomicInterval( almnt.iv.chrom, almnt.iv.start, almnt.iv.start + almnt.inferred_insert_size, "." )
                    #coverage[ almnt.iv ] += 1
                #### method 2, same as method 1
                    try:
                        almnt.iv.length = almnt.inferred_insert_size
                        coverage[ almnt.iv ] += 1
                    except:
                        print(almnt.get_sam_line())
                #### method 3
                ###coverage[ almnt.iv ] += 1
        
                
        
        #profile = numpy.zeros( 2*halfwinwidth, dtype='i' )      
        profile = [[] for x in range(2*halfwinwidth)]
        for p in tsspos:
            if p.pos >= halfwinwidth:
                window = HTSeq.GenomicInterval( p.chrom, p.pos - halfwinwidth, p.pos + halfwinwidth, "." )
                wincvg = numpy.fromiter( coverage[window], dtype='i', count=2*halfwinwidth )
                if p.strand == "+":
                    #profile += wincvg
                    for x in range(len(wincvg)):
                        profile[x].append(wincvg[x])
                else:
                    #profile += wincvg[::-1]
                    wincvg2 = wincvg[::-1]
                    for x in range(len(wincvg2)):
                        profile[x].append(wincvg2[x])
                
        ouFile = open(F.split('_NF.bam')[0] + '.NF.num.sum', 'w')
        for x in profile:
            ouFile.write(str(numpy.sum(x)) + '\n')
        ouFile.close()

        ouFile = open(F.split('_NF.bam')[0] + '.NF.num.median', 'w')
        for x in profile:
            #ouFile.write(str(numpy.median(x)) + '\n')
            #ouFile.write(str(numpy.percentile(x, 100)) + '\n')
            ouFile.write('\t'.join([str(m) for m in x]) + '\n')
        ouFile.close()
 
        
        fig = plt.figure()
        ax = fig.add_axes([0.15,0.12,0.82,0.8])
        ax.plot( numpy.arange( -halfwinwidth, halfwinwidth ), [numpy.median(x) for x in profile] )
        ax.set_xlabel('Distance to TSS (bp)')
        ax.set_ylabel('Median reads number')
        plt.savefig(F.split('_NF.bam')[0] + '.NF.TSS.median.pdf')

