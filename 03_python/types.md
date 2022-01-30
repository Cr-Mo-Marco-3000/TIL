# Types



![data structure](types.assets/data structure.png)



데이터의 분류:



- Boolean(immutable)

- Numeric(immutable)
  - Int
  - Float
  - Complex

- Sequence
  - String(immutable, sequence, iterable)
  - List(mutable, sequence, iterable)
  - Tuple(immutable, sequence, iterable)
  - Range(immutable, sequence, iterable)

- Set(mutable, iterable)
- Dictionary(mutable, iterable)



## Dictionary

- 키: 해시 가능한 값이어야 한다.
- 여기서 해시 가능하다는 것은, 변하지 않는 해시값을 갖고, 다른 객체와 비교 가능하다는 것으로, 튜플이나 frozenset 같은 불변 컨테이너 등이 있다.
- 특성
  - Not iterable
  - Not Sequence
  - Mutable
- 선언방법

```python
a = dict(one=1, two=2, three=3) # dict함수 안에 key=value형태로 쓰기, 이 때 주의해야 할 점은, key 자리에 변수를 쓸 수 없다는 점이다. 문자열로 들어간다!

b = {'one': 1, 'two': 2, 'three': 3} # {}안에 key:value 형태로 쓰기

c = {('one', 1), ('two', 2), ('three', 3)} # 튜플 형태로 묶어 넣기

d = {zip(['one','two','three'],[1, 2, 3])} # zip() 활용


```



## Set

- 특성
  - Mutable
  - Unordered
  - Iterable
- 해시 가능한 객체들을 elements로 삼는 자료형이다.
- 여기서 해시 가능하다는 것은, 변하지 않는 해시값을 갖고, 다른 객체와 비교 가능하다는 것으로, 튜플이나 frozenset 같은 불변 컨테이너 등이 있다.
- 즉 set은 리스트나 set 등 mutable한 자료들은 element로 가지지 못한다!!!
