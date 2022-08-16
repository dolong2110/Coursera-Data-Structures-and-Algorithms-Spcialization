#Uses python3

import sys
import collections

def distance(adj, s, t):
    #write your code here
    visited = set()
    q = collections.deque([s])
    steps = 0
    while q:
        n = len(q)
        for _ in range(n):
            cur = q.popleft()
            if cur == t:
                return steps
            visited.add(cur)
            for i in adj[cur]:
                if i not in visited:
                    q.append(i)
        steps += 1
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
