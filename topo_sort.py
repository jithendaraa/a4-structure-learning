import numpy as np
import networkx as nx

def topov1(ad_mat):
    while True:
        res = np.argwhere(np.all(ad_mat == 0, 0)).squeeze(-1)
        if len(res) == 0:
            break
        ad_mat[[res]] = 0
        ad_mat[:, [res]] = -1
        yield from res

ad_mat = np.array(nx.adjacency_matrix(graph).todense())

temp_ad = ad_mat.copy()
print(temp_ad)

[x for x in topov1(temp_ad)]
