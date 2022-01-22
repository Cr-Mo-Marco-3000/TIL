# 0118_workshop



## 1.

```python
# 1. 
given_num = int(input())

if 1 <= given_num <= 1000:
    for i in range(1, given_num + 1):
        if given_num % i == 0:
            print("{0} ".format(i), end="")
else:
    print("유효한 숫자가 아닙니다!")

# 2.

given_num = int(input())

# 초기화된 문구를 만듭니다.
sentence = ""

if 1 <= given_num <= 1000:
    for i in range(1, given_num + 1):
        if i == 1: # 얘가 없으면 숫자 나열의 처음부터 띄어쓰기가 붙어버려요
            sentence = sentence + "1"
        elif given_num % i == 0: 
            sentence = sentence + " " + str(i)
    print()
else: # 처음 if문과 이 else를 for 안에 넣으면 이 문구가 반복 출력되기도 합니다.
    print("유효한 숫자가 아닙니다!")

print(sentence)
```



## 2.

```python
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]

numbers.sort()
print(len(numbers))

if len(numbers) // 2:
    print(numbers[(len(numbers) // 2)])

```



## 3. 

```python
sentence = ""  # 문장을 초기화했습니다. 이후에 문장에 글자를 더해줄거에용.

num = int(input())  # 숫자를 입력받아용.

while_num = 1  # while에서 순환할 숫자에용.

for_num = 1  # for에서 순환할 숫자에용.

while while_num <= num:

    for i in range(1, for_num + 1):
        sentence = sentence + str(i) + " "
    print(sentence)

    sentence = ""  # 이거 초기화 안해서 1시간 반동안 해멨어용. 다음부터는 조건문에서 초기화를 중요시하도록 하세용.
    i = 1 # i 초기화는 for 문이 다시 시작될 때 되기 때문에 딱히 필요가 없어요! 하지만 써놨으니 기억하라는 의미에서 그냥 갈께요.
    for_num += 1
    while_num += 1

```

