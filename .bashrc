#export PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$'
case "$TERM" in
       xterm*|screen|tmux)
          bind 'set completion-ignore-case on'
          ;;
esac


alias py='python'
alias ipy='ipython'
alias fs='find `pwd` -name'
alias ss='cd /mnt/larsix/projects/NMD/hansun'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -alF'
alias sh='bash'

export hg19='/mnt/larsix/projects/NMD/hansun/Data/UCSC/ucsc-chr/hg19.fa'
export hg19g='/mnt/larsix/projects/NMD/hansun/Data/GATK/ucsc.hg19.fasta'
export hg38='/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Homo_sapiens.GRCh38.dna.toplevel.fa'
export yeast='/mnt/larsix/projects/NMD/hansun/atacSeq/00-data/bwa-index/S288C_reference_sequence_R64-2-1_20150113.fsa.fa'
export mm='/mnt/larsix/projects/NMD/hansun/Data/Ensembl/Mouse/Mus_musculus.GRCm38.dna.toplevel.fa'
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/larsix/projects/NMD/hansun/MySoft/hdf5/hdf5-1.8.15/lib


export PATH=/mnt/larsix/projects/NMD/hansun/MySoft/python/anaconda/bin:/mnt/larsix/projects/NMD/hansun/MySoft/R/R-3.2.0/bin:$PATH:/mnt/larsix/projects/NMD/hansun/MySoft/bedtools/bedtools2/bin:/mnt/larsix/projects/NMD/hansun/MySoft/sra/sratoolkit.2.5.2-ubuntu64/bin:/mnt/larsix/projects/NMD/hansun/MySoft/tophat2/tophat-2.1.0.Linux_x86_64:mnt/larsix/projects/NMD/hansun/MySoft/git/git-2.4.1:/mnt/larsix/projects/NMD/hansun/MySoft/R/R-3.2.0/bin:/mnt/larsix/projects/NMD/hansun/MySoft/ANNOVAR/annovar:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/mnt/larsix/projects/NMD/hansun/MySoft/.rtorrent/pkg-config-0.28/bin:/mnt/larsix/projects/NMD/hansun/MySoft/.rtorrent/rtorrent-0.9.4/bin:/mnt/larsix/projects/NMD/hansun/MySoft/bcftools/bcftools-1.2:/mnt/larsix/projects/NMD/hansun/MySoft/samtools/samtools-1.2:/mnt/larsix/projects/NMD/hansun/MySoft/bowtie/bowtie2-2.2.5:/mnt/larsix/projects/NMD/hansun/MySoft/bwa/bwa-0.7.12:/mnt/larsix/projects/NMD/hansun/MySoft/blat:/mnt/larsix/projects/NMD/hansun/MySoft/blast/ncbi-blast-2.2.30+/bin:/mnt/larsix/projects/NMD/hansun/MySoft/plink/plink-1.07-x86_64:/mnt/larsix/projects/NMD/hansun/MySoft/edirect/edirect:/mnt/larsix/projects/NMD/hansun/MySoft/cmake/cmake-3.3.2-Linux-x86_64/bin:/mnt/larsix/projects/NMD/hansun/MySoft/bam-readcount/bin:/mnt/larsix/projects/NMD/hansun/MySoft/fastqc/FastQC:/mnt/larsix/projects/NMD/hansun/MySoft/DANPOS2/danpos-2.2.2:/mnt/larsix/projects/NMD/hansun/MySoft/git/git-2.4.1:/mnt/larsix/projects/NMD/hansun/MySoft/hdf5/hdf5-1.8.15/bin:/mnt/larsix/projects/NMD/hansun/MySoft/Subread/subread-1.5.0-Linux-x86_64/bin:/mnt/larsix/projects/NMD/hansun/MySoft/samtools/tabix-0.2.6



cd /mnt/larsix/projects/NMD/hansun
