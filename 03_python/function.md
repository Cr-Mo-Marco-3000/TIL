# 함수의 기초

[toc]

## 1. 함수란?



**프로그램에서 어떤 특정 기능을 수행할 목적으로 만들어진 재사용 구조의 코드 부분**



함수의 장점

1) 하나의 큰 프로그램을 여러 부분으로 나눌 수 있기 때문에 구조적 프로그래밍이 가능해짐

2) 동일 함수를 여러 곳에서 필요할 때마다 호출할 수 있고
3) 수정이 용이

**인자(argument) -> 매개변수(parameter) -> 함수(function) -> 반환값(return)**



순수 함수(pure function): 결과값 반환 외에 외부에 영향을 주지 않는 함수

함수형 프로그래밍 지원 언어에서는 순수 함수를 인자, 반환값으로 사용



## 2. 함수의 호출 및 선언



함수의 호출

print() => 괄호 안에 인자 전달

```python
a, b = 2, 3

c = a + b

print("내장함수 str.format() 과 print()를 이용한 c의 결과 출력: {0}".format(c))

# str.format() 함수 호출문이 print() 함수의 인자로 전달
# print함수는 str.format()함수가 반환한 문자열을 인자로 전달받아 표준 출력에 해당 문자열 출력
```

함수의 선언

```python
def 함수명 (매개변수):
    명령문1
    명령문2
    return문
```

```python
# calc_sum 함수: 두 개의 값을 전달 받아 합을 구하는 사용자 정의 함수

def calc_sum(x, y): # 매개변수에 인자값 전달
    return x + y # calc_sum()함수를 호출한 위치에 반환 값이 전달됨

a,b = 2, 3

c = calc_sum(a, b)
d = calc_sum(a, c)

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 d의 결과: {0}".format(c))

"""


a,b = 2, 3

c = calc_sum(a, b)
d = calc_sum(a, c)

print("사용자 정의 함수 calc_sum() 호출을 이용한 c의 결과: {0}".format(c))
print("사용자 정의 함수 calc_sum() 호출을 이용한 d의 결과: {0}".format(c))

def calc_sum(x, y):
    return x + y 
=> 실행시 calc_sum is not defined 에러 발생  
"""
```

**인터프리터 언어의 경우 함수 선언 위치가 매우 중요함!!!**

명령을 한줄씩 해석해 실행하는 방식으로 동작하기 때문에,
실행 공간에 함수 정보가 없을 경우 오류가 발생할 수 있음



---



## 3. 함수의 유형



매개변수의 유무, 반환값의 유무에 따라 형태적 분류 가능

매개변수 => 함수에 입력 값을 전달해야 하는가를 결정하는 요인

반환값 => 함수가 수행 결과를 호출한 곳으로 돌려줄 필요가 있는가를 결정하는 요인



- 함수의 유형

1) 매개변수(parameter)와 반환 값이 있는 함수
2) 매개변수는 없고 반환 값이 있는 함수
3) 매개변수는 있고 반환 값이 없는 함수
4) 매개변수와 반환 값이 없는 함수



```python
# 매개변수와 반환 값이 있는 함수

def func_parameters_return(x, y, z):
    print("매개변수로 전달된 값은 {0}, {1}, {2} 입니다.".format(x, y ,z))
    print("매개변수와 반환값이 있는 함수입니다.")
    return "Hello, Python!" # 함수를 호출한 위치에 반환 값으로 전달

ret_val = func_parameters_return(1,2,3) # 1,2,3이 각각 x, y, z의 인자로 전달
print("func_parameters_return() 함수가 반환한 값: {0}".format(ret_val))

"""
매개변수로 전달된 값은 1, 2, 3 입니다.
매개변수와 반환값이 있는 함수입니다.
func_parameters_return() 함수가 반환한 값: Hello, Python!
"""

```



```python
# 매개변수는 없고, 반환 값이 있는 함수

def func_noparameters_return():
    print("매개변수가 없는 함수입니다.")
    return "Hello, Python!"
ret_val = func_noparameters_return()
print("func_noparameters_return() 함수가 반환한 값: {0}".format(ret_val))

"""
매개변수가 없는 함수입니다.
func_noparameters_return() 함수가 반환한 값: Hello, Python!
"""

```

