# 연산자

## 1. 산술연산자

- `+ - * / %`
- 정수와 정수 간 연산은 정수 형태로, 실수와 정수 간 연산은 실수 형태로 출력
  - 즉, 9/3은 몫인 3이 나온다.

- `+` 는 문자열을 연결할때도 쓰인다.

## 2. 비교 연산자

- 우리가 아는 비교 연산자
- 비교 연산자의 연산 결과는 boolean값이므로, boolean 변수에 저장 가능

- 문자열을 비교할 때는 ==가 아니라, equals() 메서드가 필요하다.



```java
public class Compare
    public static vold main(String[] args) {
    	String s1
}
```



## 3. 대입 연산자

- 우리가 아는 그 대입 연산자
- 복합 대입 연산자 가능



## 4. 증감 연산자

- 전위 연산, 후위 연산 가능
  - 전치 연산, 후치 연산이라고도 함
  - `++n, n++`
  
- 다른 연산과 같이 사용시, 전치는 먼저, 후치는 나중에 연산

## 5. 논리 연산자

- `&&`
- `||`
- `!`

- 단축 평가(short circuit operation) 가능
  - 이클립스에서, 실행하지 않는 부분은 노란색 밑줄로 표시됨
  - 예를 들어, 논리연산자 사용시, 단축평가를 통해 뒤쪽으로 넘어가지 않는 경우




## 6. 3항 연산자

- `변수 = 조건식 ? 값1 : 값2`



## 7. 참조형의 데이터타입 체크

- instanceof 연산자

- 결과값으로 논리값 반환
- 형식
  - `변수 instanceof 클래스`
  - `myString instanceof String`