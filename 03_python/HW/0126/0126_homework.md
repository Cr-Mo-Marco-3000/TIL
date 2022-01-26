# 0126_homework

 ## 1.

```python
# int, string, bool, list, tuple등이 있다.
# 기존에 우리가 Type이라고 알았던 많은 것들이 Class이다.
```



## 2.

```python
# __init__
'''
__init__은 생성자 메서드로서
특정 인스턴스를 생성하자마자 실행되는 메서드를 만든다.
보통 인스턴스의 속성을 정의한다.
'''
# __del__
'''
__del__은 소멸자 메서드로서
del 등을 사용하여 인스턴스를 소멸시킬 때, 인스터스가 소멸하기 직전에 실행되는 메서드이다.
'''

# __str__
'''
특정 객체를 출력할 때, 출력할 내용을 지정할 수 있다.
'''


# __repr__
'''
__str__과 같이, 특정 객체를 출력할 때 출력되는 내용을 지정하지만, __str__처럼 읽기 쉬운 내용보다는 보다 자세한 내용을 출력한다...고 하는데 모르겠다.
'''
```



## 3.

```python
"""
.append(x): 리스트의 마지막에, x를 항목으로 추가한다.
.remove(x): 리스트에서, x와 일치하는 첫 번째 항목을 삭제한다.
.extend(x): 리스트의 마지막에, iterable한 객체 x를 이어붙인다.
"""
```



## 4.

```python
def fibo_recursion(n):
    if n < 2:
        return m
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    
from fibo import fibo_recursion as recursion

recursion(4)
```

