# Variable

변수는 하나의 값을 저장할 수 있는 메모리 번지에 붙여진 이름



## 0. 자료형

자바에서의 자료형은 Primitive Type(8개)과 Reference Type으로 나뉨

### 1. Primitive Type

1. 정수형(4개)
   1. byte
      - 1byte
   2. short
      - 2byte
   3. int
      - 4byte
   4. long
      - 8byte

2. 실수형(2개)
   1. float
      - 4byte
   2. double
      - 8byte
3. 문자형
   - char
     - 2byte
4. 논리형
   - boolean
     - 1byte
     - `true` 또는 `false`만 가능
       - **0, 1 불가능**

### 2. Reference Type

원시형을 제외한 모든 자료형이 참조형이다.

class, array, annotation, enumerate, interface, string 등이 있다.

차후 학습한다.



### 참고: 리터럴

리터럴은 데이터값이다.

- 정수형 리터럴

  - 2진수
    - 0b로 시작
    - 0 또는 1 포함
    - `0b10101`

  - 8진수
    - 0으로 시작()
    - 0~7까지 포함
    - `017238`

  - 16진수
    - 0x로 시작
    - 0 ~ F까지 포함
    - `0xD13FA`


- 실수형 리터럴
  - 소수점
    - 3.14
    - **그냥 쓰면 기본적으로 double형으로 저장됨**
  - 지수표현
    - 6.02e23
    - 2.718F
    - 123.4E+306D
      - double 형임을 명시

- 문자

  - 한글자 표현

    - 문자형 리터럴은 메모리에 숫자로 저장되기 때문에 int에도 넣기 가능

  - `''`로 묶어 표시
  - 이스케이프 시퀀스

    - `\n`

  - 유니코드

    - `'\u4567'`

- boolean형 리터럴

  - true
  - false



## I. 변수

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
    - **초기화되지 않은 변수를 연산식에 사용할 경우 컴파일 에러가 발생한다.**
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

### 0. 기본형 변수

- 값이 저장

### 1. 참조형 변수

- 참조형 변수는 4byte
- 저장되는 값은 주소값 
  - => 한 번 더 가야지 값
  - 포인터와 비슷



### 2. 형변환

- 모든 데이터 간 형변환이 가능
  - 참조형도 가능
    - **클래스 형변환시에는 두 클래스가 상속관계여야 한다**

1. 묵시적 형변환

   - 아래는 자동으로 형 변환 가능한 형태
     - 화살표로 직접 연결되지 않아도 가능

   - **작은 타입은 큰 타입으로 자동으로(묵시적) 형 변환이 가능**
     - 할당 시
     - 반대 경우는 명시적 형변환 필요
     
   - char은 숫자이므로, 숫자형과 연산 가능
   

![image-20230406100934014](C:\Users\bizyoung93\Desktop\TIL\10_Java\02_variable.assets\image-20230406100934014.png)

2. 명시적 형변환
   - 타입 캐스팅이라고도 부름
   - `(데이터형)값`
   - **데이터 손실이 발생될 수 있음**

- 1 & 2 정리

```java
package p01;

public class variable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 123;
		// 기본적으로 Double로 저장되기에, F를 안 붙여주면 에러
		float f = 3.14F;
		double d = 3.14;
		char c = 'A';
		char c2 = '홍';
		boolean b = true;
		boolean b2 = false;
		String name = "홍길동";
		long longInt;
		// 출력
		System.out.println("정수" + n);
		System.out.println("실수" + f);
		System.out.println("큰 실수" + d);
		System.out.println("문자" + c);
		System.out.println("문자2" + c2);
		System.out.println(b);
		System.out.println(b2);
		System.out.println(name);
		
		// 작은 타입 => 큰 타입으로는 자동 형변환 가능
		int a = 300;
		float ab = a;
		System.out.println(ab);
		
		// 작은 타입 => 큰 타입이라 아래는 에러 
		/*
		int fToI;
		fToI = ab;
		*/
		
		// 자동 형변환
		short sh = 12;
		int num = 'a'; // 문자도 메모리에 저장될때는 정수이므로, 할당 및 연산 가능
		System.out.println(sh + num);
		
		// 명시적 형변환
		fToI = (int)ab;
		System.out.println(fToI);
		
        // long의 경우는 할당시 뒤에 L을 붙여야 한다.
        // longInt = 12312312312; // error
        longInt = 12312312312L;
	}

}

```
#### **연산시 데이터 형 변환 주의점**

