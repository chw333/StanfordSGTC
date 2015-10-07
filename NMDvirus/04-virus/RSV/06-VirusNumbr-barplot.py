df = pd.read_table('RSV-Virus-Normalized')
L = []
S = []
for i in range(0,16,2):
    L.append(df.Normalized[i] + df.Normalized[i+1])
    sn = df.Sample[i].split('-')[0]
    if sn == 'HRSV0h':
        S.append('Mock')
    else:
        S.append(sn[1:])
        
    
df = pd.DataFrame(L,index=S)
df.ix[:,0] = np.log2(df.ix[:,0])
df.ix[0,0]=0

fig = plt.figure()
ax = fig.add_axes([0.1,0.15,0.85,0.8])
ax = df.plot(kind='bar', ax=ax, legend=False)
ax.set_xticklabels(S, rotation=45)
ax.set_ylabel('Normalized number of virus reads (log2)')
plt.savefig('RSV-Virus-Normalized.pdf')
