#Uses python3

import sys


def acyclic(adj):
    n = len(adj)
    indegree, ans = [0 for _ in range(n)], []
    for i in adj:
        for j in i:
            indegree[j] += 1
    
    def dfs(cur):
        ans.append(cur)
        indegree[cur] -= 1
        for i in adj[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                dfs(i)
    for i in range(n):
        if indegree[i] == 0:
            dfs(i)

    return 1 - (len(ans) == n)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
