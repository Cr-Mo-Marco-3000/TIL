# 0119_homework



 ## 1.

```python
# len(), print(), sorted(), enumerate(), list(), abs(), divmod() 등이 있습니다.
# 앞으로 더 배워나갑시다. sorted() 몰라서 어제 2번 못 풀었습니다.
```



## 2.

```python

def get_middle_char(char): # 함수를 정의합니다.
    if len(char) % 2 == 1: # 함수의 길이가 홀수인 경우에는 한 글자를 반환
        return char[len(char) // 2]
    else:
        return char[len(char) // 2 - 1] + char[len(char) // 2] 
    # 짝수인 경우에는 문자 두 개를 합쳐 반환합니다.


ssafy = get_middle_char("ssafy")
coding = get_middle_char("coding")

print(ssafy, coding)

```



## 3.

```python
def ssafy(name, location="서울"):
    print(f"{name}의 지역은 {location}입니다.")
          
# (4)의 경우에는 오류가 발생한다.
# keyword argument를 사용할 경우, positional argument 다음(오른쪽)에는 
# 사용할 수 없기 때문입니다.
```



## 4.

```python
# none입니다. 함수에 return값이 없기 때문입니다.
# print는 그냥 개발자에게 보여주는 용도로만 사용됩니다. 조심해야 합니다.
```



## 5.

```python
def my_avg(*arg):
    total = 0  # 처음에는 함수 바깥에 작성했었는데 생각해보니 그럼 재사용할 때 돌아가지 않을 것 같아서 내부에 넣었습니다.
    for i in arg:  # arg눈 iterable한 객체라서 걍 써도 됩니다.
        total += i
    return total / len(arg)  # 평균을 구합니다.


mean_value = my_avg(77, 83, 95, 80, 70)
# 다른 변수에 결과값을 대입하는 게 왜 안전한지는 까먹었는데 그냥 하겠습니다.

print(mean_value) # 프린트


```



