# 트리

[toc]

## 1. 트리



> 트리의 개념

- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조



> 트리의 정의

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다.
  - 노드 중 최상위 노드를 루트 라 한다.
  - 나머지 노드들은 (n>=0)개의 분리 집합 T1, ....,TN으로 분리될 수 있다.
- 이들 T1, ..., TN들은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다.



> 트리 용어 정리

- 노드(node) - 트리의 원소
  - 트리 T의 노드 - A, B, C, D, E, F, G, H, I, J, K
  - 간선(edge) - 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
  - 루트 노드(root node) - 트리의 시작 노드
    - 트리 T의 루트 노드 - A
- 형제 노드(sibling node) - 같은 부모 노드의 자식 노드들
  - B, C, D 는 형제 노드
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  - K의 조상 노드: F, B, A
- 서브 트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 사위 레벨의 노드들
  - B의 자손 노드 - E, F, K
- 차수(degree)
  - 노드의 차수: 노드에 연결된 자식 노드의 수
    - B의 차수 = 2, C의 차수 = 1
  - 트리의 차수: 트리에 있는 노드의 차수 중에서 **가장 큰 값** - 노드들 중 자식이 최대 몇 개가 있는가?
    - 트리 T의 차수 = 3
  - 단말 노드(리프 노드): 차수가 0인 노드. 자식 노드가 없는 노드

- 높이
  - 노드의 높이: **루트에서 노드에 이르는** 간선의 수. 노드의 **레벨**
    - B의 높이 = 1, F의 높이 = 2
  - 트리의 높이: 트리에 있는 노드의 높이 중에서 **가장 큰 값**. **최대 레벨**
    - 트리 T의 높이 = 3
  - 상대적인 개념이라서, 어떤 책에서는 높이 0이 아니라 1부터 시작하는 경우도 있다.



## 2. 이진 트리

### 1. 이진 트리

> 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드(left child node) - 자식 1
  - 오른쪽 자식 노드(right child node) - 자식 2



> 이진트리의 특성

- 레벨 i에서의 노드의 최대 개수는 2^i^ 개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2 ^h+1^ - 1)개가 된다.



### 2. 이진 트리의 종류

> 포화 이진 트리(Full Binary Tree)

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대의 노드 개수인 (2^h+1^ - 1)의 노드를 가진 이진 트리
  - 높이 3일 때 (2^3+1^ - 1) = 15 개의 노드
- 루트를 1번으로 하여 (2^h+1^ - 1)까지 정해진 위치에 대한 노드 번호를 가짐



> 완전 이진 트리(Complete Binary Tree)

- 얘는 정의를 기억해 두는게 좋음

- 높이가 h이고 노드 수가 n개일 때 (단, h+1 <=n < 2^h+1^ - 1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
- 간선의 개수는 항상 n - 1



> 편향 이진 트리(Skewed Binary Tree)

- 높이 h에 대한 최소 개수의 노드를 가지면서 한 쪽 방향의 자식 노드만을 가진 이진 트리
  - 왼쪽 편향 이진 트리
  - 오른쪽 편향 이진 트리



### 3. 이진 트리의 순회



> 순회

- 순회(traversal)
  - 트리의 노드들을 체계적으로(빠짐없이) 방문하는 것
  -  트리의 각 노드를 중복되지 않게 전부 방문(visit) 하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
  - 따라서 특별한 방법이 필요하다.
- 3가지의 기본적인 순회방법
  - **전, 중, 후는 부모 노드를 언제 방문하느냐를 말하는 것이다.**
  - 전위순회(preorder traversal): VLR
    - 부모노드 방문(처리) 후, 자식노드를 좌, 우 순서로 방문(처리)한다.
  - 중위순회(inorder traversal): LVR
    - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문(처리)한다.
  - 후위순회(postorder traversal): LRV
    - 자식 노드를 좌 우 순서로 방문한 후, 부모노드로 방문(처리)한다.



> 전위 순회(preorder traversal) - **중요**

- 수행 방법
  1) 현재 노드 n을 방문하여 처리한다. => V
  2) 현재 노드 n의 왼쪽 서브트리로 이동한다. => L
  3) 현재 노드 n의 오른쪽 서브트리로 이동한다. => R
