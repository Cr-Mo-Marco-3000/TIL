# DFS

- 그래프
  - 종류
    - 유향 그래프
    - 무향 그래프
    - 가중치 그래프
    - 사이클 없는 방향 그래프
      - 시작한 정점에서 끝나는 경로를 사이클(Cycle)이라고 한다.




- 그래프의 구성 요소
  - 노드 == 정점 == 버텍스
  - 엣지 == 간선



- 그래프 표현
  - 인접 행렬
    - V X V, 혹은 (V + 1) X (V + 1) 크기의 2차원 배열을 이용해서 간선 정보를 저장
    - 배열의 배열(포인터 배열)
  - 인접 그래프
    - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
  - 간선의 배열
    - 간선(기작 정점, 끝 정점)을 배열에 연속적으로 저장



- 그래프 탐색

  - 그래프 탐색의 종류

    - 비선형적인 구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함

    - 두 가지 방법
      - DFS: 깊이 우선 탐색
      - BFS: 너비 우선 탐색, 나중에 배움

  - DFS(깊이 우선 탐색)

    - 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

    - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

    - 지나온 과거를 어딘가에(stack) 기록

      

- 과정

  - stack과 visited array가 필요하다.

  1) 시작 정점 v를 결정하여 방문한다
  2) 정점 v에 인접한 정점 중에서
     1) 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2)를 반복한다.
     2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
     3) 스택이 공백이 될 때까지 2)를 반복한다.

- 표현

  - 셋 중 하나의 방식으로 표시

  - 인접 행렬

  - 인접 리스트

  - 딕셔너리

  - 2차원 배열로, 1과 2가 연결되어 있다면 출발행, 도착열 행렬에 1을 표시(방향이 있다면)

    - 방향이 없다면, 출발행 도착행을 나누지 않고 전치되는 좌표에도 1을 표시

  - 2차원 배열, 배열의 idx 1번(0번부터 시작할 때는 0번)부터 그 노드와 연결된 노드들을 저장하는 방식

    

  

- 계산기

  - 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
  - 문자열 수식 계산의 일반적 방법
    - 중위 표기식
    - 후위 표기식

- step1. 중위 표기법에서 후위







- 백트래킹
  - 백트래킹 기법은 해를 찾는 도중에 막히면(즉 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.
  - 백트래킹 기법은 최적화 문제와 결정 문제를 해결할 수 있다.
  - 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 yes 또는 no가 답하는 문제



- 미로 찾기
  - 아래 그림과 같이 입구와 출구가 주어진 미로에서 입구부터 출구까지의 경로를 찾는 문제이다
  - 이동할 수 있는 방향은 4방향으로 제한한다.



- 백트래킹과 깊이우선탐색과의 차이

  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Prunning 가지치기)
  - 깊이우선탐색이 모든 경로를 추적하는 데 비해 백트래킹은 불필요한 경로를 조기에 차단.
  - 깊이우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제.
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능
  - 백트래킹은 모든 후보를 검사하지 **않는다!**
  - 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
  - 가지치기: 유망하지 않은 노드가 포함된 경로는 더 이상 고려하지 않는다.

  

- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행된다

  - 상태 공간 트리의 깊이 우선검색을 실시한다.
  - 각 노드가 유망한지를 점검한다.
  - 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

  

- 백트래킹을 이용한 부분집합 구하기

```python
def f(i, N, K): # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소 개수
    if i == N: # 한개의 부분집합 완성
        # print(bit, end = ' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += a[j]
                # print(a[j], end = ' ')
        print(s) # 부분집합의 합
        if s == K: # 만약 부분집합의 합이 내가 찾는 K라면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
    else: # 갈림길이 2개로 생기는 애들은, 2번 호출하게 된다.
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
    	f(i+1, N, K)
    return
    
a = [1, 2, 3, 4, 5, 6, 7, 8]
bit=[0, 0, 0, 0, 0, 0, 0, 0]
N = len(a)
f(0, 3, 10)
```



- 집합 {1, 2, 3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현





## 분할 정복 알고리즘

- 분할: 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복: 나눈 작은 문제를 각각 해결한다.
- 통합: (필요하다면) 해결된 해답을 모은다.



- 병합 정렬과 퀵 정렬에서 사용한다.

- 피봇을 중심으로 정렬을 해 나감
  - 피봇: 배열 내 임의의 원소
  - 피봇을 선택하는 방법에 차이는 있지만, 임의의 원소를 고른다면 상관이 없다.
