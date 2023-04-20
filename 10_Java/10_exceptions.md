# Exceptions

1. 예외란

   - 프로그램 실행중에 발생되는 예기치 않은 사건

   - 일반적으로 에러라고 부름

2. 예외발생의 문제점
   - main의 끝까지 가 정상종료 되지 않고, 중간에 비정상 종료됨

3. 예외처리란?

   - 비정상 종료를 예외처리를 통해 정상종료로 바꾸는 것

   - 예외가 발생된 코드를 수정하는 것이 아니다(불가능)

4. 예외 클래스

   - 제공되는 예외클래스를 사용해서 예외처리를 함

   - Object

     - Throwable

       - Error - 개발자 처리 불가

       - Exception - 개발자가 처리 가능 - **일반적으로 예외클래스의 최상위로 처리**

         - RuntimeException

           > **compile unchecked 계열**
           >
           > **원래 try - catch, throws로 예외처리 하는 게 아님!**
           >
           > **런타임 계열 에러는, 예외처리를 하지 않아도 컴파일 에러가 발생하지 않는다.**
           >
           > - 개발자가 반성을 해야 함. 
           > - **조건체크로 예외가 발생하지 않게 할 수 있기 때문**
           > - 어떤 에러가 발생할지는 알 수 없음
           > - 컴파일러가 예외처리를 하는지 관심 없음
         
           - Runtime계열 Exception들
           - ArrayIndexOutofBoundsException
           - ArithmeticException 등
           - ...
         
         - 비 Runtime계열 Exception
         
           > **compile checked 계열**
           >
           > **예외처리를 하지 않으면 컴파일 에러가 발생한다.** 
           >
           > - 조건체크로는 해결이 불가능하다.
           >
           > - **즉 예외처리가 필수적이다.**
           >
           > - 어떤 예외가 발생할 지 알 수 있다.
           
           - IOException
             - ...
           - SQLException
             - ...
           
           



## 1. 예외처리 방법

예외처리는 기본적으로 **메서드 단위로 실행**된다.



1. 예외가 발생한 곳에서 처리

   `try {...} catch (Exception e) {예외처리코드}`

   try 내부의 실행문을 진행하다가 예외가 발생하는 순간 catch문으로 넘어가고, catch문을 실행한 후 이후 문 진행
   
   

2. **예외가 발생한 곳이 아니라 위임해서 처리**

   많이 사용
   - 예외 관리를 집중해서 처리하기 위함

   문제가 발생한 곳에서 처리하지 않고,

   자기를 호출한 메서드로 위임함



**예외처리코드의 최고의 작업은 어떤 문제인지 이해하기 쉽도록 정보를 주는 작업이다.**



- 예외처리 메서드 두개
  - `error.getMessage()`
    - 기본적인 에러 정보 제공
  - `error.printStackTrace();`
    - 개발자의 디버깅을 위한 좀 더 자세한 정보 제공
    - sysout에 넣지 않고 자제척으로 사용

- 기본적인 예외처리 방법

```java
package p05;


class Test {
	public void a() {
		b();
	}
	public void b() {
		try {
			int n = 0;
			int result =  10 / n;	// 예외발생
			System.out.println("결과값 : " + result);
		} catch (ArithmeticException e) {
			System.out.println("예외처리코드: " + e.getMessage());
			// e.printStackTrace();		// 개발자가 디버깅용으로 많이 사용함.
		}
        
        /*
        // Runtime 계열은 try-catch 대신 조건문으로 처리한다
		// 즉 해당 케이스에서는 아래 방식이 더 바람직하다.
		if (n!=0) {
			int result =  10 / n;
			System.out.println("결과값 : " + result);
		}
        */
	}
    
    
}

public class ExceptionTest {

	public static void main(String[] args) {
		System.out.println("start");
		Test t = new Test();
		t.a();
		System.out.println("end-정상종료");	// main의 끝까지 가는 것이 정상종료
	}

}

```



## 2. 다형성 사용 가능

더 상위의 Exception 객체를 사용 가능하다.

다만, 이렇게 처리하는 것은 권장하지 않는다.

```java
try {			
// } catch (Exception e) {	// 다형성 적용 가능
// } catch (RuntimeException e) {
} catch (ArithmeticException e) {
    
}
```



## 3. 다중 catch

- 여러 상황의 예외를 모두 처리하기 위해 사용
- 계층구조가 낮은 Exception 클래스부터 작성한다.
  - **더 상위의 Exception 클래스가 위에 있다면, 컴파일 에러가 발생한다.**
  - instanceof에서와 비슷하지만, 에러는 나지 않는다.

```java
try {
	... // ArithmeticException 발생 가능
    ... // NullPointerException 발생 가능
} catch (ArithmeticException e) {

} catch (NullPointerException e) {
    
} catch (Exception e) { 				// 마지막에는 Exception으로 잡아준다.
    
}
```

- 예시

```java
package p06;

public class ExceptionTest {
	
	public static void main(String[] args) {
		System.out.println("start");
		try {
			// NullPointerException 발생 가능한 코드
			String n = "hello";
 			// String n = null;
			System.out.println(n.length());
			
			// ArithmeticException 발생 가능한 코드
			// System.out.println(10/2);
			System.out.println(10/0);
			
		} catch (NullPointerException e) {
			System.out.println(e);
		} catch (ArithmeticException e) {
			System.out.println(e);
		} catch (Exception e) {				// 범위가 넓은 것이 밑으로
			System.out.println(e);
		}
		System.out.println("normal end");
	}
}

```



