# 0120_workshop

 ## 1.

```python
def get_secret_word(words):
    return "".join(map(chr, words))


print(get_secret_word([83, 115, 65, 102, 89]))

get_secret_word([83, 115, 65, 102, 89])

```



## 2.

```python
def get_secret_number(name):
    # map 함수를 이용하여 아스키 숫자들을 뽑아낸다.
    return sum(map(ord, name))


get_secret_number('tom')
```



## 3.

```python
def get_strong_word(x, y):
    # for문을 사용해서 아스키 숫자의 합을 더하는 코드를 만든다
    total_x = 0
    for i in x:
        total_x += ord(i)
    # map 함수를 사용해서 아스키 숫자의 합을 더하는 코드를 만든다
    total_y = sum(map(ord, y))
    # x 문자열을 반환한다.
    if total_x >= total_y:
        return x
    # y 문자열을 반환한다.
    elif total_y >= total_x:
        return y


get_strong_word('z', 'a')
get_strong_word('tom', 'john')
# 놀랍게도 한 번도 안 틀렸다.
```

