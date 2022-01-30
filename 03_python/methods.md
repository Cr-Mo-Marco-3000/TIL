# Methods

[TOC]

## :books: Method란?



- 수단이라는 뜻이지만, ~를 한다. 어떤 행위를 한다라고 임의로 해석할 수 있다.
- 즉 S + V  느낌으로, ~ 한테 무얼 해! 어떤 명령을 내릴 때 사용한다.
- class 안에 정의된 함수이다.
- 메서드는 매우 많지만, 대표적으로 활용되는 것들 위주로 기억하고 활용하면 된다.
- dir 함수로 컨테이너가 가지고 있는 메서드를 확인할 수 있다.

```python
dir('string')

dir([1,2,3])
```







## 1. string(immutable, sequence(ordered), iterable)



### 1) 문자열 조회/탐색 메서드



#### s.find(x(글자))

- 문자열에서, 처음 나오는 x의 위치를 **반환**한다.
- 문자열에 x가 없다면, -1을 반환한다.
- 딕셔너리 탐색에서 .get()의 역할과 비슷하다.
- 이름이 부드러우니 오류를 내지 않는다고 기억하자



#### s.index(x[, start[, end]])

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



### 2) 문자열 검증 메서드



#### s.isalpha() & s.isspace() & s.isupper() & s.islower() & s.istitle()

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



#### s.startswith(x) & s.endswith(x)

- 문자열이 x로 시작하면 True를 반환, 아니면 False를 반환
- 문자열이 x로 끝나면 True를 반환, 아니면 False를 반환



### 3) 문자열 변경 메서드



- 문자열은 immutable하기 때문에, 이 method들은 새 문자열을 반환하는 식으로 작동한다.



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

- iterable의 항목들(모두 string이어야 한다!!) 사이에 separator를 넣어서 **문자열**을 **반환**한다.
- 다른 메서드들과 달리, 구분자가 앞에 들어간다.
- 만약 iterable의 항목들 중 str이 아닌 값이 있으면 Type Error를 반환한다.
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



#### s.capitalize()

- 맨 앞글자를 대문자로 만들어 문자열을 **반환**한다.



#### s.title()