1. int보다 작은 타입끼리의 연산 결과는 항상 int로 변환됨

```c
short a = 123;
short b = 4;
short c = a + b; // 에러발생
short d = (short)(a+b); // 형변환 연산자를 이용에서 에러 해결.
```

2. 작은 타입과 큰 타입을 연산할 때, 작은 타입은 자동으로 큰 타입으로 변환됨

3. 하지만, 데이터 크기 뿐 아니라, 정수 + 실수일 때는 

   => 실수;

4. 문자열 + 값

   - 계산이 아닌 연결이 된다.

   - 연결되어 문자열이 됨

```java
package p02;

public class typecast {

	public static void main(String[] args) {

		String arg1 = "너의 나이는 ";
		int arg2 = 23;
		String arg3;
		arg3 = arg1 + arg2;
		System.out.println(arg3);	
	}
}
```




### 3. 스코프

- 블록 스코프

  - 같은 블럭 내부에서는 중복된 이름 사용 불가
  - 블록 내부에서 선언된 이름은 블록 안에서 혹은 자식 블록에서만 사용 가능

  ```java
  package p01;
  
  public class scope {
  
  	public static void main(String[] args) {
          {
              int n = 10;
          }
          {
              int n = 20;
          }
  ```

  

## 2. 변수의 종류

1. 로컬 변수

   - 메서드 안에서 선언
   - 메서드가 호출시 생성, 메서드 종료시 소멸
     - 매번 생성
   - **스택 영역에 저장**
   - **사용 전 초기화 필수**

2. 인스턴스 변수

   - 메서드 밖에서 선언
   - 객체 생성시 생성, 객체 소멸시 소멸
     - 객체 생성시 생성
       - 객체 생성은 new를 통해 선언
       - `className variableName = new className();`
     - 객체별로 unique한 값을 저장하고자 할 때
   - **힙 영역에 저장**
   - **초기화 안하면 임의의 값으로 자동 초기화**
     - 인스턴스, 클래스 변수를 초기화하지 않았을 때 임의의 값
       - 정수형: 0
       - 실수형: 0.0
       - 문자형: `\u0000`
       - 논리값: false
       - 참조형: NULL

3. static 변수

   - class변수라고도 함

   - 메서드 밖에서 선언
     - static이란 키워드로 사용(사용 안하면 인스턴스 변수)
   - 프로그램 실행시 생성, 프로그램 종료시 소멸
     - **즉, 딱 한번만 생성된다.**
     - 어떤 값을 누적하거나 할 때 사용한다.
   - **method area(Permanent Generation space)에 저장되었음**
     - **JAVA 8부터는 JAVA HEAP 영역에 저장(String과 마찬가지)**
       - 원래 Perm Gen space는 HEAP 영역의 특수한 공간이었는데, 이것이 그냥 HEAP 영역으로 옮겨진 것
       - [참고](https://stackoverflow.com/questions/8387989/where-are-static-methods-and-static-variables-stored-in-java)
     - 가비지 콜렉터의 대상이 됨
   - **초기화 안하면 임의의 값으로 자동 초기화**

- 생성 및 소멸 순서
  - static 생성 => instance 생성 => local 생성 => local 소멸 => instance 소멸 => static 소멸
  
  

```java
public class Variable
    
    int instanceV = 3; // 인스턴스 변수
    static char staticV = 'a'; // 스태틱 변수 == class 변수

	int n = 30;

	i
    public static void main(String[] args) {
    	int localV = 35; // 로컬 변수
    	
        int n = 30; // 인스턴스 변수와 동일한 이름으로도 사용 가능
        
        System.out.println(n);
}
```

- 인스턴스 생성과 변수 사용법

```java
package p01;

public class variable {
	
	int m1;
	
	static String m2;
	
	
	public static void main(String[] args) {
		
		int n=0;
		
		System.out.println(n);
		
		variable t = new variable(); 	 // 인스턴스 생성 => 클래스 변수에 인스턴스를 할당
		
		System.out.println(t.m1); 		 // 인스턴스 변수 사용법
		
		System.out.println(variable.m2); // 클래스 변수는 객체생성 없이 클래스명으로 접근
										 // 초기화하지 않았으므로 NULL이 들어가 있음	
	}
}

```



## 3. 상수

- 상수는 final 키워드로 선언
- 반드시 초기화 필요

```java
final int apple = 3;
```

