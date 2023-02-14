# 모듈: 기능 단위로 구분 되어진 파일
# 패키지: 모듈을 모아둔 디렉토리 

# calculator에서 Calculator 클래스를 가져오기
from pkg.calculator import Calculator
from pkg.calculator import *


# calc = Calculator()
print(Calculator.plus(1, 20))
# print(plus(1, 3))


# from pkg.calculator2 import plus as pl, minus as mn
# 모듈 사용2(함수)
# print(pl(1, 3))
# print(mn(1, 3))

# 모듈 사용3()
# import builtins
# dir => 모듈 기능 출력
# print(dir(builtins))