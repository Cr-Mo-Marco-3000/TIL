import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())



def do(r, c, length, k):

    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N:
            if g[nr][nc] <= g[r][c]:
                length += 1


for tc in range(1, T+1):
    N, K = map(int, input().split())
    top = 0
    g = []
    max_length = 0
    # 최대높이 리스트
    max_list = []
    # 그래프 생성
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for _ in range(N):
        temp = list(map(int, input().split()))
        temp_max = max(temp)
        if temp_max > top:
            top = temp_max
        g.append(temp)
    # 최대높이 넣기
    for i in range(N):
        for j in range(N):
            if g[i][j] == top:
                max_list.append([i, j])
    visited = [[0] * N for _ in range(N)]
    for k in max_list:
        do(max_list[0], max_list[1], 0)

