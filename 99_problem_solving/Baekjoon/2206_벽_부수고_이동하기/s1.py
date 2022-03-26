from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10**6)


N, M = map(int, stdin.readline().rstrip().split())

def dfs(r, c, cnt):
    global flag
    global ans
    visited[r][c] = cnt
    if r == N-1 and c == M-1:
        if cnt <= ans:
            ans = cnt
        return
    elif cnt >= ans:
        return
    else:
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if g[nr][nc] == 1 and flag == 1:
                    flag = 0
                    do(nr, nc, cnt + 1)
                    visited[nr][nc] = 0
                    flag = 1
                elif g[nr][nc] == 0:
                    do(nr, nc, cnt + 1)
                    visited[nr][nc] = 0

def bfs(r, c):
    if g[r][c] == 1 and flag == 0:
        return
    elif g[r][c]:
        pass



# 0,0에서 N,M으로 이동


g = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
flag = 1
ans = (N-1) * (M-1)
dfs(0, 0, 1)
if ans == (N-1) * (M-1):
    print(-1)
else:
    print(ans)