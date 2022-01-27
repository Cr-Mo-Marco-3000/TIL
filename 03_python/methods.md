# Methods

[TOC]

## method란?



- 수단이라는 뜻이지만, ~를 한다. 어떤 행위를 한다라고 임의로 해석할 수 있다.
- 즉 S + V  느낌으로, ~ 한테 무얼 해! 어떤 명령을 내릴 때 사용한다.
- 함수긴 함수인데, class 안에 정의된 함수이다. 함수의 subset 느낌
- 메소드는 매우 많지만, 대표적으로 활용되는 것들 위주로 기억하고 활용하면 된다.
- 묶어서 기억할 것들은 언급하겠다.



## string(immutable, sequence)



### 문자열 조회/탐색 메소드



#### s.find(x(글자) & s.index(x(글자)):



#### s.find(x(글자))

- 문자열에서, 처음 나오는 x의 위치를 **반환**한다.
- 문자열에 x가 없다면, -1을 반환한다.
- 딕셔너리 탐색에서 .get()의 역할과 비슷하다.
- 이름이 부드러우니 오류를 내지 않는다고 기억하자



#### s.index(x(글자))

- s.find(x)와 같이, 문자열에서 처음 나오는 x의 위치를 **반환**한다.
- 단, s.find(x)와는 다르게, x가 문자열에 없다면 오류를 발생시킨다.
- 인덱스, 뭔가 딱딱하다. 이름만 들어도 오류를 낼 것 같다.



```python
string = 'apple'

a = string.find('pl')
b = string.index('l')

print(a) # => 2
print(b) # => 3

c = string.find('c')  
d = string.index('d') # => ValueError

print(c) # => -1


```



### 문자열 검증 메소드



#### s.isalpha() & s.isupper() & s.islower() & s.istitle()

- s를 **검증**하는 method이므로 ()안에는 아무것도 들어가지 않는다.
- 각각 문자열이 알파벳(유니코드상 Letter, 즉 한국어도 포함)인지,
- 대문자인지,
- 소문자인지,
- Title(띄어쓰기 된 단어의 맨 앞글자가 대문자)인지 판별한다.
- 앞에 is가 붙는다면 ~인지 검증한다는 의미로 쓰인다고 할 수 있고, 변수 이름설정에도 유용하게 쓰인다.
- s.isdecimal(), s.isdigit(), s.isnumeric() 등은 그냥 numeric이 가장 큰 범주라고만 기억하자!



```python
'앙녕'.isalpha() # => True

'AB'.isupper() # => True

'ab'.islower() # => True

'Title Sequence'.istitle() # => True
```



### 문자열 변경 메소드(upper과 lower,swapcase도 해보자.)



- 문자열은 immutable하지만, 이 method들은 새 문자열을 반환하는 식으로 작동한다.



#### s.replace(old(바꾸려는 글자들), new(새로운 글자들), count(해당 개수만큼 시행))



- 바꿀 대상 글자를 새로운 글자로 바꿔서 **반환**한다.
- count는, 앞에서부터 해당 개수만큼의 old들을 바꾼다.



```python
a = 'You are an idiot! Do it idiot!'

b = a.replace('idiot', 'genius', 1)

print(b) # => You are an genius! Do it idiot!
```



#### s.strip(chars(문자들))

- 특정한 문자들을 지정하면,
- 양쪽을 제거하거나(s.strip(chars))
- 왼쪽을 제거하거나(s.lstrip(chars))
- 오른쪽을 제거한다.(s.rstrip(chars))
- 문자열을 지정하지 않으면 좌우의 공백과 개행문자를 **제거**한 값을 **반환**한다!

```python
a = 'asdffdsa'
b = '   asdffdsa  '

print(a.strip('as')) => 'dffd'
print(b.strip(' ad')) => 'sdffds'
print(b.strip()) => 'asdffdsa'
# 제거하는 방식이 조금 특이한데, ()안에 들어가지 않은 글자가 나올 때 까지 ''안의 각 글자를 모두 제거한다.
# 즉 두번째 print 예시에서, ' '와 'a'와 'd'를 제거하지만, 문자열에서 ' '와 'a'를 제거 후 s는 제거 대상에 없으니 그 안의 d는 제거하지 못한 것이다.

```



#### s.split(chars(단위)) : 중요

- 문자열을 ()안의 특정한 단위로 나눠 **리스트**로 **반환**한다.

- .split()으로 쓰면 띄어쓰기 별로 나누어서 반환한다( .split(" ") 과 동일).
- 쉼표 등으로 나눌 때는, 안에 ', '등을 넣어 사용한다.

```python
string = 'singing in the rain'
print(string.split())
# => ['singing', 'in', 'the', 'rain']
# 입력 시 띄어쓰기로 구분된 숫자를 받아 바로 사용할 때는 다음과 같이 사용된다.
a, b, c = map(int, input().split())
print(a, b, c) # 각각 입력한 숫자대로 a, b, c 에 할당.
```