- 전위 순회 알고리즘
  - 자식이라고 T를 받았는데 T로 들어갔을 때 해당 T 노드가 존재하지 않을 경우, if 문 안을 수행하지 않고 되돌아감
- 일차원 배열로 이진 트리 표현 시 전위 순회 예

```python
def pre_order(v):
    if v: # v is not None - 노드가 존재한다면
        print(v) # 부모 출력
        pre_order(2*v) # 왼쪽 자식 확인
        pre_order(2*v + 1) # 오른쪽 자식 확인

pre_order(1)
```





> 중위 순회(inorder traversal)

- 수행 방법
  1) 현재 노드 n의 왼쪽 서브트리로 이동한다. => L
  2) 현재 노드 n을 방문하여 처리한다. => V
  3) 현재 노드 n의 오른쪽 서브트리로 이동한다. => R 
- 중위 순회 알고리즘
  - 왼쪽에서 리턴할 경우, 부모 노드를 visit
- 중위 순회 예

```python
def pre_order(v):
    if v:
        pre_order(2*v)
        print(v)
        pre_order(2*v + 1)

pre_order(1)
```





> 후위 순회(postorder traversal)

- 수행 방법
  1. 현재 노드 n의 왼쪽 서브트리로 이동한다 => L
  2. 현재 노드 n의 오른쪽 서브트리로 이동한다 => R
  3. 현재 노드 n을 방문하여 처리한다 => V

- 후위 순회 알고리즘
  - 오른쪽에서 리턴할 경우, 부모 노드를 visit

- 후위 순회 예

```python
def pre_order(v):
    if v:
        pre_order(2*v)
        pre_order(2*v + 1)
		print(v)
        
pre_order(1)
```



### 4. 이진 트리의 표현



#### 1) 1개 배열을 이용한 이진 트리의 표현

> 일차원 배열을 이용한 이진 트리의 표현

- 이진 트리에 각 노드 번호를 다음과 같이 부여
- 루트의 번호를 1로 함
- 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽 2^2^ 부터 2^n+1^-1까지 번호를 차례로 부여
- 포화 이진 트리와 완전 이진 트리에 적용 가능



> 노드 번호의 성질

- 노드 번호가 i인 노드의 부모 노드 번호 => i // 2
- 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 => 2*i
- 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 => 2*i + 1
- 레벨 n의 노드 번호 시작 번호는? 2^n^



> 표현 방법

- 노드 번호를 배열의 인덱스로 사용
- 높이가 h인 이진 트리를 위한 배열의 크기는?
  - 레벨 i의 최대 노드 수는? 2^i^
  - 따라서 1 + 2 + 4 + ... 2^i^ = 2^h+1^-1
  - 이론상으로 이렇고, 만약 100개 노드를 저장해야 한다 이러면 101짜리 배열을 만들면 됨



#### 2) 2개 배열을 이용한 이진 트리의 표현

> 이진 트리의 저장

- 부모 번호를 인덱스로 자식 번호를 저장
  - 두 개의 일차원 배열, 혹은 이차원 배열이 필요(자식은 2 개니까)

  > 참고: 주의할 점!
  >
  > 최소 포화 이진 트리의 경우 1번이 루트, 번호: 부모<자식 관계이지만
  >
  > 그 외의 트리의 경우에는 1번이 루트라는 보장이 없고, 루트를 직접 찾아야 하는 경우도 있다.

```python
'''
4
1 2 1 3 3 4 3 5
'''
E = int(input())
temp = list(map(int, input().split()))

V = E + 1

arr_1 = [0] * (V+1)
arr_2 = [0] * (V+1)

# 부모 번호를 인덱스로 자식 번호 저장
for i in range(E):
    p = temp[2*i]
    c = temp[2*i + 1]
    if not arr_1[p]:
        arr_1[p] = c
    else:
        arr_2[p] = c

```



- 자식 번호를 인덱스로 부모 번호를 저장

```python
'''
4
1 2 1 3 3 4 3 5
'''
E = int(input())
temp = list(map(int, input().split()))

V = E + 1

par = [0] * (V + 1)

for i in range(E):
    p, c = temp[2*i], temp[2*i+1]
    par[c] = p
    
```



- 루트 찾기, 조상 찾기

