# 0127_homework

 ## 1.

```python
class Circle: #
    pi = 3.14
    
    def __init__(self, r, x, y): # 인자들을 실행할 때 받는다.
        self.r = r
        self.x = x
        self.y = y
        
    def area(self): # 넓이 구하는 메서드
        return self.pi * self.r * self.r
    
    def circumference(self): # 둘레 구하는 메서드
        return 2 * self.pi * self.r
    
    def center(self): # 중심을 구하는 메서드... 는 왜 준지 모르겠다.
        return (self.x self.y)
    
dongle = Cirlce(3, 2, 4)

print(dongle.circumference()) # 둘레 : 2 * pi * r : 18.84
print(dongle.area()) # 넓이 : pi * r^2 : 28.25999...
```



## 2.

```python
class Animal: # 부모 클래스를 만든다. 이 부분은 주어졌다.
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal): # 상속받은 클래스를 만들었다.
    def __init__(self, name):
        super().__init__(name)
  # def __init__(self, name):
  #		self.name = name          => 요렇게 작성해도 되지만, 배운 김에 super()를 써봤다.
    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def __init__(self, name): # Bird 클래스에도 마찬가지고 상속해줬다.
        super().__init__(name)

    def fly(self):
        print('%s! 푸드덕!' % (self.name))


dog = Dog('멍멍이')
dog.walk()  # 멍멍이! 걷는다!
dog.bark()  # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk()  # 구구! 걷는다!
bird.eat()  # 구구! 먹는다!
bird.fly()  # 구구! 푸드덕!

```



## 3.

```python
# ZeroDivisionError: 어떤 수를 0으로 나눴을 때 발생하는 에러입니다.
# NameError: 지정한 변수가 코드 내에 없을 때 발생합니다.
# TypeError: 어떤 연산을 할 때나 특정 메소드를 실행할 때, 올바른 타입이 아닌 값이 들어가면 발생합니다. argument가 누락되거나, 너무 많이 들어가 있을 때도 발생합니다.
# IndexError: 특정 sequence에서 인덱스로 항목을 찾을 때 찾는 항목이 존재하지 않거나 sequence의 길이를 벗어나면 발생합니다. 예를 들어, a = [1, 2, 3] 이렇게 인덱스상 0부터 2까지 있는 리스트에서 a[3]을 찾을 때 나타나는 에러입니다.
# KeyError: 특정 딕셔너리에 지정한 키가 없으면 발생합니다.
# ModuleNotFoundError: 어떤 모듈을 import할 때, 찾는 모듈이 없으면 발생합니다.
# ImportError: 모듈은 있지만, 모듈 내 찾는 클래스나 함수 등이 없으면 발생합니다.
```
