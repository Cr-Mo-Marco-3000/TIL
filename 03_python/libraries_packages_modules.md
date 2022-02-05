# Library, Package, Modules



### JSON

- JSON.md, open()함수 참조



### pprint

- 임의의 파이썬 데이터 구조를 예쁘게 인쇄할 수 있는 기능을 제공

```python
import pprint
pprint.pprint()
```



## sys(module)

### stdin

- standard input - 표준 입력을 의미한다.
- readline()메소드를 사용하여 input()보다 빠른 속도로 입력을 읽을 수 있다.

```python

from sys import stdin

a = stdin.readline().rstrip()

# .readline() 개행문자 \n을 뒤에 붙이기 때문에, rstrip()등으로 이를 제거해줘야 한다.

```





## collections

### deque

- 덱을 만들 때 사용한다.
- [문서 참조](algorithm/stack_queue_deque.md)

