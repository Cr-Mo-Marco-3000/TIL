# 최소신장트리

## 최소 신장 트리

- 그래프에서 최소 비용 문제

  1) 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리

  2) 두 정점 사이의 최소 비용의 경로 찾기

- 신장 트리

  - n 개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리

  - 무방향 가중치 그래프에서 신장 트리를 뽑아내서 그 신장 트리를 구성하는 간선들의 가중치의 합이 최소가 되는 신장 트리

- MST 표현 방법

  - 인접 그래프에서 연결되어 있지 않으면 0, 연결되어 있으면 가중치를 표시

  - 인접 리스트로 표현도 가능





## Prim 알고리즘

- 정점 중심
- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
  1) 임의 정점을 하나 선택해서 시작
  2) 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
  3) 모든 정점이 선택될 때 까지 1), 2) 과정을 반복
- 서로소인 2개의 집합 정보를 유지
  - 트리 정점들 - MST를 만들기 위해 선택된 정점들
  - 비트리 정점들 - 선택되지 않는 정점들



> 반복으로 구현

```python
"""
반복으로 구현

1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합
"""

def Prim():
    for _ in range(V):                      # 모든 정점이 MST에 포함될 때 까지 반복(마지막 요소 선택 여부)
        min_weight = 12345                  # 답을 sum(key)로 구하기 때문에 노드 개수만큼 반복할 필요 없다.
        min_index = -1                      

        # 1. MST에 연결된 노드들 중 최소 가중치 찾기
        for i in range(V+1):
            if not visited[i] and key[i] < min_weight:      # 아직 MST에 포함되지 않은 노드들 중 최소 비용 간선 찾기
                min_weight = key[i]                         
                min_index = i
        visited[min_index] = 1                              # 최소 비용 간선을 택해 그 노드를 체크

        # 2. 해당 값으로부터 연결된 정점 가중치 갱신
        for j in range(V+1):                                # min_index와 연결된 인접 행열 순환하며
            if not visited[j] and g[min_index][j] < key[j]: # 미선택 노드고 가중치가 기존 key의 가중치보다 작으면
                key[j] = g[min_index][j]                    # 즉 더 저렴하게 갈 수 있으면 갱신

    print(key)
    return sum(key)



import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())                            # 0부터 시작해서 V까지 V+1개의 정점

g = [[12345 for _ in range(V+1)] for _ in range(12345)]     # 그래프는 임의의 큰 값을 잡고 초기화(최소 신장 트리이므로)

visited = [0] * (V+1)                                       # 노드의 MST 포함 여부를 체크하기 위한 배열
key = [12345] * (V+1)                                       # MST 외부 노드들로의 간선들 중 최소 가중치 간선을 판단하기 위한 배열
key[0] = 0                                                  # 시작점 설정(시작점은 가중치가 0이므로)

for _ in range(E):                                          # 무향 그래프이므로 양쪽에 모두 가중치를 줌
    start, end, weight = map(int, input().split())
    g[start][end] = weight
    g[end][start] = weight

print(Prim())
```



> 힙으로 구현

```python
"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합

heap 활용하면 최솟값을 찾는 과정 생략 가능
 - min_heap을 구하면 root는 항상 최소 가중치 위치
 - heap_pop을 할 때마다 root에 있는 최소 가중치 반환
"""
def Prim():
    ans = 0                                             # ans 초기화
    heap = []                                           # 힙 리스트 초기화
    heapq.heappush(heap, (0, 0))                        # 힙에 시작 노드 추가(가중치, 노드번호), 둘 다 0
    while heap:                             
        w, v = heapq.heappop(heap)                      # w: 현재 가중치, v: 현재 정점 => 항상 최솟값 반환(최소힙 루트는 항상 최솟값)
        if not visited[v]:                              # 정점을 아직 방문 안했다면
            ans += w                                    # v까지 이동한 가중치 누적
            visited[v] = 1                              # 해당 정점을 방문하고, 선택해서 활용
            for n, weight in g[v]:                      # 인접 리스트에서 인접 정점
                if not visited[n]:                      # 그 정점을 아직 방문하지 않았다면
                    heapq.heappush(heap, (weight, n))   # v와 연결되어 있는 모든 (가중치, 인접 정점)을 추가
    return ans


import sys, heapq
sys.stdin = open('input.txt')


V, E = map(int, input().split())                        # V + 1개의 정점(0부터 시작)
visited = [0] * (V+1)                                   # 정점 방문 여부 체크
g = [[] for _ in range(V+1)]                            # 인접 리스트 구현

# 인접 리스트 구현
for _ in range(E):
    start, end, weight = map(int, input().split())      # 간선만큼(E) 돌면서 두 정점과 가중치를 받고 구현
    g[start].append([end, weight])                      # 무향 그래프 => (정점, 가중치) 형태로 추가
    g[end].append([start, weight])

print(Prim())
```

