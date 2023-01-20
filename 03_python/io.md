# io module

입출력 작업을 위한 모듈

따로 `import` 하지 않아도 된다.

## 1. 사용법

기본 사용 방법은 다음과 같다.

`f = open(file_directory, mode)`

mode에 들어갈 수 있는 모드는 대표적으로 3가지가 있다.

- `'r'`: 읽기(기본값)
- `'w'`: 파일 생성(파일이 있으면 덮어쓰기) 후 쓰기
- `'a'`: (파일이 없으면)파일 생성 후 뒤에 붙이기

아래 예시에는, `./resource/` 경로에 리소스 파일들이 존재한다고 가정한다. 



### I. 기본 읽기

```python
f = open('./resource/python.txt', 'r') # 파일을 특정 모드로 불러옴

print(f) # class io wrapper 형태 => 그냥 list(f)해도 리스트 형태로 출력되지만, 이쁘지 않으니 아래 전용 메서드들을 사용한다.

contents = f.read() # 전체 파일 읽기 => 전체 파일을 string으로 읽어온다.

print(contents) # read() contents에 할당 후 사용

f.close() # open 후 닫아주지 않으면 메모리 낭비가 된다.
```



### II. with를 이용한 입출력

- `with` 문을 사용하면 `close()`를 사용하지 않아도 자동으로 닫힌다
  - 따라서 메모리 누수가 발생하지 않는다.

```python
with open('./resource/python.txt', 'r') as f:
    
    # 위와 마찬가지로, read()등으로 contents에 할당 후 사용
    contents = f.read()
```



## 2. io 어트리뷰트 & 메서드

### II. 메서드

#### 1) read()

- 파일을 하나의 문자열로 한 번에 다 읽는다.
- 한 번에 다 읽기 때문에, 이후 다시 `read()`해도 빈 문자열이 읽힌다.

```python
with open('./resource/python.txt', 'r') as f:
    
    contents = f.read()
    print(contents)
    
    contents = f.read()
    print(contents) # 빈 문자열이 읽힌다.
```



#### 2) readline()

- 파일을 한 줄에 