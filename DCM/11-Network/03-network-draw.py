import matplotlib
matplotlib.use('Agg')
import networkx as nx
import pylab as plt

def draw(inF):
    G = nx.Graph()

    inFile = open(inF)
    S = set()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            S.add(item)
    inFile.close()

    L = list(S)
    G.add_nodes_from(L)

    LC = []
    for x in L:
        if x == 'EGR1' or x == 'RBM20':
            LC.append('r')
        else:
            LC.append('w')

    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i in range(len(fields)-1):
            G.add_edge(fields[i], fields[i+1])
    inFile.close()
    nx.draw_networkx(G,pos=nx.spring_layout(G), node_size=800, font_size=6, node_color=LC)
    limits=plt.axis('off')
    plt.savefig(inF + '.pdf')


draw('String-Biogrid-Network-RBM20-EGR1')





