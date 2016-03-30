import networkx as nx

def network(inF, gene1, gene2):
    G = nx.Graph()

    inFile = open(inF)
    S = set()
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        S.add(fields[0])
        S.add(fields[1])
    inFile.close()
    L = list(S)

    G.add_nodes_from(L)

    inFile =open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        G.add_edge(fields[0], fields[1])
    inFile.close()
    
    print(G.number_of_nodes())
    print(G.number_of_edges())

    #s = nx.shortest_path(G, 'RBM20', 'EGR1')
    s = nx.all_shortest_paths(G, gene1, gene2)
    ouFile = open(inF + '-' + gene1 + '-' + gene2, 'w')
    for x in s:
        ouFile.write('\t'.join(x) + '\n')
    ouFile.close()

network('String-Biogrid-Network', 'RBM20', 'ZBTB7A')