```python
'''
4
1 2 1 3 3 4 3 5
'''
E = int(input())
temp = list(map(int, input().split()))

V = E + 1

par = [0] * (V + 1)

for i in range(E):
    p, c = temp[2*i], temp[2*i+1]
    par[c] = p



# ex) 5번 노드의 조상 찾기

c = 5
ancestors = []

while par[c] != 0:
    ancestors.append(par[c]) # 자식 번호를 인덱스로 부모 노드를 저장한 상태에서 거슬러 올라가며 부모 노드를 저장
    c = par[c]
    
root = c # 0이 아닌 마지막 부모 노드가 루트가 됨
```



- 배열을 이용한 이진 트리의 표현의 단점
  - 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적



#### 3) 연결리스트를 활용한 트리의 표현

- 배열을 이용한 이진 트리 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있따.
- 연결 자료구조를 이용한 이진트리의 표현
  - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여 구현

```python
# 왼쪽 자식 노드, 데이터, 오른쪽 자식 노드 식으로 아래와 같이 구현
# 
nod = [0, 0, 0]
```



> 참고: 수식 트리

- 수식을 표현하는 이진 트리
- 수식 이진 트리(Expression Binary Tree)라고 부르기도 함.
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드

- 순회를 이용하여 계산



## 3. 이진 탐색 트리

> 이진 탐색 트리

- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다
- 왼쪽 서브트리 < 루트 노드 < 오른쪽 서브트리
- 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.
- 즉 어떤 노드를 기준으로, 왼쪽 값들은 모두 노드보다 작은 값, 오른쪽은 큰 값이다.



> 탐색연산

- 루트에서 시작
- 탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
  - 값 x == 루트노드 키값: 원하는 원소를 찾았으므로 탐색연산 성공
  - 값 x < 루트노드 키값: 루트노드의 왼쪽 서브트리에 대해서 탐색연산 수행
  - 값 x > 루트노드 키값: 루트노드의 오른쪽 서브트리에 대해서 탐색연산 수행

- 서브트리에 대해서 순환적으로 탐색 연산을 반복한다.



> 삽입 연산

- 먼저 탐색 연산을 수행
  - 삽입할 원소와 같은 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인한다.
  - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다.



> 성능

- 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다.
  - O(h)
    - h: BST의 깊이(height)
- 총 노드의 개수를 n이라고 했을 때,
  - 평균의 경우
    - 이진 트리가 균형적으로 생성되어 있는 경우
    - O(log n)
  - 최악의 경우
    - 한쪽으로 치우친 경사 이진트리의 경우
    - O(n)
    - 순차탐색과 시간복잡도가 같다.



> 검색 알고리즘의 비교

- 배열에서의 순차 검색: O(N)
- 정렬된 배열에서의 순차 검색: O(N)
- 정렬된 배열에서의 이진탐색: O(log n)
  - 고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
- 이진 탐색트리에서의 평균: O(log n)
  - 최악의 경우: O(N)
  - 완전 이진 트리 또는 균형트리로 바꿀 수 있다면 최악의 경우를 없앨 수 있다.
    - 새로운 원소를 삽입할 때 삽입 시간을 줄인다.
    - 평균과 최악의 시간이 같다. O(N)
  - 해쉬 검색: O(1)
    - 추가 저장 공간이 필요.



## 4. 힙

> 힙

- **완전 이진 트리**에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
- 최대 힙(max heap)
  - 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  - 부모노드의 키값 > 자식노드의 키값
  - 루트 노드: 키값이 가장 큰 노드
- 최소 힙(min heap)
  - 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - 부모노드의 키값 < 자식노드의 키값
  - 루트 노드: 키값이 가장 작은 노드



> 힙의 삽입, 삭제

- 힙에서는 루트 노드의 원소만을 삭제할 수 있다!

