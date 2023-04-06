# Java Intro

## 1. 자바의 특징

자바의 대표적인 특징은 다음과 같다

1. 플랫폼으로부터 독립적이다.
2. 객체 지향 프로그래밍을 지원한다
3. 메모리를 자동으로 관리한다

등이 있다.



### 자바 라이선스

오라클이 가지고 있으며, 오라클은 자바 개발 도구(JDK: Java Development Kit)을 배포하여 기술적 지원을 함



## 2. 자바 설치

Java SE(Standard Edition)의 구현체에는 Open JDK가 있고 Oracle JDK가 있다.

Opne JDK 버전의 LTS 버전인 17버전을 설치하자.

공식 사이트에서보다는 이클립스 재단에서 관리하는 adoptium 사이트에서 다운로드 하는 것이 좋다.

### 1. 윈도우에서 설치

1. JDK 설치 경로를 `C:\Program Files\Java\jdk-17.0.6`으로 바꾼 후 설치 진행
   - 사용 버전에 따라 이름을 달리해 준다.

2. 환경 변수 설정 JDK 설치 후 프로그램들이 JDK를 이용할 수 있도록 JAVA_HOME 환경 변수를 생성하고, Path 환경 변수를 수정한다.
   1. 윈도우의 시스템 속성에서 환경 변수 클릭
   2. 시스템 변수 새로 만들기에서 다음과 같이 생성
      - 변수 이름
        - JAVA_HOME
      - 변수 값
        - 위에서 지정한 폴더 경로 `C:\Program Files\Java\jdk-17.0.6`

3. Path 환경 변수 편집

   - path 환경변수란 프로세스 또는 사용자가 명령을 내릴 때, 해당 명령을 찾기 위한 디렉토리를 지정하는 것이다

   - `C:\Program Files\Java\jdk-17.0.6`경로에 들어가면 bin 디렉토리가 있는데, 이곳에는 다양한 명령어들이 존재한다
   - 대표적으로 자바 소스 파일을 컴파일해주는 javac.exe와 자바 프로그램을 실행해주는 java.exe 명령어가 있다.
   - 위 두 명령어는 터미널에서 컴파일하고 실행될 때 사용된다. 이를 어떤 위치에서도 사용 가능하게끔 Path 환경 변수에 추가해주자.
     -  **시스템 변수** Path에서 편집을 누른 후 새로 만들기, `%JAVA_HOME%\bin`입력
       - `%JAVA_HOME%`에는 위에서 지정한 환경 변수의 값(폴더 경로)를 의미
         - 즉 `%JAVA_HOME%\bin` === `C:\Program Files\Java\jdk-17.0.6\bin`
       - 이후 생성한 `%JAVA_HOME%`를 맨 위로 올려준다
         - 이는 Path 환경 변수에 등록된 순서대로 명령어를 찾기 때문이다.
         - 만약 다른 버전 등의 명령어가 더 위에 있을 경우, 다른 버전의 명령어가 사용될 수 있으므로 주의 

4. 환경 변수 설정 확인
   - 명령 프롬프트에서
     - `javac -version` 입력
     - `java -version` 입력
   - 만약 설정이 잘못 된 경우 환경변수를 확인, 수정한 후 터미널을 재시작해야 한다.

## III. 자바 구동 방식

- 자바는 컴파일 방식과 인터프리터방식을 혼용한다.

1. 자바 소스 파일 작성

   - 확장자는 `.java`
   - **해당 파일명은 클래스명과 일치(대문자로 시작)**
   - 텍스트 파일

2. 컴파일러의 컴파일을 통해 바이트코드 파일 생성

   - 확장자는 `.class`

   - `javac`(java compiler) 명령어를 통해 소스 파일을 컴파일

   - **어떤 운영체제에서도** **동일한 소스 파일**을 컴파일하면 **동일한 바이트코드** 파일 생성
     - 즉, 동일한 .class파일 생성
     - 다시 컴파일 할 필요가 없음
   - **개발 완료된 자바 프로그램 형태**

