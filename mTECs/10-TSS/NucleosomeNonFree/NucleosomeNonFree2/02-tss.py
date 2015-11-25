import matplotlib
matplotlib.use('Agg')
import HTSeq
import numpy
import pylab as plt
import os

CH = [str(x) for x in range(1,20)] + ['X', 'Y']

gtffile = HTSeq.GFF_Reader( "Mus_musculus.GRCm38.82.gtf" )

tsspos = set()
for feature in gtffile:
    if feature.type == "exon" and feature.attr["exon_number"] == "1":
        if feature.iv.chrom in CH:
            tsspos.add( feature.iv.start_d_as_pos )

Fs = os.listdir('.')
for F in Fs:
    if F[-8:] == '_NS2.bam':

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
        
                
        
        profile = numpy.zeros( 2*halfwinwidth, dtype='i' )      
        for p in tsspos:
            if p.pos >= halfwinwidth:
                window = HTSeq.GenomicInterval( p.chrom, p.pos - halfwinwidth, p.pos + halfwinwidth, "." )
                wincvg = numpy.fromiter( coverage[window], dtype='i', count=2*halfwinwidth )
                if p.strand == "+":
                    profile += wincvg
                else:
                    profile += wincvg[::-1]
                
        ouFile = open(F.split('_NS2.bam')[0] + '.NS2.num', 'w')
        for x in profile:
            ouFile.write(str(x) + '\n')
        ouFile.close()
        
        fig = plt.figure()
        ax = fig.add_axes([0.15,0.12,0.82,0.8])
        ax.plot( numpy.arange( -halfwinwidth, halfwinwidth ), profile )
        ax.set_xlabel('Distance to TSS (bp)')
        ax.set_ylabel('Number of reads')
        plt.savefig(F.split('_NS2.bam')[0] + '.NS2.TSS.pdf')

