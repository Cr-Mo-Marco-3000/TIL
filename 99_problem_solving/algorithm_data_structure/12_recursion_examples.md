# 재귀

- 재귀 함수를 다룰 때, 내부 구조가 똑같이 생긴 서로 다른 함수를 호출한다고 생각하자.
- 내가 현재 어디인지, 어디까지 가야 하는지 판단하자.

```python
# 재귀 기본

def func(i, N):
    if i == N:
        return
    else:
        f(i+1, N)
```

```python
# A를 B에 복사
A = (10, 20, 30)
B = [0, 0, 0]

def func(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)
        
```

```python
# A에 v=5가 있으면 1 리턴, 없으면 -1 리턴

def f(i, N, v):
    if i == N:				# 배열을 벗어난 경우, 검색 실패
        return -1
    elif A[i]==v:
        return 1
    else:					# 배열을 벗어나지 않고 검색 실패한 경우
        return f(i+1, N, v) # 리턴값을 다시 리턴
       

A = (7, 2, 5, 4, 1, 3)
N = len(A)
v = 5
print(f(0, N, v))
v = 9
print(f(0, N, v))
```

```python
# A => [0, 0, 0] 각 자리에 0 또는 1을 집어 넣는 경우


def func(i, N):
    if i == N:
        print(A)
    else:
        a[i] = 0
        func(i+1, N)
        a[i] = 1
        func(i+1, N)

def func2(i, N):
    if i==N:
        print(A)
    else:
        for j in range(2):
            A[i] = j
            f(i+1, N)
        
        
N = 3
A = [0] * N
func(0, N)
```

```python
# 1, 2, 3 중복사용해 3자리수 만들기

def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(1, 4):
            A[i] = j
            f(i+1, N)
            
N = 3
A = [0] * N
func(0, N)
```

```python
# 1~k 를 중복 사용해 3자리수 만들기
# 갈림길의 개수는 k에 영향, 깊이는 N에 영향

def f(i, N, k):
    if i == N:
        print(A)
    else:
        for j in range(1, k + 1):
            A[i] = j
            f(i+1, N, k)
            
N = 3
k = 5
A = [0] * N
func(0, N)
```

```python
# 1~k 를 중복 사용해 3자리수 만들기
# 세자리 수 v 값을 만들 수 있으면 중단하고 1 리턴, 없으면 0 리턴
# 111 <= v

def f(i, N, k, v):
    if i == N:
        s = A[0]* 100 + A[1] * 10 + A[2]
        # print(s)
        if s==v:
            return 1
        else:
            return 0
    else:
        for j in range(1, k + 1):
            A[i] = j
            # 다 돌지 않고 값을 발견시 return값을 이용해 중단하는 방법
            if f(i+1, N, k, v):
                return 1
        return 0
            
N = 3
k = 5
A = [0] * N
v = 123
func(0, N)
```

```python
# A의 부분집합중 합이 K인 부분집합의 개수 구하기
def func(i, N, s, K): # s i-1 원소까지 고려된 부분집합의 합
    global cnt
    if i==N:
        if s == K:  #끝에서 for를 돌려 합을 구할 필요 없어 시간단축
            cnt += 1
    elif s > K:
        return
    else:
        f(i+1, N, s + A[i], K) # A[i] 포함
        f(i+1, N, s, K)    


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 55
cnt = 0
N = len(A)
f(0, N, 0, K)
```

