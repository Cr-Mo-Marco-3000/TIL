# Important APIs

이번 장에서 학습할 클래스들은 어플리케이션 개발시 매우 많이 유용하게 사용되는 API 이기 때문에 잘 숙지하도록 한다.

## I. 문자열

문자열은 참조 데이터형으로, `""`를 이용해서 리터럴(값)을 표현한다.

문자열을 생성하는 방법은 다음과 같다.

### 1. String class

문자열을 생성하는 가장 대표적인 두 가지 방법

1. `String str = new String("Hello");`
2. `String str2 = "Hello";`

2가지 방법은 비슷해 보이지만 차이점이 있다.

1. 1번은 동일한 문자열이 존재해도 새로운 객체를 생성한 후 할당한다.
   - 또한, new 키워드를 이용한 문자열은 heap 메모리에 저장된다.
   - 따라서 ==으로 비교했을 때는, 주소값을 비교하므로 false가 나오게 된다.

2. 2번은 동일한 문자열이 존재한다면 새로 생성하지 않고 재사용한다.
   - literal pool이라는 특별한 메모리에 저장된다.

따라서, 문자열의 값을 비교할 때는 equals() 메서드를 반드시 사용해야 한다.

String 클래스의 특징은, 한 번 생성된 문자열은 변경되지 않는다는 '불변성' 특징이 있다.

즉 다양한 메서드로 가공했을 때, 새로운 변경된 문자열이 생성된다.

따라서 문자열이 자주 변경될 경우에는 String 클래스 대신에  StringBuffer 또는 StringBuilder 클래스를 사용하는 것을 권장한다.

```java
package p03;

public class StringTest {

	public static void main(String[] args) {
		String str = new String("Hello");
		String str2 = new String("Hello");
		String str3 = "Hello";
		String str4 = "Hello";
		
		// 위치값 비교 => 주소를 비교하기 때문에 false true
		System.out.println(str == str2);
		System.out.println(str3 == str4);
		
		// 값 비교 => 값 비교하기 때문에 둘 다 true
		System.out.println(str.equals(str2));
		System.out.println(str3.equals(str4));		

	}

}

```

다음은 String class의 대표적인 메서드들이다.

![image-20230417211157495](C:\Users\bizyoung93\Desktop\TIL\10_Java\09_useful_apis.assets\image-20230417211157495.png)

- 참고: 길이 비교
  - String class
    - `.length()`
  - Array
    - `.length`
  - Collection
    - `.size()`



### 2. StringBuffer(StringBuilder)

문자열 연산시 매우 비효율적으로 메모리를 사용하게 된다.

문자열을 이용한 연산작업이 많은 경우에는 StringBuffer 또는 StringBuilder를 사용할 수 있으며, 두 개의 클래스의 사용법은 거의 유사하고 차이점은 StringBuffer는 thread-safe 하지만 무거운 특징을 가지며 StringBuilder는 thread-unsafe하지만 성능이 좋은 특징이 있다.

생성 방법은 다음과 같으며, 따라서 동일한 문자열이 존재해도 매번 생성된다.

`StringBuffer str = new StringBuffer("Hello")`

StringBuffer 클래스의 대표적인 메서드는 다음과 같다.

![image-20230417211907791](C:\Users\bizyoung93\Desktop\TIL\10_Java\09_useful_apis.assets\image-20230417211907791.png)

참고: StringBuffer의 append 메서드와 String의 concat 메서드, += 연산자의 속도비교를 해 보면, `append > concat > +=` 이다.

```java
package p03;

public class StringBufferTest {
	public static void main(String[] args) {
		StringBuffer mySB = new StringBuffer("Hello");
		mySB.append(" World");
		mySB.toString();
		System.out.println(mySB);			// Hello World
	}
}

```

### 3. toString()

Wrapper 클래스의 toString 메서드는 문자열이 아닌 기본형 데이터를 문자열로 바꾸는 메서드로서, String.valueOf(값) 메서드와 동일한 기능을 한다.

각각의 메서드는 static 메서드이기 때문에 클래스명으로 접근한다.

```java
Integer.toString();
Character.toString();
Float.toString();
Boolean.toString();
```



## II. Wrapper Class

원시 타입의 값을 갖는 객체를 생성할 수 있다.

이런 객체를 wrapper class(포장 객체)라고 한다.

포장 객체를 생성하기 위한 클래스는 `java.lang` 패키지에 포함되어 있는데, char 타입과 int 타입이 각각 Character와 Integer인걸 제외하고 기본 타입의 첫 문자를 대문자로 바꾼 이름을 가지고 있다.

포장 객체는 포장하고 있는 기본 타입의 값을 변경할 수 없고, 단지 객체로 생성하는 데 목적이 있다.

이런 객체가 필요한 이유는 컬렉션 객체 때문이다.

**컬렉션 객체는 기본 타입의 값은 저장할 수 없고, 객체만 저장할 수 있다.**



### 1. 박싱과 언박싱

- jdk 1.5부터 지원

- 박싱
  - 기본 타입의 값 -> 포장 객체
  - `Integer myInt = 10;`

- 언박싱
  - 포장 객체 -> 기본 타입의 값
  - `Integer myInt2 = new Integer(10);`
  - `int myInt3 = myInt2`

- 다른 예시
  - `Object [] obj = { 10,  "홍길동", 3.14 }`