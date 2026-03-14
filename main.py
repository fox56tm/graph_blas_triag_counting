import numpy as np
import graphblas as gb
import algorithms as alg

import networkx as nx


def generate_large_graph(nodes=5000, prob=0.005):

    G = nx.erdos_renyi_graph(nodes, prob)

    edges = list(G.edges())

    rows, cols = zip(*edges) if edges else ([], [])

    return list(rows), list(cols)


rows, cols = generate_large_graph()


matrix = gb.Matrix.from_coo(rows, cols, [1]*len(rows), nrows=5000, ncols=5000)

c = alg.bukhartAlg(matrix)

b = alg.sandiaAlg(matrix)

z = alg.nativeAlg(matrix)

print(c)

print('\n')

print(b)

print('\n')
print(z)

