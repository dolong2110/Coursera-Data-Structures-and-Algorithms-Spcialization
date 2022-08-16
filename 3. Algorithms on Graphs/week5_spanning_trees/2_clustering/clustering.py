#Uses python3
import sys
import math
import heapq


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def clustering(x, y, k):
    #write your code here
    n = len(x)
    pq = []
    uf = UnionFind(n)

    for i in range(n):
        x1, y1 = x[i], y[i]
        for j in range(i + 1, n):
            x2, y2 = x[j], y[j]
            # Calculate the distance between two coordinates.
            cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            edge = Edge(i, j, cost)
            pq.append(edge)
    heapq.heapify(pq)
    cnt = n - 1
    res = []
    heapq.heapify(res)
    while pq and cnt:
        edge = heapq.heappop(pq)
        if not uf.connected(edge.point1, edge.point2):
            uf.union(edge.point1, edge.point2)
            heapq.heappush(res, -edge.cost)
            cnt -= 1
    for _ in range(k - 1):
        c = -heapq.heappop(res)

    return c


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
