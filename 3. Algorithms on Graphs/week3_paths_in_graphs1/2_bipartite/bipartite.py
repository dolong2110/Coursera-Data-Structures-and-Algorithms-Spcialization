#Uses python3

import sys
import collections

def bipartite(adj):
    #write your code here
    n, colored = len(adj), {}
    for i in range(n):
        if i not in colored:
            colored[i] = 1
            q = collections.deque([i])
            while q:
                cur = q.popleft()
                for nb in adj[cur]:
                    if nb not in colored:
                        colored[nb] = -colored[cur]
                        q.append(nb)
                    elif colored[nb] == colored[cur]:
                        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