```python
# 매개변수는 있고 반환 값이 없는 함수


def func_parameters_noreturn(x, y, z):
    print("매개변수로 전달된 값은 {0}, {1}, {2} 입니다.".format(x, y, z))
    print("반환값이 없는 함수입니다.")


func_parameters_noreturn(1, 2, 3)

"""
매개변수로 전달된 값은 1, 2, 3 입니다.
반환값이 없는 함수입니다.
"""
```

```python
# 매개변수와 반환 값이 없는 함수

def func_noparameters_noreturn():
    print("매개변수와 반환값이 없는 함수입니다.")
    
func_noparameters_noreturn()

"""
매개변수와 반환값이 없는 함수입니다.
"""
```



## 4. 함수와 매개변수



### 매개변수

함수 호출 시 입력 값을 전달 받기 위한 변수

전달받은 인자의 값에 의해 타입이 결정됨

선언된 매개변수의 개수만큼 인자 전달 가능

```python
def calc_sum(x, y, z):
    result = x + y + z
    return result
ret_val = calc_sum(1, 2, 3)
print("calc_sum() 함수가 반환한 값: {0}".format(ret_val))

# 매개변수와 인자의 개수 일치
# calc_sum() 함수가 반환한 값: 6 => 결과값
# 인자 수가 적게 전달될 시 TypeError: calc_sum() missing 1 required positional argument:'z' 발생, 인자 수가 적게 전달될 시, 3개 인자 전달해야 하는데 4개 전달했다는 오류 발생

```

### 언팩 연산자

매개변수의 개수를 가변적으로 사용할 수 있도록 언팩 연산자(*) 제공

매개변수에 적용 시 **인자를 튜플 형식**으로 처리함



```python
# 언팩 연산자를 사용하는 튜플 형식의 가변 매개변수

def calc_sum(*params): # 매개변수에 인자 값들이 튜플 형식으로 전달
    total = 0
    for val in params:
        total += val
    return total # 변수 total의 값이 calc_sum() 함수를 호출한 위치에 반환 값으로 전달

ret_val = calc_sum(1, 2) 
# 1, 2가 인자로 전달되어 for 문이 두 번 반복, calc_sum() 함수는 수행 결과로 3 반환
print("calc_sum(1, 2) 함수가 반환한 값: {0}".format(ret_val))


ret_val = calc_sum(1, 2, 3)
print("calc_sum(1, 2, 3) 함수가 반환한 값: {0}".format(ret_val))

# 6반환
```



**주의할 점**

가변형 매개변수는 하나만 지정 가능

가변형 매개변수를 가장 마지막 매개변수로 지정해야 부작용 없이 사용할 수 있음



```python
# 명시적 매개변수와 가변형 매개변수의 혼합 사용
def calc_sum(precision, *params): # 첫 번째 매개변수 precision에 인자 값이 가장 먼저 전달
    # 나머지 인자 값들이 params 매개변수에 튜플 형식으로 전달.
    if precision == 0:
        total = 0
    elif 0 < precision < 1:
        total = 0.0
        
    for val in params:
        total += val
    return total

ret_val = calc_sum(0, 1, 2)
print("calc_sum(0, 1, 2) 함수가 반환한 값: {0}".format(ret_val))

# 매개변수 precision의 값이 0이므로, 정수 0으로 초기화
# 매개변수 params가 1과 2를 가진 튜플이므로, 두 번 반복

# calc_sum(0, 1, 2) 함수가 반환한 값: 3
# calc_sum(0, 1, 2) 함수가 반환한 값: 3.0
```



기본적으로 함수는 하나의 값을 반환할 수 있지만, 
파이썬은 언팩연산자 기능을 사용하면 하나 이상의 값을 반환 가능



