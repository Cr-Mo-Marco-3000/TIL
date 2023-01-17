# Packing & Unpacking

- 패킹과 언패킹을 정리한다.



## 패킹

- 여러 개의 인자를 묶어서 하나의 객체로 합친다.

  

- 변수 선언 시

  - 리스트로 묶인다.
  - 예시는 다음과 같다.

```python
a, *b = 1, 2, 3, 4, 5

print(a)
print(type(a))
print(b)
print(type(b))

'''
1
<class 'int'>
[2, 3, 4, 5]
<class 'list'>
'''
```



- 함수 내부에서 패킹이 들어갈 경우
  - 매개변수에 * 또는 **를 붙인다.
  - 튜플 형태, 또는 딕셔너리 형태로 묵인다.
  - 예시는 다음과 같다.

```python
def packing(a, *b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    
    
a = packing(1, 2, 3, 4, 5)
# 2, 3, 4, 5를 튜플로 묶었다.
'''
1
(2, 3, 4, 5)
<class 'int'>
<class 'tuple'>
'''


def aprint(a, **b):
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    
aprint(a=1, b=2, c=3)
#딕셔너리 객체를 넣을 때는, 위와 같은 형태로만 넣어야 한다. : 쓰면 안 된다. {}로 묶는 게 아니므로., dict()함수 쓰듯이 해야 한다.

# 함수에 인자를 받을 때는 두 가지 방법이 있는데, def func(a, b, c): 와 같이 단독으로 넣어 주기 혹은 def func(a='b', b='c'): 등과 같이 넣어 주기가 있다. 후자일 경우에는 함수의 매개변수에 **kwargs를 사용해서 패킹해서 받아 주어야 한다.


'''
1
<class 'int'>
{'b': 2, 'c': 3}
<class 'dict'>
'''
```



## 언패킹

- 한 개의 인자를 여러개로 풀어준다.
  - 함수에서 언패킹을 할 때는, 인자에 *를 붙여 사용한다.
  - 예시는 다음과 같다.

```python
a = (1, 2, 3, 4)

print(*a)
# 1 2 3 4 5

def aprint(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

aprint(*a)    	
# 1
# 2
# 3
# 4
 
```



