import matplotlib
matplotlib.use('Agg')
import HTSeq
import numpy
import pylab as plt

CH = [str(x) for x in range(1,20)] + ['X', 'Y']

bamfile = HTSeq.BAM_Reader( "Tspan8_negative_MHCII_high_rep1_HQ.bam" )
gtffile = HTSeq.GFF_Reader( "Mus_musculus.GRCm38.82.gtf" )

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
                print(almnt.iv)
        #### method 3
        ###coverage[ almnt.iv ] += 1

        

tsspos = set()
for feature in gtffile:
    if feature.type == "exon" and feature.attr["exon_number"] == "1":
        if feature.iv.chrom in CH:
            tsspos.add( feature.iv.start_d_as_pos )

profile = numpy.zeros( 2*halfwinwidth, dtype='i' )      
for p in tsspos:
    if p.pos >= halfwinwidth:
        window = HTSeq.GenomicInterval( p.chrom, p.pos - halfwinwidth, p.pos + halfwinwidth, "." )
        wincvg = numpy.fromiter( coverage[window], dtype='i', count=2*halfwinwidth )
        if p.strand == "+":
            profile += wincvg
        else:
            profile += wincvg[::-1]
        

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot( numpy.arange( -halfwinwidth, halfwinwidth ), profile )
plt.savefig('test.pdf')