3. 자바 가상 머신 구동

   - 바이트코드 파일을 특정 운영체제가 이해하는 기계어로 번역 & 실행시키는 명령어는 `java`
   - 해당 명령어는 JDK와 함께 설치된 자바 가상 머신(Java Virtual Machine)을 구동시켜 바이트코드를 기계어로 번역 & 실행
     - 자바 가상 머신 내부의 자바 인터프리터와 JIT 컴파일러가, 바이트코드를 한줄씩 기계어로 번역해가며 실행됨
   - 바이트코드 파일은 운영체제와 상관없이 동일하지만, JVM은 해당 바이트코드를 각 운영체제에서 이해할 수 있는 서로 다른 기계어로 번역하므로 운영체제별로 다른 JDK를 설치한 것이다.

### Java Virtual Machine

- S/W not H/W

- 주요 기능: `.class`(bytecode) 실행

- 자체적인 메모리 포함
- JDK 설치할 때 포함
- 포함관계
  - JDK(Java Development Kit)
    - 개발도구 포함
      - Javac
    - JRE(java runtime enviroment)
      - 실행환경 포함
      - .class
      - JVM

- 운영체제에 의존적(독립적이지 않음)

## IV. 소스 작성 및 실행 실습

1. 아래와 같이 디렉토리 구조 생성
   - 소스 파일 및 컴파일된 바이트코드 파일을 쉽게 관리하게 위해서 패키지 사용

```java
temp
|-- src // 소스 파일이 저장되는 디렉토리
|    |-- ch01 // 패키지 디렉토리
|		   |--sec06 // 패키지 디렉토리
|				|--Hello.java // 소스 파일			
|
|-- bin // 바이트코드 파일이 저장되는 디렉토리
```

2. Hello.java에 입력

```java
package ch01.sec06; // 바이트코드 파일이 위치할 패키지 선언

public class Hello { // Hello 클래스 선언
    public static void main(String[] args) { // main() 메서드 선언
        System.out.println("Hello, Java!") // 콘솔에 출력하는 코드
    }
}
```

2. 소스 파일을 javac 명령으로 컴파일
   1. temp 디렉터리에서 다음 명령어 실행
      - `javac -d [바이트코드파일저장위치] [소스경로 | *.java]`
        - `*.java`는 확장명이 .java인 모든 파일
        - `-d`는 디렉토리 지정 명령
      - `javac -d bin src/ch01/sec06/Hello.java`
      - 자바 컴파일 시 주석에 한글에 있으면 오류 발생
3. 바이트코드를 기계어로 번역 후 실행
   - `java -cp [바이트코드파일위치] [패키지...클래스명]`
     - `-cp`는 class path
       - 클래스 파일을 검색하기 위한 디렉토리
   - `java -cp bin ch01.sec06.Hello`
   - 뒤의 클래스명에는 `.class`를 붙이면 안된다.
   - 콘솔에 Hello, Java 출력
   - 해당 바이트코드는 다른 운영체제에서도 정상적으로 실행 가능하다.



## V. 이클립스 설치

인스톨러보다 압축 형태로 다운받은 후, 해당 경로에 압축을 푼다

`C:\Program Files\eclipse`

프로젝트가 저장될 워크스페이스 생성

`C:\ThisIsJavaSecondEdition\workspace`



## VI. 프로젝트 생성

- 워크스페이스는 하나의 프로그램 단위
- 프로젝트란 하나의 실행 파일이 생성되는 단위
- 패키지는 유사한 기능을 가진 클래스들을 모아놓은 단위

1. File => New => Java Project
2. JRE 옵션
   - Use an execution environment JRE
     - 기본 선택
     - 선택된 JavaSE 버전 기준으로 소스 파일을 컴파일하고 실행
     - 빌드 번호와 상관없이 JavaSE 버전에 중점을 둘 때 선택
   - Use a project specifir JRE
     - 선택된 JDK 기준으로 소스 파일을 컴파일하고 실행
     - 빌드 번호별로 JDK를 선택할 때 유용
   - Use default JRE 'xxx' and workspace compiler preferences
     - 이클립스의 기본 자바 버전을 사용해서 소스 파일을 컴파일하고 실행
