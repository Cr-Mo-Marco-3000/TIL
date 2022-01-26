# 0126_workshop

 ## 1.

```python
# 1) 파이썬의 패키지 관리 시스템인 pip에게, faker라는 패키지를 설치하라는 명령어이다.
# 2) python의 터미널이나, bash등 쉘의 터미널에서 실행할 수 있다.
```



## 2.

```python
# 1) Faker라는 패키지로부터 Faker라는 모듈을 불러오기 위한 코드이다.
# 2) Faker는 클래스, fake는 인스턴스이다.
# 3) name()은 fake의 메서드이다.
```



## 3.

```python
class Faker():
    
    def __init__(self, lang):
        
# a)는 __init__ 여야 하고
# b)는 self 여야만 하지만
# c)는 내가 정할 수 있다. 언어가 들어가 매개변수 명을 lang이라 했다.
```



## 4.

```python
from faker import Faker

fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())

# 1 : 이도윤

# 2 : 이지후

# Faker에 직접 명령을 내리는 것으로 봐서, 클래스 메서드로 보인다.
```



## 5.

```python
from faker import Faker
fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())

# 아직 잘 모르겠다.
```

