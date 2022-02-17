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


'''교수님이 알려주신 방법'''
# 실전에서는 못씀

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

arr2 = [[0]*3 for _ in range(4)]
# 요렇게 하면 된다.
arr2[0][1] = 1
print(arr2)
# [[0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
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



- 델타를 이용한 2차 배열 탐색: 방향델타
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

```python
import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

r, c = 0, 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for k in range(4):
    nr = r + dr[k]
    nc = c + dc[k]
    print(nr, nc)
    #print(data[nr][nc]) : 파이썬이라서 작동함 => 음수 인덱스를 지원하기 때문

    #1 보통 이렇게 표현
    if 0 <= nr < N and 0 <= nc <N:
        # 이 경우에만 무언가를 하겠다.
        print(nr, nc)
        print(data[nr][nc])
    #2
    if nr < 0 or nr >= N and nc < 0 or nc >= N:
        continues
```



- 전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
      # if i > j:
      #		arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        
# 얘도 노 상관
# zip 함수를 사용할 수도 있다.
```



- 부분집합 문제
  - 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
  - 원소가 5개 => 32개의 부분집합
  - 부분집합의 수
    - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n^개
    - 각 원소별로 포함되거나 포함되지 않거나 2가지 상태가 존재하기 때문

- 부분집합 생성하기
  - 각 원소가 부분집합에 포함되었는지를 loop를 이용하여 확인하고 부분집합을 생성하는 방법

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

```python
A = [1, 2, 3]
bit = [0]* 3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            # print(bit)
            # 부분집합 출력
            # 원소의 수가 적을 때
            for p in range(3):
                if bit[p]:
                    print(A[p], end=" ")
            print()
```

​		

- 비트 연산자
  - 비트 연산: 같은 비트 자리 사이에서 연산을 함
  - `&` 비트 단위로 AND 연산을 한다
  - `|` 비트 단위로 OR 연산을 한다
  - `<<` 피연산자의 비트 열을 왼쪽으로 이동시킨다.
  - `>>` 피연산자의 비트 열을 오른쪽으로 이동시킨다.

- << 연산자
  - 1 << n: 2^n^ : 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
  - a = 1 << 5 : 5번 비트가 1인 값
- & 연산자
- i & (1<<j): i의 j번째 비트가 1인지 아닌지를 검사한다.
  - if i & (1 << j): i의 j번 비트가 1이면: 1, 0이면 0



- 보다 간결하게 부분집합을 생성하는 방법
  - python 코드 예

```python
arr = [3, 6, 7, 1, 5, 4]
# 6개 원소 -> 부분집합은 64개
n = len(arr) # n : 원소의 개수

for i in range(1 << n): # 1 << n : 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번 비트가 1인경우
            print(arr[j], end=", ") # j번 원소 출력
    print()
print()
```



## 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

- 목적하는 탐색 키를 가진 항목을 찾는 것

  - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키

- 검색의 종류

  - 순차 검색(sequential search)
  - 이진 검색(binary search)
  - 해쉬(hash)

  

### 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적인 검색 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  - 알고리즘이 단순하여 구현이 쉽지만, 겁색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임



1) 정렬되어 있지 않은 경우

   - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.

   - 키 값이 동
   - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
   - 첫 번째 원소를 찾을 때는 1번, 두 번째 원소를 찾을 때는 2번 비교
   - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
     - (1/n) * (1+2+3...+n) = (n+1)/2
     - 시간 복잡도 O(n)

```python
# 구현 예에서, while 문에 i<n이 먼저 와야 함! 그래야 index error가 안남!
# 즉 인덱스 범위와 배열의 내부를 같이 검사할 때는 인덱스 범위가 먼저 와야 한다.
# 나중에는 습관적으로 인덱스 범위를 먼저 설정하고 하게 된다.
# 내가 찾는 키값이 없는 경우에는 인덱스 에러가 난다.
```



2) 정렬되어 있는 경우
   - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자.
   - 자료를 순차적으로 검색하면서 키 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.



### 이진검색

- 자료의 가운데에 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서
- 이진 검색을 하기 위해서는 **자료가 정렬된 상태**여야 한다.
- 시간 복잡도
  - logn

​	

- 검색 과정

  - 자료의 중앙에 있는 원소를 고른다.

  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.

  - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.

  - 찾고자 하는 값을 찾을 때까지 1 ~ 3의 과정을 반복한다.

    

- 구현
  - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.
  - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열~
  - 재귀로도 구현 가능 but 이진 검색 알고리즘은 반복으로 하는 게 빠르다.(속도를 목적으로 이진 검색 하는데...)



### 인덱스

- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일걷는다.
- Database 분야가 아닌 곳에서는 Look up table등의 용어를 사용하기도 한다.
- 인덱스를 저장하는 데 필요한 디스크 공간은 보통 테이블을 저장하는데...
- 지금은 그냥 넘어가자



### 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례때로 선택하여 위치를 교환하는 방식
  - 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.
- 정렬 과정
  - 주어진 리스트 중에서 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

- 시간 복잡도
  - O(n^2^)
  - 이중 for문으로 구현 : 시간 복잡도가 n^2^ 이라고 생각하면 된다
- 얘는 기본적인 정렬이므로 외워라
- 버블과 선택 정렬의 차이점을 그림으로 그려서 설명할 수 있게 연습할 수 있어야 한다.



### 셀렉션 알고리즘

- k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 한다.



연습문제3

1. 델타 활용
2. 인덱스 활용