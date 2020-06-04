import math
from collections import deque

def plus_neighbors(A, N, M, i, j):
    neigh = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
    ret = []
    for k, l in neigh:
        if (0 <= k < N) and (0 <= l < M) and (A[k][l] == '1'):
            ret.append((k, l))
    return ret

def cross_neighbors(A, N, M, i, j):
    neigh = [(i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]
    ret = []
    for k, l in neigh:
        if (0 <= k < N) and (0 <= l < M) and (A[k][l] == '1'):
            ret.append((k, l))
    return ret

def star_neighbors(A, N, M, i, j):
    return plus_neighbors(A, N, M, i, j) + cross_neighbors(A, N, M, i, j)

get_neighbors = {'+': plus_neighbors, 'x': cross_neighbors, '*': star_neighbors}

def solve():
    M, N = [int(i) for i in input().split()]
    A = [input().strip() for _ in range(N)]
    sol = []
    for symbol in ('+', 'x', '*'):
        visited = set()
        total = 0
        get_neigh = get_neighbors[symbol]
        for i in range(N):
            for j in range(M):
                if ((i, j) in visited) or (A[i][j] == '0'):
                    continue
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for k, l in get_neigh(A, N, M, x, y):
                        if (k, l) not in visited:
                            queue.append((k, l))
                            visited.add((k, l))
                total += 1
        sol.append(str(total))
    print(' '.join(sol))


def main():
    N = int(input())
    for _ in range(N):
        solve()

if __name__ == "__main__":
    main()