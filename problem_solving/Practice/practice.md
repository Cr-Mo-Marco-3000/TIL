# Practice



## 1.1 종합소득세 계산하기

A라는 나라에서는 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용된다.

즉, 1,300만원을 벌었을 경우 `1,200*0.06 + 100*0.15`를 계산한 결과가 납부해야 하는 세액이다.

납부해야하는 세금의 결과를 반환하는 함수 `tax()`를 작성하시오.

```python
def tax(won):
    if won >= 4600:
        payment = (won - 4600) * 0.35 + 72 + 510
        
    elif won >= 1200:
        payment = (won - 1200) * 0.15 + 72
    else:
        payment = won * 0.06
    return payment
```



## 1.2 카쉐어링 요금 계산하기

카쉐어링 서비스는 요금을 다음과 같이 계산한다.

대여는 10분 단위로 가능하다.

대여 요금 : 10분당 1,200원

보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산)

주행 요금 : km당 170원 (주행 요금은 100km가 넘어가면, 넘어간 부분에 대하여 할인이 50% 적용)

예) 160km를 달렸으면, 170*100 + 85 *60

양의 정수인 대여시간(분)과 주행거리를 받아 계산 결과를 반환하는 함수 `fee()`를 작성하시오.

참고 함수 [`math.ceil`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)

```python
def fee(minute, distance):
    import math
    
    lent_fee = math.ceil(minute / 10) * 1200

    if (minute % 30) >= 20:
        insurance_fee = (minute // 30) * 525 + 525
        
    elif 0 <= (minute % 30) < 20:
        insurance_fee = (minute // 10) * 175 
    
    if distance > 100:
        ride_fee = ((distance - 100) * 0.5 * 170) + 17000 # 0.5 * 170을 안 해줬다.
        
    elif 0 <= distance <= 100:
        ride_fee = distance * 170
   
    total_fee = lent_fee + insurance_fee + ride_fee
    
    return total_fee
    
    
```



## 1.3 문자열 탐색

문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 카운트하는 함수 `start_end()`를 작성하시오.

```python
def start_end(words):
    total = 0
    for word in words:
        if (len(word) >= 2) and (word[0] == word[-1]):
            total += 1
    return total   
```



## 1.4 Collaz 추측

1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측이다. 그 원리는 아래와 같다.

1. 입력된 수가 짝수라면 2로 나눈다.

2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.

3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.

   예를 들어, 입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.

위 작업을 몇 번이나 반복해야하는지 반환하는 함수 `collatz()`를 작성하시오 (단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)

```python
def collatz(num):
    count = 0
    while count < 500:
        
        if not num % 2: # 짝수일때
            num = num / 2
            
        elif num % 2: # 홀수일때
            num = (num * 3) + 1
        
        count += 1 # 짝수든, 홀수든 작업이 끝나면 1을 더한다.
        
        if num == 1:
            return count
    return -1
        
```



## 1.5 딕셔너리 뒤집기

딕셔너리는 기본적으로 key와 value로 이뤄져있다.

딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하시오.

```python
def dict_invert(my_dict): # map, enumerate, items, update, for 두번쓸까?
    my_list = []
    new_key_list = []
    value_pack = []
    ans_dict = {}
    
    for key, value in my_dict.items():
        my_list.append([value, key])
        new_key_list.append(value)
    
    new_key_set = set(new_key_list)

    for key in new_key_set: # key set 10 20 30
        
        for twin_set in my_list:# [10 1] [20 2] 30 3 30 4
            
            if key == twin_set[0]: # 1
                value_pack.append(twin_set[1]) 
                
        ans_dict.update({key:value_pack}) # for 조건문 안으로 잘못 잡았다.
            
        value_pack = []
    print(ans_dict)

# def dict_invert(my_dict):
#     new_dict = {} 
#     for key in my_dict:
#         new_dict.setdefault(my_dict[key], []).append(key)
#     return new_dict

```

