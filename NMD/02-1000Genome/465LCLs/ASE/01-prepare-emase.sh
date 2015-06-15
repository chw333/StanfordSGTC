REF_FASTA=Homo_sapiens.GRCh37.75.dna.fa
REF_GTF=Homo_sapiens.GRCh37.75.gtf
REF_DIR=transcriptome
BIN=/mnt/larsix/projects/NMD/hansun/MySoft/python/anaconda/envs/emase/bin
${BIN}/prepare-emase -G ${REF_FASTA} -g ${REF_GTF} -o ${REF_DIR} -m --no-bowtie-index
