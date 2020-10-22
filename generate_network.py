from networkx.generators.random_graphs import gnp_random_graph

n=100
p=0.5
g= gnp_random_graph(n, p)

# print(g.nodes)

ed = g.edges
f = open('filename.txt', 'w')

#res = ed


print('\n'.join(map(str, ed)).replace('(','').replace(')','').replace(',',''), file = f)