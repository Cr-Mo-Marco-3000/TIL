# Array 2

## 2차원 배열

- 2차원 배열의 선언

  - 1차원 list를 묶어놓은 list
  - 2차원 이상의 다차원 list는 차원에 따라 Index를 선언
  - 2차원 List의 선언: 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
  - Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

  - `arr = [[0,1,2,3],[4,5,6,7]]` (2행 4열의 2차원 list)

| 0    | 1    | 2    | 3    |
| ---- | ---- | ---- | ---- |
| 4    | 5    | 6    | 7    |



- 2차원 배열을 파이썬에서 받는 법

```python

'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)


'''
3
123
456
789
'''

# 단 서버에 windows format text가 올라와 있으면 오류가 난다.
N = int(input()) 
arr = [list(map(int, input())) for _ in range(N)]
print(arr)


```



- 배열 순회
  - n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

```python
# i 행의 좌표
# j 열의 좌표
# 일반적으로 i행 j열로 표현
# 우리가 저장할 때는 0번부터 시작하지만, 문제에서 언급될 때는 1번 행이라 표현할 때도 있으니 주의!
for i in range(n):
    for j in range(m):
        arrayp[n][m] # 필요한 연산 수행
```



- 주의!

```python
# 주의!
arr = [[0] * 3] * 4
print(arr)
arr[0][1] = 1
print(arr)
# 이렇게 하면 안됨!
# [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
# 이렇게 나옴 => 같은 객체를 참조하기 때문
```



- 열 우선 순회

```python
# 열 우선 순회
# i 행의 좌표
# j 열의 좌표
for j in range(m):
    for i in range(n):
        arr[i][j] # 필요한 연산 수행
        
for i in range(n):
    for j in range(m):
        arr[j][i] # 이렇게도 가능
```



- 지그재그 순회

```python
# 지그재그 순회
# 처음에는 열을 왼쪽부터, 다음에는 오른쪽부터 순회
for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]
# 역순회의 열 인덱스는 m-1-j이므로, 이게 나타나게 하기 위해(j + m - 1 - 2j) = m-1-j
# i가 1, 3, 5 등 홀수열(인덱스는 0, 2, 4) 일때는 * 0을 해줌)
```



- 1행 1열에 전부 0 붙이기
  - 실제 인덱스와 문제에서의 인덱스를 일치시키기 위해
  - 연산을 하기보다는 인덱스 자체를 저장할 때부터 고정

```python
N = int(input())

arr2 = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]
print(arr2)
```



- 델타를 이용한 2차 배열 탐색
  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
  - 주변에 0, 1, 2, 3 각각 방향을 정해놓고 움직이면 편하다.
  - 어떻게 방향을 잡던지, 연속적으로 90도씩 돌아가도록 하는 게 편하다.

```python
arr[0 ... N-1][0 ... N-1] # NxN배열
# 우 하 좌 상(direction)를 외부에 만들어 연산
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for k in range(4):
	ni = i + di[k]
	nk = j + dj[k]
    if 0 <= ni < N and 0 <= nj < M: # 유효 인덱스 범위(0과 N, M을 벗어나면 안 되므로)
        arr[ni][nj] 				# if문으로 쓸 수도 있지만... 귀찮다.

        
# 이렇게 하는 방법도 있다.
for di, dj in[(0,1), (1,0), (0, -1), (-1, 0)]:
    ni = i + di
    nj = j + dj
    if 0 <= ni < N and 0 <= nj < M: # 유효 인덱스
        arr[ni][nj]
```

```python
# 실제 예시
arr = [[1,2,3], [4,5,6], [7,8,9]]

N = 3
for i in range(N):
    for j in range(N): # 상하좌우
        for di, dj in[(-1,0), (1,0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, arr[ni][nj])
        print()
```

