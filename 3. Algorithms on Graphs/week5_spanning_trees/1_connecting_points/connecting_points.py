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

def minimum_distance(x, y):
    result = 0
    #write your code here
    n = len(x)
    pq = []
    visited = [0 for _ in range(n)]
    cnt = n - 1
    x1, y1 = x[0], y[0]
    for j in range(1, n):
        x2, y2 = x[j], y[j]
        cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        edge = Edge(0, j, cost)
        pq.append(edge)
    heapq.heapify(pq)
    visited[0] = 1
    while pq and cnt:
        edge = heapq.heappop(pq)
        p1, p2, c = edge.point1, edge.point2, edge.cost
        if not visited[p2]:
            result += c
            visited[p2] = 1
            for j in range(n):
                if not visited[j]:
                    dist = math.sqrt((x[p2] - x[j])**2 + (y[p2] - y[j])**2)
                    heapq.heappush(pq, Edge(p2, j, dist))
            cnt -= 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