3. Create module-info.java file 체크 해제 후 Finish

4. 윈도우의 경우 기본 텍스트 파일 인코딩 변경 필요(MS949 => UTF-8)
   - 맥은 필요없음
   - Window => Preferences => General => Workspace => Text file encoding => Other => UTF-8



### Java, JDK, JRE, JavaSE 용어 정리

> 일반적으로 Java 버전을 언급할 때는 Java 17처럼 표현하지만, 다음과 같은 용어로 표현되기도 한다.
>
> Java 개발 도구에 중점: JDK 17
>
> Java 실행 환경에 중점: JRE 17
>
> Java 스펙 내용에 중점: JavaSE-17
>
> JavaSE(Java Standard Edition)은 자바 개발에서부터 실행까지의 모든 환경을 정의한 스펙을 말한다.
>
> JavaSE 스펙을 준수해서 만든 것이 OpenJDK, OracleJDK라고 생각하자



## VII. 소스 작성 후 실행

### 1. 패키지 생성

- Package Explorer 뷰에서 src 디렉토리를 선택한다.

- 마우스 오른쪽 버튼 => New => Package
- Name 입력칸에 패키지 이름(예시에서는 ch01.sec09) 입력 후 Finish

#### 패키지란?

- 패키지는 소스 파일과 바이트코드 파일을 관리하기 위한 디렉토리
- 상위 패키지와 하위 패키지를 구분짓는 기호는 `.`
- 파일 시스템에서는 상위, 하위 디렉토리로 생성됨
- 기본적으로 이클립스에서는 패키지를 한 줄(Flat)으로 표시하지만, 메뉴 보기 아이콘을 클릭 후 Package Presentation 항목을 Hierarchical로 선택하면 계층 구조로 볼 수 있다.



### 2. 소스 파일 생성

- 위에서 만든 패키지를 선택 후, 오른쪽 클릭 => New => Class 선택
- Name 입력칸에 클래스 이름을 입력 후 main()메소드를 추가하기 위해 `public static void main(String[] args)`를 체크 후 Finish

#### 자동 컴파일

- 이클립스에서는 소스 파일을 저장하는 순간 자동으로 컴파일이 된다. 즉, **바이트코드가 자동으로 생성**된다.
- 생성된 바이트코드는 프로젝트 디렉터리 안 bin 디렉터리 안에, **패키지 디렉토리와 함께** 저장된다.
  - 즉, 패키지 디렉터리 구조와 바이트코드 디렉터리 구조는 같다.



### 3. 바이트코드 파일 실행

두 가지 방법 중 하나를 택하자

1. Hello.java 소스 파일을 선택하고 툴바에서 실행 아이콘 클릭
2. 오른쪽 클릭 => Run As => Java Application



## VIII. 코드 구조 이해

1. 패키지 선언
2. 클래스
   - 클래스명은 숫자로 시작 불가
   - 공백 포함 불가
   - **소스 파일명(.java)와 대소문자가 완전히 일치해야 함(자동으로 그렇게 생성된다.)**
3. 메서드
   - **바이트코드 파일을 실행하면 main() 메서드 블록이 실행됨**
   - 따라서 **main() 메서드를 실행 진입점**이라고 부른다.

