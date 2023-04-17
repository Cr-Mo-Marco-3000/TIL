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

       - Exception - 개발자가 처리 가능 - 일반적으로 예외클래스의 최상위로 처리

         - RuntimeException

           > **compile unchecked 계열**
           >
           > **원래 try - catch, throws로 예외처리 하는 게 아님!**
           >
           > **런타임 계열 에러는, 예외처리를 하지 않아도 컴파일 에러가 발생하지 않는다.**
           >
           > - 개발자가 반성을 해야 함. 
           > - 조건체크로 예외가 발생하지 않게 할 수 있기 때문
           > - 어떤 에러가 발생할지는 알 수 없음

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
           > - 어떤 예외가 발생할 지 알 수 있다.

           - IOException
             - ...
           - SQLException
             - ...

           



## 1. 예외처리 방법

1. 예외가 발생한 곳에서 처리

   `try {...} catch (Exception e) {...}`

   try 내부의 실행문을 진행하다가 예외가 발생하는 순간 catch문으로 넘어가고, catch문을 실행한 후 이후 문 진행



2. **예외가 발생한 곳이 아니라 위임해서 처리**

   - 많이 사용
     - 예외 관리를 집중해서 처리하기 위함

   문제가 발생한 곳에서 처리하지 않고,

   자기를 호출한 메서드로 위임함

   `b() throws XXXException {}`

**예외처리코드의 최고의 작업은 어떤 문제인지 이해하기 쉽도록 정보를 주는 작업이다.**



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



