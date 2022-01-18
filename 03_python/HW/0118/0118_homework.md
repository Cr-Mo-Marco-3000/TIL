# 0118_homework



# 1.

```python
Mutable = [List, Set, Dictionary]

Immutable = [String, Tuple, Range]


```



# 2.

```python
# range
a = []

for i in range(50):
    if i % 2 == 1:
        a = a + [i]
print(a)	


# range + slicing
b = []
for i in range(50):
    b = b + [i+1]
c = b[0:50:2]
    
print(c)

# list comprehension

a = [idx for idx in range(1,51,2)]
```



## 3.

```python


a = {
    "김재석": 30,
    "고은민": 27,
    "구홍지": 25,
    "권민주": 26,
    "김남훈": 28,
    "김민준": 27,
    "김윤지": 27,
    "김철현": 29,
    "김현영": 30,
    "도진욱": 28,
    "백경원": 26,
    "변정호": 29,
    "손주호": 29,
    "이도운": 30,
    "이동준": 27,
    "이병승": 28,
    "이보나": 25,
    "이주영": 28,
    "전상현": 27,
    "정진아": 30,
    "최병성": 29,
    "최영찬": 27,
    "홍인표": 28,
    "조혜림": 26,
}
```

## 4.

```python
n = 5
m = 9

for hor in range(m):
    print("*" * n)

```



## 5.

```python
temp = 36.5

print('입실 불가') if temp >= 37.5 else print('입실 가능')
```



## 6.

```python
scores = [80, 89, 99, 83]


idx = 0
total_score = 0
while idx < 4:
    total_score = total_score + scores[idx]
    idx += 1

print(total_score)

```

