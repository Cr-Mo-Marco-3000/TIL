# 0119_workshop

 ## 1.

```python
def list_sum(int_list):
    total = 0
    for i in int_list:
        total += i
    return total


iu = list_sum([1, 2, 3, 4, 5])

print(iu)

```



## 2.

```python
def dict_list_sum(dic_list):
    total = 0
    for i in dic_list:
        total += i['age']  # 실수 1: age에 따옴표를 씌우지 않아서 NameError가 떴다.
                           # 실수 2: +를 빼먹었다.
    return total


total_value = dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])

print(total_value)

```



## 3.

```python
def all_list_sum(long_list):
    total = 0 # 토탈 변수 초기화
    for i in long_list: # 주어진 리스트에서, 첫 번째 항목인 list를 뽑아낸다.
        for j in i: 
            total += j # 여기서 한 번 오류가 났는데, i[j]라고 했었다.
    return total       # 그렇게 쓸 거면 in 뒤에 range(len(i))가 들어가야 한다.


answer = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])

print(answer)
```





