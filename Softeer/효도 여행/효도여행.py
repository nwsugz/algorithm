def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    return L[m][n]

def dfs(node, parent, graph, path, paths, edges):
    if len(graph[node]) == 1 and node != 1:  # leaf node
        paths.append(path)
        return

    for neighbor, char in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, path + char, paths, edges)

import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])
S = data[2]

edges = data[3:]
graph = [[] for _ in range(N + 1)]

for i in range(0, len(edges), 3):
    u = int(edges[i])
    v = int(edges[i + 1])
    c = edges[i + 2]
    graph[u].append((v, c))
    graph[v].append((u, c))

paths = []
dfs(1, -1, graph, '', paths, edges)

max_happiness = 0
for path in paths:
    max_happiness = max(max_happiness, lcs(S, path))

print(max_happiness)