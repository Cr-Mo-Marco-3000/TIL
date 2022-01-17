# 0117_homework

## 1.

```python
# 파이썬에서 이미 사용중인 예약어 목록
import keyword
print(keyword.kwlist)

# 아래와 같은 단어는 변수 이름으로 사용할 수 없다.
'False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
'while', 'with', 'yield'
```



## 2.

```python
# 3가지 방법이 있다.

num1 = 0.1 * 3
num2 = 0.3

# 1. 두 값을 뺀 수의 절대값이 매우 작은 수인 경우, 두 수를 같은 것으로 판단한다.

print(bool(abs(num1 - num2) < 1e-10))

# 2. 두 값을 뺀 수의 절대값이 매우 작은 수인 경우, 두 수를 같은 것으로 판단한다.

import sys

print(abs(num1 - num2) <= sys.float_info.epsilon)

print(sys.float_info.epsilon)

# 3. math 모듈을 활용한다.

import math
print(math.isclose(num1, num2))
```



## 3. 

```python
# 1. 줄바꿈
\n

# 2. 탭
\t

# 3. 백슬래시
\\
```



## 4. 

```python
name = "철수"

# %-formatting
print("안녕, %s야" % (name))

# str.format()
print("안녕, {0}야".format(name))

# f-string
print(f"안녕, {name}야")

```



## 5. 

```python
int('3.5')
# 5번이 오류가 난다.
# 정수형로 만들 수 없기 때문이다
```



## 6. 

```python
n = 5
m = 9

a = "*" * n
b = "{0}\n".format(a) * m

print(b)

```



## 7.

```python
print(
    "\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'"
)
```



## 8. 

```python


print((((((b ** 2) - (4 * a * c))) ** 0.5) - b) / (2 * a))
print((-1 * ((((b ** 2) - (4 * a * c))) ** 0.5) - b) / (2 * a))

```

