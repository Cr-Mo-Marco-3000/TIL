# Functions in Python



## 1. 설명

### I. 인자

> https://docs.python.org/ko/3/glossary.html#term-argument

함수에 인자를 받을 때는 두 가지 방법이 있다.

순서는 위치 인자 => 키워드 인자 순서대로 들어간다.

#### 1) 키워드 인자

- 함수 호출 때 식별자가 앞에 붙은 인자
  - 여기서 식별자는 `name=` 형태로, name 부분에는 변수의 형태와 같이 ''를 붙이지 않은 문자열이 들어간다.
  - `complex(real='레알', imag=5)`
- 또는 **를 앞에 붙인 - 언패킹한 - 딕셔너리로 전달되는 인자.
  - `complex(**{'real': '레알', 'imag': 5})`

#### 2) 위치 인자

- 인자 목록의 처음에 나오거나
  - `complex(3, 5)`
- 이터러블 앞에 *를 붙여 - 언패킹해 - 전달할 수 있다.
  - `complex(*(3, 5))`



## 2. Built-in-Functions

### map(function, iterable)

- iterable 객체의 각각 항목에 function을 적용해서 반환

```python

```

### sorted(iterable, reverse=False)

- 파일을 오름차순으로 정렬
- reverse=True를 넣으면 내림차순으로 정리

```python
a = [2, 3, 7, 9, 6]
b = sorted(a)
b = [2, 3, 6, 7, 9]
```

### reversed(sequence)

- 파일을 반전된 상태의 iterator로 반환
- 활용하려면 list등의 형태로 재변환해주어야 함

```python
a = (1, 2, 3)
b = reversed(a)
c = list(b)
print(c)	
```



### open(file, mode, encoding)

```python
# 파일들을 불러와서 읽을 때 쓴다.
# mode = 'r' open for reading이 default

# 기본 형태
# a = open(file(파일명), mode='r'(파일을 읽을건지, 쓸건지, 붙일 것인지) encoding=None(일반적으로 utf-8 활용))

# 파일 객체 활용: 요즘은 이렇게 많이 활용 안함
a = open('경로/파일명.json', mode='r', coding=utf-8)


# with 키워드 활용: 요즘 이렇게 많이 활용
# => with 키워드를 활용하지 않으면, f.lclose()를 반드시 호출하여 종료시켜야 오류가 발생하지 않음, 따라서 일반적으로 with 키워드를 활용하여 작성

with open('workfile') as f:
	read_data = f.read()


# f가 닫혔는지 확인하면, True라고 나온다
f.closed


# json과 함께 활용
get_json = open("C:/Users/bizyo/ssafy7/TIL/03_python", mode='r', encoding=utf-8)
use_json = json.load(open)
# => 이제 use_json를 딕셔너리나 리스트 등으로 이용 가능!
```



### bool

- 값이 참이면 True를, 거짓이면 False를 반환
- 빈 리스트, 빈 set 등 빈 객체의 경우도 False를 반환

``` python
a = bool([])
b = bool(())
c = bool([0])
print(a, b, c)
# => False False True
```



### chr

- 숫자를 유니코드에 해당하는 문자로 변환

``` python
a = chr(8364)
print(a)
# => '€'
```



### ord

- 글자를 유니코드에 해당하는 숫자로 변환

```python
a = ord('€')
print(a)
# => 8364
```