```python
"""
최소힙의 조건
1. 완전 이진 트리
2. 자식 < 부모 (왼쪽 & 오른쪽 자식의 크기 비교는 상관 없음)
"""

def heap_push(value):
    global heap_count
    """
    핵심) 완전 이진 트리의 조건에 위배되지 않도록 연산 수행
    1. Tree의 가장 마지막에 요소 삽입
    2. 삽입된 노드와 부모 노드를 비교하여 swap
    3. 부모 노드보다 크거나/작고 and 루트 노드에 도달하기 전까지 반복
    """
    heap_count += 1                 # 값을 하나 늘리고
    heap[heap_count] = value        # 그 자리에 값을 쓰고
    child = heap_count              # child -> 항상 완전이진트리의 마지막에 추가
    parent = child // 2             # child의 부모 -> 자식 // 2 -> 해당 위치에서 부모와 대소 비교를 위해

    # 루트 노드가 아니고(parent가 0인 경우는 root 노드 뿐) & 부모 노드 값 > 자식 노드 값 => swap (min_heap을 만들어야 하기 때문에)
    while parent and heap[parent] > heap[child]:              # 부모가 0이 아니고(root가 아니고) / 부모 노드가 더 작을 때까지
        heap[parent], heap[child] = heap[child], heap[parent] # 자식 <-> 부모 교환
        child = parent                                        # child를 기존 부모를 가리키는 key로 설정 -> 부모와의 교환을 통해 올라온 key값을 child로 두고
        parent = child // 2                                   # parent는 기존 child를 가리키던 key로 교환 -> 해당 child 값의 부모를 다시 잡아 같은 행동을 반복

def heap_pop():
    global heap_count
    """
    핵심) 완전 이진 트리의 조건에 위배되지 않도록 연산 수행
    1. root 삭제 (최대힙이면 최댓값, 최소힙이면 최솟값이 반환)
     - heap에서는 루트의 원소만 삭제 가능
    2. Tree의 가장 마지막 요소를 root 자리로 이동 
    3. root 노드부터 시작해서 자식 노드 중 더 큰 값과 비교하며 swap 
    4. 조건을 만족하고 Tree의 가장 아래 도착할 때까지 반복
    """
    return_value = heap[1]      # root의 원소 백업하고 (return_value -> 하나의 for문에서 반환해야 하는 값)
    heap[1] = heap[heap_count]  # heap의 마지막 요소 값을 heap의 가장 위에 옮겨두고
    heap[heap_count] = 0        # heap의 마지막 요소는 0으로 변경(삭제)
    heap_count -= 1             # 마지막을 가리키는 위치 변경

    parent = 1                  # 최상단 노드부터 시작
    child = parent * 2

    if child + 1 <= heap_count:          # 오른쪽 자식이 존재하고(heap_count는 마지막 요소를 가리키는 인덱스) + (완전 이진 트리이기 때문에 오른쪽 자식이 없다는 건 제일 마지막을 의미)
        if heap[child] > heap[child+1]:  # 왼쪽과 오른쪽 자식의 크기를 비교해서 왼쪽 자식이 더 크다면
            child = child + 1            # 오른쪽 자식과 교환할 수 있도록 child의 값을 오른쪽 자식의 인덱스에 맞춰준다. (아니라면 왼쪽을 그대로 유지)
                                         # (참고 - 더 작은 자식을 찾아 그 값과 바꾸는 이유는 큰 값과 변경하게되면 최소힙 조건을 유지할 수 없기 때문)

    while child <= heap_count and heap[parent] > heap[child]:   # 자식 노드가 하나라도 존재하고, 부모 노드가 > 자식 노드  -> swap
        heap[parent], heap[child] = heap[child], heap[parent]   # 부모 자식 노드 swap
        parent = child                                          # 기존 자식을 부모로
        child = parent * 2                                      # 자식을 부모로

        if child + 1 <= heap_count:           # 오른쪽 자식이 존재하고 (완전 이진 트리이기 때문에 오른쪽 자식이 없다는 건 제일 마지막을 의미)
            if heap[child] > heap[child+1]:   # 왼쪽과 오른쪽 자식의 크기를 비교해서 왼쪽 자식이 더 크다면
                child = child + 1             # 오른쪽 자식과 교환할 수 있도록 child의 값을 오른쪽 자식의 인덱스에 맞춰준다. (아니라면 왼쪽을 그대로 유지)
    return return_value

heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)             # 크기 설정 (+1은 인덱스를 노드 번호에 맞추기 위해서 설정)

#1. heap push
for i in range(N):
    heap_push(nums[i])         # 인덱스 0번에 해당하는 노드부터 heap_push 연산 수행
print(*heap)                   # 0 2 3 5 7 4 6

#2. heap pop
for i in range(N):             # 삭제 - 루트 노드
    print(heap_pop(), end=' ') # 2 3 4 5 6 7
```
