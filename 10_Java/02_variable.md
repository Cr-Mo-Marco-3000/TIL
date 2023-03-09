# Variable

변수는 하나의 값을 저장할 수 있는 메모리 번지에 붙여진 이름



## I. 변수 선언

- 변수를 선언할 때는 타입과 이름을 결정한다.
- 규칙
  - 첫 번째 글자가 문자여야 함
  - 중간부터는 문자, 숫자, $, _를 포함 가능
  - camelCase로 작성
    - 자바 소스 파일명(클래스명 - .java)는 Upper Camel Case(Pascal Case)로 작성
    - 변수명은 camelCase로 작성

```java
int age; // 정수(int)를 저장할 수 있는 age 변수
double value; // 실수(double)을 저장할 수 있는 value 변수

// 변수를 선언 후 대입(assign)
int score;
score = 90;
```

- 변수에 최초로 값을 대입하는 행위를 변수 초기화라고 하고, 이때의 값을 초기값이라고 한다.

```java
// 변수 초기화
int score = 90;
```

- 변수 선언은 저장되는 값의 타입과 이름만 결정
  - 초기화되지 않은 변수는 아직 메모리에 할당되지 않음, 따라서 변수를 통해 메모리 값을 읽을 수 없다.
    - 초기화되지 않은 변수를 연산식에 사용할 경우 컴파일 에러가 발생한다.
  - 메모리 할당과 저장은 변수에 값이 대입될 때 수행

- 변수는 또 다른 변수에 대입되어, 메모리 간에 값을 복사할 수 있다.

```java
int x = 10;
int y = x; // 변수 y에 변수 x 값을 대입
```

- 두 변수의 값을 교환
  - 파이썬처럼은 안 되고, 새 변수를 생성해 값을 대입해주어야 한다.

```java
package ch02.sec01
    
public class void main VariableExchangeExample{
    public static void main(String[] args) {
        int x = 3;
        int y = 5;
        System.out.println("x: " + x + ", y: " + y) // x: 3, y: 5        
            
        int temp = x;
        x = y; // 이미 x는 int로 선언되었음으로 재선언 할 필요가 없다.
        y = temp;
        System.out.println("x: " + x + "y: " + y) // x: 5, y: 3
    }
}
```



## II. 정수 타입