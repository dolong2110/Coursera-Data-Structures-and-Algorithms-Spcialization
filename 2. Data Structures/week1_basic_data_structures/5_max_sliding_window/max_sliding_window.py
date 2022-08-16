# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    d = deque()
    out = []
    for i, n in enumerate(sequence):
        while d and sequence[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - m:
            d.popleft()
        if i >= m - 1:
            out.append(sequence[d[0]])
    return out

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