```python
def calc_sum(precision1, precision2, *params):
    if precision1 == 0:
        total1 = 0
    elif 0 < precision1 < 1:
        total1 = 0.0
    # 매개변수 precision 1에 전달된 값에 따라 반환값으로 사용할 total1의 값을 정수 0 혹은 부동소수점 숫자 0.0으로 초기화

    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0

    for val in params:  # 튜플 형식의 매개변수 params의 전달된 인자들을 반복 접근
        total1 += val  # 변수 total1과 total2에 개별 인자 값 누적
        total2 += val
    return total1, total2  # 튜플을 반환해서 하나 이상의 값을 반환할 수 있음


ret_val = calc_sum(0, 0.1, 1, 2)

print("calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: {0}, {1}".format(*ret_val))
# 튜플 ret_val을 여러 인자로 분리하기 위해 언팩 연산자 사용
print("calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: {0}, {1}".format(ret_val[0], ret_val[1]))
# 위와 동일한 결과를 출력 => 튜플의 개별 원소를 인덱스로 접근해 처리

"""
calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: 3, 3.0
calc_sum(0, 0.1, 1, 2) 함수가 반환한 값: 3, 3.0
"""

```



### 키워드 언팩 연산자(**)

매개변수의 개수를 가변적으로 사용할 수 있도록 함

키워드 인자들을 전달해 **매개변수를 딕셔너리 형식**으로 처리함

키1=값1 키2=값2

```python
def use_keyword_arg_unpacking(**params):
    for k in params.keys():  # 매개변수 params에서 params.keys() 함수 호출을 통해 키 리스트 구함
        print("{0} : {1}".format(k, params[k]))  # 키는 전달된 매개변수 이름, 값은 전달된 인자 값임


print("use_keyword_arg_unpacking()의 호출")
use_keyword_arg_unpacking(a=1, b=2, c=3)
# 키=값 형식으로 전달하면, params 매개변수에 딕셔너리 형식으로 전달

"""
use_keyword_arg_unpacking()의 호출
a : 1
b : 2
c : 3
"""
```



### 기본 값을 갖는 매개변수

매개변수에 전달할 인자 값이 생략되었다면? => 사용할 기본 값 지정 가능

기본 값을 가지는 매개변수는 일반 매개변수 앞에 위치할 수 없다!

```python
def calc(x, y, operator="+"):  # '+'를 기본값으로 지정 => operator에 전달할 인자를 생략하면 +가 기본으로 전달
    if operator == "+":
        return x + y
    else:
        return x - y


ret_val = calc(10, 5)  # 매개변수의 기본값 "+" 사용

print(ret_val)
```



### scope

변수의 유효범위

어디서나 접근 가능한 전역 변수 => 전역 스코프

함수 내에서만 접근 가능한 지역 변수 => 함수 스코프

```python
def test_scope(a):
    result = a + 1  # 지역변수 result: 변수 a값에 1을 더한 값
    print("\n\ttest_scope() 안에서의 a의 값: {0}".format(a))
    print("\ttest_scope() 안에서의 result의 값: {0}\n".format(result))
    return result  # 지역변수 a와 result는 유효하지 않은 정보가 됨


x = 5
print("test_scope() 호출 전 x의 값: {0}".format(x))
ret_val = test_scope(x)  # 전역변수 x의 값 5: 매개변수 a의 인자로 전달, 지역변수 result에 6 저장
print("test_scope() 함수가 반환한 값: {0}".format(ret_val))
print("test_scope() 호출 후 x의 값: {0}".format(x))


"""
test_scope() 호출 전 x의 값: 5

        test_scope() 안에서의 a의 값: 5
        test_scope() 안에서의 result의 값: 6

test_scope() 함수가 반환한 값: 6
test_scope() 호출 후 x의 값: 5
"""
```

### 변수에 접근하는 절차

```python
# 1순위
a = 1
def scope():
    a = 2
    print(a) # 함수 스코프 내에서 가장 먼저 변수를 찾음
    
scope()
print(a)

# 2순위
a = 1
def scope():
    print(a) # 함수 스코프 내에 변수가 없을 경우 전역 스코프에서 변수를 찾음

scope()
print(a)

# 이와 같이 지역변수와 전역변수 이름이 같을 경우! 전역변수가 가려져 접근 못할 수 있음
# => 접근하고자 하는 전역변수 앞에 global을 기술함
```



함수 내에서 global 변수에 접근하기

```python
def change_global_var():
    global x  # 함수 내에서 x는 전역변수를 가리킴
    x += 1 # 변수 x의 값 5가 인자로 전달되고, 1을 더한 결과값 반환


x = 5
change_global_var() # 변수 x의 값 5가 전역변수 x의 값으로 변경
print("전역변수 x의 값: {0}".format(x))

# 결과 6
```



