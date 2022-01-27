# 0127_workshop

 ## 1.

```python
class Point:

    def __init__(self, x, y): # 처음에는 상속 관련 문제인가 했는데,
        self.x = x            # 점과 사각형이 같은 속성을 공유하는 건 아닌 것 같아서
        self.y = y            # 그냥 겹친 메서드로 풀었다.
							  # 이 부분은 class Point의 인스턴스 변수,
                              # 즉 속성을 정의하는 부분이다.

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1  # 처음에 매개변수 명을 p1, p2로 하려다 햇깔릴 것 같아서 바꿨다.
        self.point2 = point2  # 매개변수 자체를 다른 클래스의 인스턴스로 받는다.

    def get_area(self): # 넓이를 반환하는 메서드이다, 보다시피 이중 메서드를 썼다.
        return abs((self.point1.x - self.point2.x) * (self.point1.y - self.point2.y))

    def get_perimeter(self): # 이 부분도 마찬가지로, if문을 쓰려다 간단하게 절대값을 취했다.
        return 2 * (abs(self.point1.x - self.point2.x) + abs(self.point1.y - self.point2.y))

    def is_square(self): #조건을 쪼개, 가로 세로의 길이가 같으면 True를, 아니면 False를 반환한다.
        if abs(self.point1.x - self.point2.x) == abs(self.point1.y - self.point2.y):
            return True
        return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

'''
제시문대로 출력 완료!
4
8
True
9
12
True
'''
```

