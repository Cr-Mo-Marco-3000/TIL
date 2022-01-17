# 0117_workshop

## 1.

```python
a = int(input())

for i in range(1, a + 1):
    print(i)
```





## 2.

```python
a = int(input())

for i in range(a, 0, -1):
    print(i)
    if i == 1:
        print(0)

```



## 3. 

```python
a = int(input())
total = 0
b = 0

if a > 10000:
    print("10000이 넘는 숫자는 주어질 수 없습니다.")
else:
    while b <= a:
        total += b
        b += 1
    print(total)
```