## 5. 고급 함수 사용법

### 중첩 함수

**함수 내에 중첩함수를 선언해 사용 가능**

1) 중첩함수를 포함하는 함수 내에서만 호출이 가능함

2) 중첩함수를 포함하는 함수의 스코프에도 접근이 가능
   - 함수 내에서 직접 선언해 호출할 수도 있고, 함수의 매개변수로 함수 인자를 전달받아 함수 내에서 호출해서 사용 가능



```python
def calc(operator_fn, x, y):
    return operator_fn(x, y)  # 매개변수 operator_fn에 전달된 함수를 실행해 반환된 값을 return문을 통해 반환


def plus(op1, op2):
    return op1 + op2


def minus(op1, op2):
    return op1 - op2


ret_val = calc(plus, 10, 5) # plus를 calc의 첫 번째 변수(oeprator_fn)에, 10을 두 번째 변수에, 5를 세 번째 변수에 전달
print("calc(plus, 10, 5)의 결과 값: {0}".format(ret_val))

ret_val = calc(minus, 10, 5)
print("calc(minus, 10, 5)의 결과 값: {0}".format(ret_val))

```

프로그래밍 언어는 프로그램의 유연성을 높이기 위해 함수를 매개변수로 전달하는 방식 선호!!!

but 매번 함수를 선언해 사용한다는 것이 불편할 수 있음!



### 람다식

Lambda 매개변수 : 반환값

1. 변수에 저장해 재사용이 가능한 함수처럼 사용함
2. 기존의 함수처럼 매개변수의 인자로 전달함
3. 함수의 매개변수에 직접 인자로 전달함



```python
def calc(operator_fn, x, y):
    return operator_fn(x,y)

ret_val = calc(lambda a, b: a + b, 10, 5)
print("calc(lambda a, b: a + b, 10, 5)의 결과 값: {0}".format(ret_val))

ret_val = calc(lambda a, b: a - b, 10, 5)
printprint("calc(lambda a, b: a - b, 10, 5)의 결과 값: {0}".format(ret_val))
```



### 클로저

1. 중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근 가능
2. 중첩함수 자체를 반환값으로 사용한다면?
   1) 정보 은닉 구현 가능
   2) 전역변수의 남용 방지
   3) 매서드가 하나밖에 없는 객체를 만드는 것보다 우아한 구현 가능

**이러한 기법을 클로저라고 부름**

```python
def outer_func():
    id = 0  # 지역변수: 함수 내의 코드 또는 중첩함수에서만 접근 가능

    def inner_func():
        nonlocal id  # 변수 id가 중첩함수인 inner_func 함수의 지역변수가 아님, 변수 id 접근 시 outer_func 함수 스코프에서 찾게 만듦
        id += 1
        return id

    return inner_func  # inner_func 함수 호출이 아닌 함수에 대한 참조를 반환함에 유의함


make_id = outer_func()
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))
print("make_id() 호출의 결과: {0}".format(make_id()))

# 중첩함수 inner_func() 호출 =>
# outer_func() 함수의 지역변수 id의 값 1씩 증가 =>
# 증가된 id값 반환 =>
# str.format() 함수의 인자로 전달, 변환 문자열 생성 =>
# print() 함수를 통해 표준출력으로 출력

"""
make_id() 호출의 결과: 1
make_id() 호출의 결과: 2
make_id() 호출의 결과: 3
"""
```

**함수를 활용하여 원의 둘레와 면적 구하기**

반지름 입력, 원의 면적 계산, 원의 둘레 계산

결과

반지름을 입력하세요

원의 면적: 78.50, 원의 둘레 : 31.40

```python
# -*- coding: utf-8 -*-

# practice.py


PI = 3.14


def input_radius():
    radius_str = input("반지름을 입력하세요: ")
    return float(radius_str)


def calc_circle_area(r):
    return PI * r * r


def calc_circumference(r):
    return 2 * PI * r


radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)

print("원의 면적: {0:0.2f}, 원의 둘레: {1:0.2f}".format(circle_area, circumference))

```

