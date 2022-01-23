# JSON Data

- JSON은 자바스크립트 객체 표기법으로 개발환경에서 많이 활용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함

- *문자 기반(텍스트) 데이터 포맷*으로 **다수의 프로그래밍 환경에서 쉽게 활용 가능함**

  - 텍스트를 언어별 데이터 타입으로 변환시키거나
  - 언어별 데이터 타입을 적절하게 텍스트로 변환

  

- 활용법

```python
# JSON 파일은 파일의 표기법이 파이썬의 Dictionary와 비슷함
# 파이썬에서는 open함수를 이용하여 사용

{a, b, c}, 
{d, e, [f, g, h]},
.....


# 객체(리스트, 딕셔너리)를 JSON으로 변환
import json
x = [1, 'simple', 'list']
json.dumps(x)
# => '[1, "simple", "list"]'

# JSON을 객체(리스트, 딕셔너리 등)으로 변환
x = json.load(f)

# open()와 함께 활용
get_json = open("C:/Users/bizyo/ssafy7/TIL/03_python", mode='r', encoding=utf-8)
use_json = json.load(open)
# 이제 use_json를 딕셔너리나 리스트 등으로 이용 가능!

```

