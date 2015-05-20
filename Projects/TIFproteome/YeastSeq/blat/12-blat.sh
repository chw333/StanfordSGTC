db=/srv/gsfs0/projects/steinmetz/hansun/TIFproteome/Annotation/Ensembl/blast/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa
query=SRR1258542-unmapped.fa
out=${query}.blated
blat $db $query  -out=blast8 $out
