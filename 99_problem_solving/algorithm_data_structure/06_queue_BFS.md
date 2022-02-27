# Queue



## 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에서는 삽입만, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조(FIFO)

- 큐의 선입선출구조
  - 머리(Front): 저장된 원소 중 첫 번째 원소: 마지막으로 삭제된 위치
  - 꼬리(Rear): 저장된 원소 중 마지막 원소: 마지막으로 저장된 위치
- 큐의 기본 연산
  - 삽입: enQueue
  - 삭제: deQueue
- 큐의 사용을 위해 필요한 주요 연산
  - enQueue(item)
  - deQueue()
  - createQueue()
  - isEmpty()
  - isFull()
  - Qpeek()

- front = rear
  - queue가 비어 있는 상태



## 선형큐

- 1차원 배열을 이용한 큐
  - 큐의 크기 = 배열의 크기
  - front: 저장된 첫 번째 원소의 인덱스: 마지막으로 꺼내진 위치
  - rear: 저장된 마지막 원소의 인덱스: 마지막으로 저장된 위치
- 상태 표현
  - 초기 상태: front = rear = -1
  - 공백 상태: front == rear
  - 포화 상태: rear == n-1(n: 배열의 크기, n-1: 배열의 마지막 인덱스)

- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front와 rear을 -1로 초기화
- 삽입: enQueue(item)
  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
    2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장

```python
def Queeue(item):
    global rear
    if isFull():
        print(Queue )
```

- 삭제: deQueue()
  - 가장 앞에 있는 원소를 삭제하기 위해
    1) front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
    2) 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함(뺀다기 보다는 접근한다 생각)
- 공백상태, 포화상태(isEmpty(), isFull())
  - 공백상태: front = rear
  - 포화상태: rear == n-1(n: 배열의 크기, n-1: 배열의 마지막 인덱스)

- 검색: Qpeek()
  - 가장 앞에 있는 원소를 검색하여 반환하는 연산
  - 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환
- 큐를 구현하여 다음 동작을 확인해 봅시다.
  - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고, 큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
    - 1, 2, 3이 출력 되어야 함

```python
front = -1
rear = -1
Q = [0] * 10
rear += 1
Q[rear] = 1

front += 1
print(Q[front])
front += 1
print(Q[front])
```

- 선형 큐 이용시의 문제점
  - 잘못된 포화상태 인식
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열(list 말고 길이가 고정된 array)의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n-1인 상태, 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
  - 해결방법 1(X)
    - 매 연산이 이루어질 때 마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
  - 해결방법 2(O)
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
    - 원형 큐(순환 큐)의 논리적 구조
      - rear가 배열의 끝으로 간 이후에, 인덱스를 맨 앞으로 되돌리는 방식



## 원형 큐

원형 큐의 구조

- 초기 공백 상태
  - front = rear = 0
- Index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
  - 이를 위해 나머지 연산자 mod를 이용
- 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 초기 위치
  - front == rear == 0
- 초기 공백 큐 생성



- 공백상태: front = rear
- 포화상태: 삽입할 rear의 다음 위치 == 현재 front
  - (rear) + 1 mod n == front(n은 배열의 길이)



## 우선순위 큐



- 우선순위 큐의 특성

  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

  

- 우선순위 큐의 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링

  

- 우선순위 큐의 구현
  - 배열을 이용한 우선순위 큐
  - 리스트를 이용한 우선순위 큐

  

- 배열을 이용하여 우선순위 큐 구현 & 문제점

  - 배열을 이용하여 자료 저장
  - 원소를 삽입하는  과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
  - 문제점
    - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생함
    - 이에 소요되는 시간이나 메모리 낭비가 큼



## 큐의 활용



- 버퍼
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링: 버퍼를 활용하는 방식



- 버퍼의 자료 구조
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다
  - 순서대로 입력/출력/전달되어야 하므로 FIFO방식의 자료구조인 큐가 활용된다.



## BFS



- 그래프를 탐색하는 방법에는 크게 두 가지가 있음
  - 깊이 우선 탐색(DFS)
  - 너비 우선 탐색(BFS)

  

- 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용함

- 탐색 순서

- A B C D E F G H I

- 연습문제: 미로의 거리

