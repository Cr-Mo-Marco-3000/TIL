# 스택, 큐, 덱



[toc]



## 1. 스택

- LIFO: Last In First Out 형태

- 일반적인 리스트 구조와 같으므로 리스트를 쓰듯이 사용하면 된다.
- 즉 append, extend, pop 등의 메소드를 활용 가능하다.
- 맨 우측에 추가, 제거하는 것은 time complexity가 1이지만, 
- 좌측에 추가하는 것은 길이(n)만큼의 시간 복잡도를 지닌다.



## 2. 큐

- FIFO: First In First Out 형태

- 맨 좌측에서 빼는 것과 우측에 추가 할 때는 유용하지만, 그 외에는 덱의 하위호환이다.
- 그냥 덱을 쓰자. 파이썬에서도 그냥 덱을 쓰길 원하는 것 같다.



## 3. 덱

- Double-ended que의 줄임말로, 맨 좌측에 항목을 더하고 빼는 것과 맨 우측에 더하고 뺄 때 모두 time complexity가 1이다.
- 큐의 상위호환으로 유용하게 쓸 수 있으나, 중간에 있는 항목을 조작할 때는 유용성이 떨어진다.
- 덱의 선언방법 및 메소드들은 다음과 같다.



### 1. 선언방법

```python
from collections import deque
# 혹은 import collections를 한 뒤 변수를 선언시, collections.deque를 한다.

# dq = deque(iterable)
a  = deque([1, 2, 3, 4, 5])

print(a) # deque([1, 2, 3, 4, 5])
print(type(a)) # <class 'collections.deque'>

```



### 2. 좌우 끝 항목 추가/제거

```python
# dq.append(item) item을 덱의 오른쪽에 더한다.
a.append(6) # deque([1, 2, 3, 4, 5, 6])


# dq.appendleft(item): item을 덱의 왼쪽에 더한다.
a.appendleft(0) # deque([0, 1, 2, 3, 4, 5, 6])


# dq.pop(), dq.popleft(): 맨 오른쪽, 왼쪽 항목을 제거한다. 
# 여기서 주의할 점은, 어떤 argument도 받지 않는다는 것이다!
# 즉, 일반 리스트에서 하듯이 pop()으로 위치를 선택해서 제거할 수 없다.


# a.pop(-1) # TypeError
a.pop() # deque([0, 1, 2, 3, 4, 5])
a.popleft() # deque([1, 2, 3, 4, 5])

```



### 3. Iterable 추가

```python
b = [6, 7, 8]
c = [0, -1, -2]


# dq.extend(iterable): iterable 항목을 오른쪽으로 이어붙인다.
# dq.extendleft(iterable): iterable 항목을 왼쪽으로 이어붙인다.

# extend와 extendleft를 할 때는, iterable한 객체의 맨 왼쪽의 값부터 하나씩 이어붙인다.
# 즉 아래의 경우에는 deque a의 우측부터 6, 7, 8을 붙이고, 좌측부터 0, -1, -2를 붙인다.

a.extend(b) # deque([1, 2, 3, 4, 5, 6, 7, 8])

a.extendleft(c) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
```



### 4. 항목 제거

```python
# dq.remove(item): 맨 왼쪽에서부터 탐색하여, item을 리스트에서 제거한다.

a.appendleft(1) # deque([1, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

a.remove(1) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
```



### 5. 회전

```python
# dq.rotate(num): deque을 우측, 좌측으로 회전시킨다. 회전이란 맨 끝의 값을 반대쪽 끝에 붙인다는 뜻이다.
# num이 양수라면, 그 값만큼 오른쪽으로 회전시키고 음수라면 왼쪽으로 회전시킨다.

a.rotate(3) # deque([6, 7, 8, -2, -1, 0, 1, 2, 3, 4, 5])

a.rotate(-3) # deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
```