## 4. finally

정상 실행이든, 에러이든, 반드시 마지막에 수행되어야 하는 문장이 존재할 경우 사용되는 문이다.

예시로는, DB등 외부 자원에 연결하는 문(`open()`)은 반드시 연결을 종료(`close()`)해 주어야 하기 때문에 사용한다.

사실 그냥 try - catch 아래에 주어도 되지만, 좀 더 강조하기 위해 사용한다.

- 세 가지 구조
  - try - catch - catch
  - try - catch - finally
  - try - finally
    - 예외가 발생하면, 예외처리 없이 바로 finally로 넘어감

- null의 의미
  - 아직 가리키는 곳이 없다.



## 5. throws

발생한 예외를 해당 메서드 내에서 try - catch로 처리하지 않고, 자기를 소환한 더 상위의 메서드로 던져서 저리한다.

일반적으로, 최종 main까지 던져서 처리한다.

- 런타임 에러 계열은 해당 throws 처리를 적절히 해 주지 않아도 throw 처리가 된 것처럼 작동하지만, 비런타임 계열은 그렇지 않기 때문에 처리를 철저히 해 주어야 한다!
- 물론 다형성 처리도 가능하다.
  - 권장하지는 않는다.

```java
package p01;

class Test {
	
    // 다형성 처리
	public void a() throws Exception {
		b();
	}
	
	// 자체 try - catch 처리를 하지 않고 a에게 에러를 던진다. => 다중 Throw 가능
	// 런타임 계열일때는, throws 처리를 해 주지 않아도 에러를 던진다.
	public void b() throws NullPointerException, ArithmeticException {	 
		int n = 0;
		int result = 10 / n;
		// String name = null;		
		System.out.println(name.length());
	}
	
}

public class ExceptionTest {
	public static void main(String[] args) {
		System.out.println("Start");		
		Test t = new Test();
		try {
			t.a();
		} catch (NullPointerException e) {
			System.out.println("예외처리 Null: " + e);
		} catch (ArithmeticException e) {
			System.out.println("예외처리 Aritmetic: " + e);
		} catch (Exception e) {
			System.out.println("예외처리 All: " + e);
		}
		
		System.out.println("정상종료");
	}

}

```



## 6. 명시적 예외발생

- 문법적으로 문제가 없을 때는, 시스템이 에러를 발생시키지 않는다.
- 하지만, 비즈니스 규칙에 위반되는 경우, 자체적으로 에러를 발생시켜야 하는 경우가 있다.
  - 강제적으로 예외 클래스의 객체를 생성한다.
- 비런타임계열(을 포함한 예외 객체)일 경우는 compiler checked이므로, 예외처리가 필수이다.
- 형식
  - `throw new XXXException("Exception Message");`
  - 실행 이후 비정상종료된다.

```java

// Exception Message가 e.getMessage, e.printStackTrace()에 담긴다.
if (condition)
    throw new XXXException("Exception Message");

```

- 예시

```java
package p01;

import java.util.Random;

class MyRandom {
	public void getRandom() throws MyException {
		Random r = new Random();
		int n = r.nextInt(3);
		System.out.println("값: " + n);
		
		// 비런타임계열을 포함하기 때문에, 예외처리가 필수이다. => 빨간밑줄
		// if (n==0) throw new Exception("랜덤값 0으로 인해 예외 발생");
		
		// 런타임계열(compiler unchecked)이기 때문에, 예외처리가 필수가 아니다.
		if (n==0) throw new MyException("랜덤값 0으로 인해 예외 발생");
	}
}

public class ExceptionTest2 {
	public static void main(String[] args) {
		System.out.println("start");
		MyRandom x = new MyRandom();
        
		try {
			x.getRandom();			
		} catch (MyException e) {
			System.out.println("예외처리" + e.getMessage());
		}
		
		System.out.println("end-정상종료");
	}

}

```



## 7. 사용자 정의 예외 클래스

사용자가 자체적으로 예외인 상황을 만들어야 할 경우, 즉 해당 비즈니스 규칙에 맞는 예외를 만들어야 할 경우

Exception 클래스를 상속받아, 자체적으로 정의해 사용한다.

1. extends Exception을 사용한 클래스를 작성한다. 
2. 문자열 인자를 가진 생성자를 작성한다. 
   - 예외처리시 catch블록에서 출력할 문자열을 초 기화하는 역할이다. 

3. 필요시` throw new UserException(mesg);` 코드로 강제적으로 예외를 발생시켜 사용 한다

```java
// 사용자 정의 예외 클래스 생성
package p01;

public class MyException extends Exception {
	public MyException(String message) {
		super(message);
	}
}

// 사용

package p01;

import java.util.Random;

class MyRandom {
	public void getRandom() throws MyException {
		Random r = new Random();
		int n = r.nextInt(3);
		System.out.println("값: " + n);
		
		if (n==0) throw new MyException("랜덤값 0으로 인해 예외 발생");
	}
}

public class ExceptionTest2 {
	public static void main(String[] args) {
		System.out.println("start");
		MyRandom x = new MyRandom();
        
		try {
			x.getRandom();			
		} catch (MyException e) {
			System.out.println("예외처리" + e.getMessage());
		}
		
		System.out.println("end-정상종료");
	}

}

```

