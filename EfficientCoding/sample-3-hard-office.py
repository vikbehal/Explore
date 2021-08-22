from itertools import combinations
from math import inf
from collections import deque


def solve(w, h, p):
    q = deque()
    visited = set()
    maxDist = 0
    for a, b, d in p:
        q.append((a, b, d))
        visited.add((a, b))

    while q:
        r, c, d = q.popleft()
        maxDist = max(maxDist, d)
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= i < h and 0 <= j < w and (i, j) not in visited:
                visited.add((i, j))
                q.append((i, j, d + 1))

    return maxDist


w = 5
h = 1
n = 1

mindist = inf
pos = []
for a in range(h):
    for b in range(w):
        pos.append((a, b, 0))

print(pos)
for p in combinations(pos, n):
    print(p)
    mindist = min(mindist, solve(w, h, p))

print(mindist)