- 어포스트로피(')나 공백 이후를 대문자로 만들어 **반환**한다.



#### s.upper()

- 모든 글자를 대문자로 만들어 **반환**한다.



#### s.lower()

- 모든 글자를 소문자로 만들어 **반환**한다.



#### s.swapcase()

- 대문자는 소문자로, 소문자는 대문자로 바꿔 **반환**한다.



## 2. number(immutable)



- 정확히 real, imag는 메서드가 아니고, 인스턴스 변수라 할 수 있다.
- 나중에 정리하겠다.



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







## 3. List(mutable, sequence(ordered), iterable)



- list 메서드의 핵심은, 그 중 값을 변경시키는 것들이 존재한다는 것이다.
- 이는 list가 mutable하기 때문이다.
- List가 가진 특징은, mutable, ordered(순서가 있음), iterable(순회가능)



### 1) 값 추가 및 삭제



#### l.append(x)

- list의 마지막에에 x를 항목으로 **추가**한다.
- 기존의 리스트에 항목을 추가하는 것이지, 새 문자열을 만드는 것이 아니다!

```python
a = [1, 2, 3]

a.append(4)

print(a)

# => [1, 2, 3, 4]
```



#### l.extend(iterable)

- 기본의 list에 iterable의 항목을 **추가**한다.
- 따라서, 문자열의 글자별로 리스트의 항목에 추가하는 실수를 할 수 있으니 주의!
- extend도 마찬가지로, 기존의 리스트에 항목를 추가하는 것이지 새 리스트를 만드는 것이 아니다.
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

- list의 정해진 위치 index에 x를 **추가**한다.
- i가 리스트의 길이보다 긴 경우, 리스트의 맨 뒤에 값을 추가한다. 왜냐면 가장 뒤의 위치에 넣어야 하거든.
- 리스트의 마지막에 항목을 넣을 때, index에 -1을 넣어서는 안된다. insert는 원래 자리에 있던 항목을 뒤로 밀어내고 그 자리에 x를 추가하기 때문에, 리스트의 마지막이 아니라 마지막에서 두 번째, 즉 -2 자리에 항목이 추가되게 된다.
- 리스트의 마지막에 항목을 추가하려면 len()을 쓰자! 보통 len()이면 항목의 인덱스를 벗어나지만, .insert()에서는 괜찮다.
- 즉, l.insert(len(l)(혹은 l의 길이 이상),x)는 l.append(x)와 같다.

```python
cafe = ['starbucks', 'paul bassett', 'blue bottle']

cafe.insert(1, 'hollys')

print(cafe) # => ['starbucks', 'hollys', 'paul bassett', 'blue bottle']

cafe.insert(6, 'cafebene')

print(cafe) # => ['starbucks', 'hollys', 'paul bassett', 'blue bottle', 'cafebene']
```





#### l.remove(x)

- list에서 값이 x인 첫 번째 항목을 삭제한다.
- 만일 값이 x인 항목이 없으면 ValueError가 발생한다.

```python
a = [1, 2, 3]

a.remove(2)

print(a)

# => [1, 3]

a.remove(2)

# => ValueError
```





####  l.pop(i)

- list에서 위치 i에 있는 값을 삭제하며, 그 항목을 반환한다.
- i가 지정되지 않을 경우, 마지막 항목을 삭제하고 반환한다.

```python
numbers = [1, 2, 3, 4, 5, 6]

numbers.pop(-1)

# numbers = [1, 2, 3, 4, 5]

num = numbers.pop()

# numbers = [1, 2, 3, 4]
# num = 5
```



#### l.clear()

- 리스트의 모든 항목을 삭제한다.



### 2) 탐색 및 정렬



#### l.index(x[, start[, end]])

- x 값을 찾아 해당 index 값을 반환한다.
- x 값이 리스트에 없다면, ValueError가 발생한다.
- String.index()와 비슷하다고 보면 된다.

```python
a = [1, 2, 3, 4, 5]

a.index(3)

# 2

a.index(20)
```



#### l.count(x)

- list에서 x의 개수를 반환한다.
- 원하는 값을 모두 삭제하려면, 다음과 같이 할 수 있다.

```python
list_to_remove = [1, 2, 3, 2, 1, 3, 1, 2]

target_value = 1

num = list_to_remove.count(target_value)

for i in range(num):
    list_to_remove.remove(target_value)
```



#### l.sort()

- 리스트를 정렬한다.
- 기본적으로 오름차순으로 정렬하며, reverse = True 매개변수를 지정한다면, 내림차순으로 정렬한다.
- sorted() 함수와는 다르게, 원본 리스트에 정렬 결과를 대입한다.

```python
test_list_1 = [0, 3, 5, 6, 5, 4, 3, 1]

test_list_2 = [0, 3, 5, 6, 5, 4, 3, 1]

test_list_1.sort()

new_list = sorted(test_list_2)

print(test_list_1) # [0, 1, 3, 3, 4, 5, 5, 6]
print(test_list_2) # [0, 3, 5, 6, 5, 4, 3, 1]
print(new_list) # [0, 1, 3, 3, 4, 5, 5, 6]
```



#### l.reverse()

- 리스트의 element들의 순서를 반대로 뒤집는다.
- 정렬하는 것이 아니라, 단순히 뒤집는 것이다.
- reversed()와는 다르게, 원본 list를변형시킨다.

```python
classroom = ['Tom', 'David', 'Justin']

print(classroom) # ['Tom', 'David', 'Justin']

classroom.reverse()

print(classroom) # ['Justin', 'David', 'Tom']
```



## 4. Tuple(immutable, sequence)



- 값을 변경할 수 없기 때문에, list와는 달리 값에 영향을 미치지 않는 메서드만을 지원한다.
- 즉, .append()와 같은 메서드는 사용할 수 없다는 뜻이다.



### 1) 탐색

#### t.index(x[, start[, end]])

- 튜플에 있는 항목 중 값이 x와 같은 첫 번째 인덱스를 돌려준다.
- 다른 index들과 같이, 해당 값이 없으면 ValueError를 발생시킨다.

```python
test_tuple = (1, 3, 5, 7, 9, 8, 4, 3, 5, 1)

a = test_tuple.index(3)

print(a) # 1

b = test_tuple.index(3, 2, 9)

print(b) # 7
```



#### t.count(x)

- 튜플에서 x가 등장하는 횟수를 반환합니다.

```python
a = (1, 3, 5, 1, 3, 5)

a.count(3)

print(a) # 2
```



## 5. Set(mutable, unordered, iterable)



- 변경 가능하고, 순서가 없고, **순회가능**하다.
- Set과 같이, 순서가 없어도 순회가능함에 유의!



### 추가 및 삭제



#### .add(elem)

- elem을 set에 추가한다.

```python
a = {'사과', '바나나', '수박'}

a.add("포도")
a.add("포도")

print(a) # {'사과', '바나나', '수박', '포도'}

a.add(("두리안", "자두"))

print(a) # {'수박', '바나나', '포도', '사과', ('두리안', '자두')}

a.add({"복숭아", "딸기"}) # ValueError : set은 해시가능한 값이 아님! Type.md 참조!


```



#### .update(*iterable)

- 여러 값을 추가한다.
- 반드시 iterable한 데이터 구조를 전달해야 한다.
- .add()와 .update()의 관계는, .append()와 .extend()의 관계와 유사하다 할 수 있다.
- 단, .extend()와 .update()가 다른 점은, update는 여러 개의 iterable을 인자로 받을 수 있다는 점이다.

```python
a = {'사과', '바나나', '수박'}

print(a) # {'사과', '바나나', '수박'}

b = ("두리안", "자두")
c = ("복숭아", "딸기")

a.update(b, c)

print(a) # {'두리안', '바나나', '자두', '딸기', '사과', '복숭아', '수박'}

```



#### .remove(elem)

- elem을 set에서 삭제한다.
- set 내부에 elem이 존재하지 않으면 KeyError가 발생한다.
- 즉, 파이썬 내부에서 set은 일종의 dictionary로 취급됨을 알 수 있다.

```python
a = {'사과', '바나나', '수박'}

a.remove("사과")

print(a) # {'바나나', '수박'}
```



#### .discard(elem)

- elem을 set에서 삭제한다.
- .remove()와 다른 점은, elem이 set 내부에 존재하지 않아도 KeyError가 발생하지 않는다는 점이다.

```python
a = {'사과', '바나나', '수박'}

a.discard('딸기') # 아무 일도 일어나지 않는다.

print(a) # {'사과', '바나나', '수박'}
```



## 6. dict(mutable, unordered, iterable)



- 변경 가능하고, 순서가 없고, **순회가능**하다(단, for문을 통한 순회 등을 할 때 key값만이 대입된다.
- Set과 같이, 순서가 없어도 순회가능함에 유의!



### 조회



#### d.get(key[, default])

- key를 통해 value를 가져온다
- key가 존재하지 않을 경우, None을 반환한다. 즉, d[key]와는 달리 KeyError가 발생하지 않는다.
- default에는 key가 없을 경우 반환할 기본값을 설정할 수 있다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

# my_dict['strawberry'] # KeyError

print(my_dict.get('strawberry')) # None

print(my_dict.get('strawberry', 'pepper')) # pepper

```



#### d.setdefault(key[, default])

- key를 통해 value를 가져온다
- .get()과 다른 점은 key가 존재하지 않을 경우,
  default값을 입력한 키의 value로 집어넣고 그 값을 반환한다는 점이다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

print(my_dict.setdefault('strawberry')) # None

print(my_dict.setdefault('peach', '복숭아')) # 복숭아

print(my_dict) {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'strawberry': None, 'peach': '복숭아'}
```



### 추가 및 삭제



#### d.pop(key[, default])

- key가 딕셔너리에 있으면 제거하고 그 값을 반환한다. 그렇지 않으면 default값을 반환한다.
- default 값을 설정하지 않은 상태인데 해당 key가 딕셔너리에 없을 경우, KeyError가 발생한다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

print(my_dict.pop("apple", "음슴")) # 음슴

print(my_dict.pop("apple")) # ValueError

print(my_dict) # {'banana': '바나나'}
```



#### d.update([other])

- other가 제공하는 key, value쌍으로 딕셔너리를 **덮어쓴다.**
- other에는 다른 딕셔너리나 key/value 쌍으로 되어 있는 모든 iterable을 사용 가능하다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

my_dict.update(strawberry='딸기', peach='복숭아', apple='사과앙')

print(my_dict) 
# {'apple': '사과앙', 'banana': '바나나', 'melon': '멜론', 'strawberry': '딸기', 'peach': '복숭아'}

d = {'mango':'망고', 'watermelon':'수박'}

my_dict.update(d)

print(my_dict) 
# {'apple': '사과앙', 'banana': '바나나', 'melon': '멜론', 'strawberry': '딸기', 'peach': '복숭아', 'mango': '망고', 'watermelon': '수박'}
```



#### dict.keys(), dict.values(), dict.items()

- 각각 dict에 있는 모든 key 값들, value값들 key:items 값들을 dictionary view object로 반환한다.
- 반환되는 타입은 고유값이므로, 사용하려면 형변환이 필요하다.
- .items()로 반환한 객체의 item들은 key와 value를 묶은 tuple 형태이다.
- () 안에는 아무 것도 들어가면 안된다!

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

a = my_dict.keys()
b = my_dict.values()
c = my_dict.items()

print(str(a) + "\n" + str(b) + "\n" + str(c) + "\n")


'''

dict_keys(['apple', 'banana', 'melon'])
dict_values(['사과', '바나나', '멜론'])
dict_items([('apple', '사과'), ('banana', '바나나'), ('melon', '멜론')])

'''

# for 문으로 dictionary 순환하는 법!
# .items()에서 반환되는 개개 item들은 (key, value)의 튜플형태로 묶어 있으므로 (key, value) = (key, value)가 돼서 순환가능하다!
for key, value in dict.items():
    print(f"{key} : {value}")

```
