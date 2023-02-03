# 예외: 코드 실행시 발생할 수 있는 문제
# error: 시스템 상에서 발생하는 문제

# 예외 종류
# SyntaxError, Type, Index, Value, key

"""
1. SyntaxError
=> 문법적인 예외
"""
# print('앙냥냥)

""" 
2. NameError
=> 참조 변수가 초기화 되지 않거나 존재하지 않는 예외 
"""
# print(a)

"""
3. ZeroDivisionError
=> 0으로 나눌 수 없다는 예외
"""
# a = 10 / 0

"""
4. IndexError
=> 존재하지 않는 인덱스를 참조 할 때
"""
# a = [0, 1, 2]
# print(a[5])
# 또는
# while True:
#   a.pop()


"""
5. KeyError
=> 키가 존재하지 않을 때 발생하는 예외
"""
# yb = {'name': 'yb', 'age': 25, 'city': 'SU'}
# print(yb['name']) # 에러발생
# print(yb.get('name')) # 에러 발생하지 않음 => 파이썬 권장

"""
6. AttributeError
=> 클래스 혹은 모듈이 갖고 있지 않은 속성 사용시 발생하는 예외
"""
# import time
# print(time.time())
# print(time.month())

"""
7. ValueError
=> 참조값이 존재하지 않는 경우 발생하는 예외
"""
# a = [1, 2, 3]
# print(a.index(4))
# print(a.remove(1))

"""
8. FileNotFoundError
=> 존재하지 않는 파일 사용시 발생하는 에러
"""
# f = open('test.txt', 'r')'

"""
9. TypeError
=> 데이터타입에 알맞지 않은 연산시 발생하는 예외
"""


"""
# 예외처리 형태 1

try:
    수행코드
except 예외명:
    예외처리 수행코드
[except 예외명2:
    예외처리 수행코드2]
[else:
    예외 발생하지 않는 경우 수행 코드]
[finally:
    항상 수행하는 코드]
"""

# try:
#     last_names = ['lee', 'hong', 'kim']
#     search_name = 'sadf'
#     idx = last_names.index(search_name)
#     print(f'{search_name}은 {idx+1}번째에 위치하고 있습니다.')
# except ValueError:
#     print('찾으시는 성이 없습니다.')
# except TypeError:
#     print('검색하신 last name은 존재하지 않습니다.')
# else:
#     print('예외 발생하지 않았습니다.')
# finally:
#     print('무조건 실행되는 구문입니다.')


"""
# 예외처리 형태 2
=> except가 없으면 finally라도 들어와 주어야 함

try:
    수행 코드
finally:
    수행 코드
"""


"""
# 예외처리 형태 3

## 1) 예외 발생시키기
=> raise 예외명

## 2) 여러 개의 에러 묶기
=> raise (예외명1, 예외명2)

## 3) raise Exception
=> 모든 예외를 처리할 수 있는 객체
=> 모든 except의 마지막에 들어가야 함
=> 앞에 있으면 다른 에러보다 먼저 받아버림

## 4) 사용자 지정 에러 만들기
=> 
Error 클래스를 상속받아서 만든다.
=>
class NotFoundParkError(Exception):
    print('사용자 정의 예외---')

## 5) 에러 이름 지정
=> 특정 에러의 이름을 바꿔서 출력하거나, raise from 문을 써서 에러를 추적할 때 사용한다.
except ValueError as VE:
    print('에러발생', VE)
"""

# try:
#     last_name = 'kim'
#     if last_name == 'park':
#         print('park을 찾았습니다.')
#     else:
#         # 에러를 무조건 발생시킨다.
#         raise ValueError

# except ValueError:
#     print('park를 찾지 못했습니다.')

# except (KeyError, NameError):
#     print('여러 개의 에러 처리')

# except Exception:
#     print('다른 모든 에러 처리')

# 4) 임의 에러 만들기
# class NotFoundParkError(Exception):
#     print('사용자 정의 예외---')


# try:
#     input('입력주세요!')
# except Exception:
#     print(Exception)
#     print('에러!')

# except와 except Exception은 다름
# https://stackoverflow.com/questions/40280776/use-of-except-exception-vs-except-raise-in-python
# https://stackoverflow.com/questions/18982610/difference-between-except-and-except-exception-as-e

try:
    my_list = [0, 1, 2]
    print(my_list[10])
except Exception as e:
    print(dir(e))
    print(e)
