import string
inFile = open('HOXB3.fasta')
head = inFile.readline()
seq = inFile.readline().strip()
inFile.close()
trans = string.maketrans('ATCG','TAGC')

for i in range(0, len(seq)-16):
    S = seq[i:i+17]
    S = string.translate(S, trans)
    S = S[::-1]

    #if S[0] in ['G','A'] and S[1] in ['G'] and S[2] in ['G', 'T'] and S[3] in ['T'] \
            #        and S[4] in ['C','G'] and S[5] in ['A'] \
            #and S[11] in ['A', 'G'] and S[12] in ['G'] and S[13] in ['G', 'T'] and S[14] in ['T'] \
            #and S[15] in ['C', 'G'] and S[16] in ['A']:
    if S[0] in 'GA' and S[1] in 'G' and S[2] in 'TG' and S[3] in 'T' and S[4] in 'CG' and S[5] in 'A' and S[11] in 'GA' and S[12] in 'G' and S[13] in 'TG' and S[14] in 'T' and S[15] in 'CG' and S[16] in 'A':
        print(S)