#### separator.join(iterable(객체)) : 중요

- iterable의 인자들 사이에 separator를 넣어서 **문자열**을 **반환**한다.
- 만약 iterable의 인자들 중 str이 아닌 값이 있으면 Type Error를 반환한다.
- 즉, ['1', '2', '3']은 iterable에 들어갈 수 있지만, ['1', '2', **3**]은 에러가 발생한다.
- 2개 인자 동시에 받는 건 안된다...

```python
a = ('apple', 'is', 'delicious')
b = ['1', '2', '3']
c = ['1', '2', 3]

print(" ".join(a)) # => 'apple is delicous' 반환
print("".join(b)) # '123' 반환
print("".join(c)) # TypeError
```



#### .capitalize()

- 맨 앞글자를 대문자로 만들어 문자열을 **반환**한다.

#### .title()

- 어포스트로피(')나 공백 이후를 대문자로 만들어 **반환**한다.

#### .upper()

- 모든 글자를 대문자로 만들어 **반환**한다.

#### .lower()

- 모든 글자를 소문자로 만들어 **반환**한다.

#### .swapcase() 등이 있다.

- 대문자는 소문자로, 소문자는 대문자로 바꿔 **반환**한다.



## number



#### number.real

- 복소수 number에서 실수부를 뽑아낸다
- 뽑아낸 숫자는 float type을 가진다.

```python
a = 2 + 3j

b = a.real

print(b)

# => 2.0
```



#### number.imag

- 복소수 number에서 허수 앞의 숫자를 뽑아낸다.
- 뽑아낸 숫자는 float type을 가진다.

```python
a = 2 + 3j

b = a.imag

print(b)

# => 3.0 
```





## List(mutable, sequence)



- list 메소드의 핵심은, 그 중 값을 변경시키는 것들이 존재한다는 것이다.
- 이는 list가 mutable하기 때문이다.



### 값 추가 및 삭제



#### l.append(x) & l.extend(iterable) & l.insert(i(index),x) 



#### l.append(x)

- list의 마지막에에 x를 인자로 **추가**한다.
- 기존의 문자열에 인자를 넣는 것이지, 새 문자열을 만드는 것이 아니다!

```python
a = [1, 2, 3]

a.append(4)

print(a)

# => [1, 2, 3, 4]
```



#### l.extend(iterable)

- 기본의 list에 iterable의 항목을 **추가**한다.
- 따라서, 문자열을 그대로 넣게 되는 실수를 범할수도 있으므로 주의!
- extend도 마찬가지로, 기존의 문자열에 인자를 추가하는 것이지 새 문자열을 만드는 것이 아니다.
- 연산자 +와 비슷한 역할을 한다. => '+'는 리스트와 리스트만 결합할 수 있다.

```python
cafe = ['starbucks', 'paul bassett', 'blue bottle']

cafe_2 = ['coffee bean', 'ediya']

cafe_3 = 'hollys'

cafe.extend(cafe_2)

print(cafe) # =>['starbucks', 'paul bassett', 'blue bottle', 'coffee bean', 'ediya']

cafe.extend(cafe_3) 

print(cafe) # => ['starbucks', 'paul bassett', 'blue bottle', 'coffee bean', 'ediya', 'h', 'o', 'l', 'l', 'y', 's'] 
```



#### l.insert(i,x)

- list의 정해진 위치 index에 x값을 **추가**한다.

- i가 리스트의 길이보다 긴 경우, 리스트의 맨 뒤에 값을 추가한다. 왜냐면 가장 뒤의 위치에 넣어야 하거든.

- -1는 안된다. len()쓰자! 보통 len()이면 항목의 인덱스를 벗어나지만, .insert()에서는 괜찮다.

```python
cafe = ['starbucks', 'paul bassett', 'blue bottle']

cafe.insert(1, 'hollys')

print(cafe) # => ['starbucks', 'hollys', 'paul bassett', 'blue bottle']

cafe.insert(6, 'cafebene')

print(cafe) # => ['starbucks', 'hollys', 'paul bassett', 'blue bottle', 'cafebene']
```





#### list.remove(x)

- list에서 x를 제거한다.

```python
a = [1, 2, 3]
a.remove(2)
print(a)
# => [1, 3]
```



## dict: items, .get 많이 사용.

#### dict.keys(), dict.values(), dict.items()

- 각각 dict에 있는 모든 key 값들, value값들 key:items 값들을 반환한다.
- 반환되는 타입은 고유값이므로, 사용하려면 형변환이 필요하다.
- () 안에는 아무 것도 들어가면 안된다!

```python
a = {1='a', 2='b' 3:'c'}
b = list(a.keys())
c = list(a.values())
d = list(a.items())
print(b, c, d)
```