```java
// 패키지 선언 => 소스 파일이 ch01.sec09 패키지에 있다는 뜻
// 컴파일 후 생성되는 바이트코드 파일은 bin/ch01/sec09 패키지에 생성됨
// 소스 파일을 작성할 때는 우선 패키지 생성 후 작성해야 한다.
package ch01.sec09; 

// public class Hello => 클래스 선언, Hello => 클래스명
// 클래스명은 숫자로 시작 불가, 공백 포함 불가, 소스 파일명(.java)와 대소문자가 완전히 일치해야 함
// {} 클래스 블록 => 클래스의 정의 내용이 작성됨
public class Hello {
	
	// public ... {} => main() 메서드, public ... {} => 메서드 선언, main => 메서드명, {} => 메서드 블록
	// 바이트코드 파일을 실행하면 main() 메서드 블록이 실행됨
	// 따라서 main () 메서드를 프로그램 실행 진입점(entry point)라고 부른다.
	public static void main(String[] args) { 
		System.out.println("Hello, World!"); // 출력하는 코드
	}
}

```

4. 코드 주석

   - 문자열 내부에는 주석 작성이 불가능하다.

   - 종류는 세 가지가 있다.

     - 행 주석

     - 범위 주석

     - 도큐먼트 주석
       - javadoc 명령어로 API 도큐먼트를 생성하는 데 사용된다.
       - javadoc.exe 파일

```java
package ch01.sec11;
/**
 * 
 * 
 * @author bizyoung93
 * 이 부분은 도큐먼트 주석이라고 한다.
 * javadoc 명령어로 API 도큐먼트를 생성하는 데 사용된다.
 * 
 */
 
 /*
   이 부분은 범위 주석이라고 한다.
   여러 줄을 주석으로 처리한다.
 */

 // 이건 행 주석이다. //부터 행 끝까지 주석으로 처리한다.
public class Hello {

	public static void main(String[] args) {
		System.out.println("문자열 안에는 주석을 쓸 수 없다.");

	}

}

```

5. 실행문과 세미콜론
   - main() 메서드 블록 내부에는 다양한 실행문이 작성된다.
   - 실행문 끝에는 반드시 세미콜론을 붙여야 한다.

```java
package ch01.sec12;

public class Calculator {

	public static void main(String[] args) {
		int x; // 변수 선언
		x = 1; // 변수에 값 저장
		int y = 2; // 선언과 저장을 동시에
		int result1 = x + y;
		int a = 3; int b = 4; // 실행문을 세미콜론으로 구분해서 한 줄로 작성 가능
		int result2 = a + b;
		System.out.println(result1);
		System.out.println(result2);
	}

}

```

## IX. 에디션 종류

자바 에디션에는 대표적으로 3가지가 있다.

해당 에디션들은 표준안, 일종의 설계도에 해당한다

- 각 에디션은 플랫폼(장치)에 따라 어떤 것으로 프로젝트를 진행할지 달라진다.

1. Java Standard Edition(Java SE)

   - 개인용

   - PC에서 실행되는 app 개발

2. Java Enterprise Edition(Java EE)

   - 회사용
   - 웹서비스를 만들 때 사용한다.

3. Java Micro Edition(Java ME)

   - 휴대용

Java SE를 사이에 두고, EE와 ME가 양쪽에 교집합으로 엮이는 구조를 띄고 있다.



## X. 자바 압축파일의 종류

- 모두 java의 -jar 옵션 `java -jar`을 통해 생성
- `jar.exe`로 해제

1. `.jar`
   - 여러 개의 **클래스 파일**을 압축한 파일
   - 압축 방식이 .zip과 똑같아서, 확장자를 바꿔도 상관없다.
   - SE 관련
2. `.war`
   - 여러 개의 웹 어플리케이션 압축 포맷 파일
3. `.ear`
   - jar + war

- eclipse library tab의 jar파일들은 미리 만들어져 제공되는 **클래스 파일**들의 압축파일이다.
  - 기존에는 rt.jar(runtime)에 다 들어 있었는데, JAVA9부터 쪼개졌다.
  - 기본 라이브러리를 API라고 부른다.
  - [API문서](https://docs.oracle.com/javase/8/docs/api/index.html) 참고
  
  - 클래스 파일들은 C:\Program Files\Java\jdk-17.0.6\lib\jrt-fs`에 존재
  - 소스 코드는 `src.zip`파일에 있음