```python
# bfs로 최단거리 찾기

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
	return -1, -1  # 뭔가 잘못됐을 때 파악하기 위해 지정

def bfs(i, j, N):
	visited = [[0] * N for _ in range(N)] # 미로의 크기만큼 생성
    queue = [] 				# 큐 생성
    queue.append((i,j)) 	# 시작점 enQueue
    visited[i][j] = 1 		# 시작점 방문표시
    while queue:			# 큐가 비어있지 않으면 반복
        i, j = queue.pop()	# t <= deQueue
        if maze[i][j] == 3:
            return visited[i][j] - 2 # 출발 도착 칸 제외		
        for di, dj in [[0,1]. [1,0], [0,-1], [-1,0]]:
            ni, nj = 1+di, j+dj 	 # 주변 칸 좌표, 미로를 벗어나지 않고, 인접(벽이 아님)
            # 벽이 아닌 곳 != 1 아래 maze[ni][nj] != 1 조건은 벽이 아닌 곳
            # ni, nj 범위 지정이 앞에 나와야 인덱스 에러가 안남!
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] = 0:
                queue.append((ni, nj)) # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착지를 찾지 못한 경우            
 
T = int(input())


for tc in range(1, T+1):
    N = int(input()) # 크기정보
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 좌표 => 함수 생성해서 지정 => 
    sti, stj = fstart(N)
    print(sti, stj) # 뭔가 잘못됐을 때 파악하기 위해 지정
    ans = bfs(sti, stj, N) # bfs를 만들어보자!
    print(f'#{tc} {ans}')
    
# 사방을 1(벽)으로 둘러싸면 인덱스 확인이 좀 더 간편하다.
# 최단 거리만 찾고 끝나게 될 경우, 출구가 있는지 찾고 끝나게 될 경우 bfs가 더욱 간단하게 된다.
# 출발지가 한 곳이 아니어도 된다.
```

- bfs의 특징
  - 가까이 있는 곳들부터 탐색
    - 어느 곳 까지 갈 때 어느정도의 자원이 필요한지 파악이 가능하다.

  - 최단 거리만 찾고 끝나게 될 경우, 출구가 있는지 찾고 끝나게 될 경우 bfs가 더욱 간단하게 된다.
  - 출발지가 여러 곳이어도 된다.
  - BFS는 무조건 가까운 것 순으로 처리하기 때문에,  최소경로를 위해 비교할 필요 없지만
  - DFS는 가능한 순서대로 진행하기 때문에, 비교가 필요하다.


```python
# 재귀 DFS로 구현

def dfs(i, j, N, c): 		# c는 지나온 칸 수
    global minV
    if maze[i][j] == 3:		# 목적지에 도착하면 최소거리와 비교
        if minV > c:		# 
            minV = c
    # elif c > minV:
        # return
    else: 					# visited를 만드는 대신, 1로 변경해준다.
		maze[i][j] = 1 			
        for di, dj in [[0, 1], [1,0], [0,-1], [-1,0]]:
            ni nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1:
                dfs(ni, nj, N, c+1)
        # 1로 메꾼 걸 지워 주어야, 다른 경로 탐색 중 겹칠 때 그냥 통과한다.
        maze[i][j] = 0 # 갈 수 있나 없나만 체크할 때는 이걸 지워주어도 된다.


for tc in range(1, T+1):
    N = int(input()) # 크기정보
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 좌표 => 함수 생성해서 지정
    sti, stj = fstart(N)
    
    minV = 10000
    dfs(sti, stj, N, 0) # 마지막 자리는 문제 조건에 따라 0 또는 1
    if minV == 10000:
        minV == 1
    print(f'#{tc} {minV-1}')
```

```python
# 도착했나 안했나 확인만 하기, 끝까지 순환

def dfs(i, j, N, c): 		# c는 지나온 칸 수
    global minV
    if maze[i][j] == 3:		# 목적지에 도착하면 최소거리와 비교
        ans = 1
    else: 					# visited를 만드는 대신, 1로 변경해준다.
		maze[i][j] = 1 			
        for di, dj in [[0, 1], [1,0], [0,-1], [-1,0]]:
            ni nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1:
                dfs(ni, nj, N, c+1) 
		# maze[i][j] = 0 다른 경로로 갈 필요가 없으므로


for tc in range(1, T+1):
    N = int(input()) # 크기정보
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 좌표 => 함수 생성해서 지정
    sti, stj = fstart(N)
    
    dfs(sti, stj, N, 0) # 마지막 자리는 문제 조건에 따라 0 또는 1
    if minV == 10000:
        minV == 1
    print(f'#{tc} {minV-1}')
```

```python
# return값으로, 경로가 존재하는지 확인만 하기 => 내가 구현하려다 실패한 방식
def dfs(i, j, N): 		
    if maze[i][j] == 3:		# 찾으면 중단하는 경우
        return 1			
    else: 					
		maze[i][j] = 1 			
        for di, dj in [[0, 1], [1,0], [0,-1], [-1,0]]:
            ni nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1:
                if dfs(ni, nj, N):
                    return 1
    	return 0
for tc in range(1, T+1):
    N = int(input()) # 크기정보
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 좌표 => 함수 생성해서 지정 => 
    sti, stj = fstart(N)
    ans = dfs(sti, stj, N)
    print(f'#{tc} {ans}')
# 한 노드 아래에서, 모든 경로가 0을 return할 때, 상위 노드로 올라가 다른 노드를 탐색해야 하므로
```

- dfs에서 스택을 썼던 이유는

  - 갈 수 있는한 끝까지 가고
  - 돌아오기 위해 스택에 보관

- bfs는 내가 가야할 곳에 넣는다!

