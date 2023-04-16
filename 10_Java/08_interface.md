# 인터페이스와 추상클래스, 중첩 클래스

**인터페이스와 추상 클래스를 통해서 하위 클래스들에게 부모의 메 서드를 반드시 사용하도록 강제할 수 있다.**

인터페이스란 용어자체가 ‘서로 다른 장치를 이어주는 접속장치’를 의미

강제를 함으로써 통일성 및 일관성이 지켜질 수  있으며 결국에는 재사용성 및 유지보수가 향상되고 관리하기도 쉬워진다.

마찬가지로 메서드도 통일된 하나의 메서드로 처리하는 것이 관리차원에서 효율적이다.



## 1. 추상 클래스(abstract class)

블록이 없는 메서드를 포함할 수 있는 클래스를 추상클래스라고 한다.

근데 인터페이스를 더 많이 쓴다.

```java
public abstract class className {
    // 인스턴스 변수
    // 생성자
    // 일반 메서드
    // 추상 메서드
}
```

블록이 없는 메서드를 추상 메서드(abstract method)라고 하며 abstract 키워드를 사용하여 다음과 같이 표현한다.

`public abstract 리턴타입 메서드명([파라미터]);`

### 0. Concrete Class

구상 클래스는, **추상 클래스의 반대의 의미**로, 모든 것이 정해진 클래스를 의미한다.



### 1. 특징

- 미완성 클래스이다.
- 구성요소는 다음과 같고, 반드시 **추상 메서드를 포함할 필요가 없다.**
  - 인스턴스 변수
  - 일반 메서드
  - 생성자
  - **추상 메서드**

- 추상 메서드를 포함할 수 있기 때문에 **객체 생성이 불가능**하다

- **인터페이스와는 달리 다양한 접근 지정자를 사용 가능하다.**

- 불완전한 추상 클래스를 사용하기 위해서는 일반 클래스를 이용한다. 
  - 상속을 이용하고 다형성 적용도 가능하다. 
- 주의할 점은, **상위 추상 클래스가 추상 메서드를 포함**하면 하위 클래스에서 **반드시 추상 클래스의 추상 메서드를 재정의 해야 된다.** 
  - 만약 재정의 하지 않으면 컴파일 에러가 발생되기 때문에 **강제성이 있다.** 
- 추상 클래스도 클래스이기 때문에 단일상속만 지원된다.
- 추상 클래스와 추상 메서드의 UML표기법은 이탤릭체로 표현한다.
- 객체 생성은 불가능하지만 선언된 변수의 데이터형으로 사용할 수 있다.
- **쓰는 목적**
  - **강제성 및 통일성을 제공한다. 상속의 장점을 가져가면서 하위 클래스에게 특정 메서드만 강제할 수 있다.**
- 일반 클래스와 마찬가지로 파일이 `.java`로 저장된다


```java
package abstractclass;

public class Main {
	public static void main(String[] args) {
		// MyClass mine = new MyClass();				//추상 클래스는 반드시 상속해서 사용해야 한다.
		MyClass mine =  new MyClassChild("김현영", 31); 	// 단, 이렇게 다형성 활용은 가능하다.
		mine.getName();
		
		
	}
}

abstract class MyClass {					// 추상 클래스 생성
	String name;
	int age;
	
	// constructor
	public MyClass() {}
	public MyClass (String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public void normalMethod () {
		System.out.println("일반 메서드 실행");
	}
	
	// abstract method
	public abstract void getName (); // 추상 메서드 생성

}

class MyClassChild extends MyClass {
	
	// constructor
	public MyClassChild(String name, int age) {
		super(name, age);
	}
	
	// 추상 클래스를 상속받았을 때는, 해당 추상 클래스의 추상 메서드를 반드시 오버라이딩해야 한다!
	@Override
	public void getName() {
		System.out.println(name);
	};
}




```



## II. 인터페이스

추상 클래스와 비슷한 용도로 인터페이스를 사용할 수 있다.

다음과 같이 interface 키워드를 사용하고, 4가지 구성요소를 포함할 수 있다.

`java.util.function` api에서 interface를 확인할 수 있다.

```java
public interface interfaceName {
    // public static final로 지정한 상수
    // public abstract 지정자를 이용한 추상메서드
    // public default 지정자를 이용한 일반메서드
    // public static 지정자를 이용한 일반메서드
}
```

### 1. 특징

- 일반 클래스, 추상 클래스와 마찬가지로 파일이 `.java`로 저장된다.
- **인터페이스 자체는 public, 혹은 (default)의 접근 지정자를 가질 수 있다.**
  - 일반 클래스도 동일하다.

- **멤버는 위의 네 가지와 중첩 인터페이스가 가능하며, 접근 지정자는 public만 가능하다.**
  - 상수의 경우 일반 클래스, 추상클래스에서는 public이 필수까지는 아니지만, 인터페이스에서는 필수이다.
  - **만약 접근 지정자를 명시해주지 않는다면, 다른 경우(`(default)`)와는 다르게 public으로 지정된다**
    - **다른 접근 지정자는 에러가 발생한다.**

- 구성요소는 상수 및 추상 메서드, default 메서드, static 메서드만 가질 수 있다. 
  - 상수는  **public static final** 지정자를 사용한다.
    - **작성하지 않아도, 변수를 작성하면 자동으로 지정이 된다.**
  - 추상 메서드(abstract method)는 **public abstract** 지정자를 사용한다. 
    - 추상 클래스와 다르게 인터페이스의 추상 메서드는 public 뿐만 아니라 **abstract 키워드를 생략** 할 수 있으나 지정하는 것을 권장한다.
    - **추상 메서드 작성 역시 선택사항이다**
- 또한 일반 클래스의 일반 메서드 기능과 동일한 **default 메서드와, static 메서드 기능과 동일한 static 메서드는 블록({})을 포함**한다.
  - `public default`와, `public static` 키워드를 사용한다.
  - default 메서드에는 **default 키워드가 반드시 필요**하다.
    - 왜 일반 메서드에 static keyword를 붙여주냐면, 인터페이스에서 키워드가 없는 메서드는 추상 메서드로 정의되기 때문이다.
    - 위에서 abstract를 생략할 수 있다고 서술한 것을 다시 확인!
- 추상 메서드를 가지고 있기 때문에 **객체생성이 불가능**하다. 추상클래스와 마찬가지로 인터페이스를 사용하기 위해서는 **일반 클래스를 이용**한다. 
- 인터페이스끼리는 상속, 인터페이스와 클래스 사이는 구현이라고 부른다.
  - 클래스에 인터페이스를 넘겨줄 때는, 상속(extends)과 비슷한 **구현 (implement)을 이용**하고 다형성 적용도 가능하다. 
    - 구현할 때는 implements 키워드를 사용한다.
  - **인터페이스끼리 상속할 때**는, 클래스끼리의 상속과 마찬가지로 **extends를 사용**한다.
    - 클래스와 다르게 다중 상속이 된다.
- 주의할 점은 **구현한 하위 클래스**에서 반드시 **인터페이스의 추상 메서드를 재정의** 해야 된다.
  - 다만, 상속받은 **다른 인터페이스에서**는 **추상 메서드를 재정의할 필요가 없다.**
    - 해도 된다.
  - 정리하자면, 다중 상속이든, 단일 상속이든 인터페이스들 사이에서는 추상 메서드를 재정의할 필요가 없고, 해당 인터페이스(들)을 **구현한 클래스에서는 위에서 만들어준 추상 메서드(들)을 반드시 재정의해야 한다.**
- **다중 상속, 다중 구현이 가능하다.**
  - 클래스는 단일 상속만 지원되지만 인터페이스는 **다중 구현을 지원**한다. 
- 구현은 ‘준상속’ 관계이기 때문에 계층 구조적으로 인터페이스가 구현 클래스보다 큰 타입이다. **따라서 다형성 적용이 가능하다.**
  - 즉, 인터페이스 이름의 변수 데이터형에 구현 클래스를 저장할 수 있다.
- 인터페이스는 객체 생성은 불가능하지만 변수의 데이터형으로 사용할 수 있다.
  - 즉, 다형성 적용이 가능하다는 다른 말이다.
- **상속과 마찬가지로 강제성 및 통일성을 제공한다.**
- UML
  - 인터페이스의 UML표기법은 `<<interface>>` 으로 표현한다.
  - 추상 메서드의 UML표기법은 **이탤릭체로 표현**한다.
  - 구현을 UML 표기법으로  **점선의 빈 삼각형**을 이용한다.
  - 단, 같은 인터페이스 사이의 상속은 실선의 빈 삼각형을 사용한다.
  - 상속 및 구현은, 모두 부모로 향하는 삼각형으로 표현한다.

```java
package day0414;


// 인터페이스 정의
interface Flyer {							// public 또는 (default)만 가능하다
	public static final String transport = "비행기"; 	// 상수는 public static final을 사용하여 작성	=> public static으로 외부에서 객체생성 없이 접근 가능, final로 값 변경 불가능
	
	int airNum = 1;									// 명시하지 않아도 인터페이스의 상수는 자동으로 public static final이 붙는다.
	
	public abstract void takeOff();					// 추상 메서드	=> abstract는 인터페이스에서는 없어도 되지만 있는 것을 권장
	
	public default void fly() {						// default를 붙여주지 않으면 추상 메서드 취급을 당한다.
		System.out.println("fly");
	}
	public static void land() {						// static 메서드이다.
		System.out.println("land");
	}
}

// 인터페이스 구현
class Bird implements Flyer{
	
	@Override
	public void takeOff() {
		System.out.println("1000km");				// 추상 메서드 재정의
	};
	
}


public class Ex07_2 {

	public static void main(String[] args) {
		Bird fly = new Bird();
		System.out.println(Flyer.transport);		// 인터페이스 상수 접근
		fly.takeOff();								// 인터페이스를 상속받은 클래스 메서드 접근
		fly.fly();									// 부모의 메서드에 접근
		Flyer.land();								// static 메서드 접근
	}

}

```

- 다중 상속

```java
interface A {}
interface B {}

interface C extends A, B{}	// 다중 상속

class D implements A, B{}	// 다중 구현

class F implements C{}
```

- 추상 클래스와의 비교

![image-20230414103957664](C:\Users\bizyoung93\Desktop\TIL\10_Java\08_interface.assets\image-20230414103957664.png)

## 2. 사용 이유

1. 하위 클래스에서 특정 메서드를 강제할 목적

2. **클래스들간의 의존성 감소**

   1. loosely coupling

   2. decoupling

### 클래스들 간의 의존성 감소 예시

- 일반 클래스로 작성했을 때, 여러 파일들을 돌아다니며 작성해주어야 함

```java
// DB 사용 예시
// MySQL DB 연동 클래스
package p02;

// MySQL DB 연동 클래스
public class MySQLDao {
	
	public void connectMySQL() {
		System.out.println("OracleDAO.connectMySQL()");
	}
	
}

// Oracle DB 연동 클래스
package p02;

// Oracle 연동 클래스
public class OracleDao {
	
	public void connectOracle() {
		System.out.println("OracleDAO.connectMySQL()");
	}
	
}


// DBservice.java
package p02;

public class DBservice {
	
	OracleDao dao;
	
	public void setDB(OracleDao dao) {
		this.dao = dao;
	}
	
	public void connectService() {
		dao.connectOracle();
	}
}

// TestMain.java
package p02;

public class TestMain {

	public static void main(String[] args) {
		
		DBservice service = new DBservice();
		
		OracleDao dao = new OracleDao();
		
		service.setDB(dao);
	}

}

```

- 인터페이스로 만들었을 때, TestMain만 바꾸어주면 됨

```java
// DBDao.java
// interface

package p03;

public interface DBDao {
	public abstract void connectDB();
	
}

// DBService
package p03;

public class DBservice {
	
	DBDao dao;
	
	public void setDB(DBDao dao) {
		this.dao = dao;
	}
	
	public void connectService() {
		dao.connectDB();
	}
}

// MySQL
package p03;

public class MySQLDao implements DBDao {
	
	@Override
	public void connectDB() {
		System.out.println("DBDAO.connectMySQL()");
	}
}

// Oracle

package p03;

public class OracleDao implements DBDao {
	
	@Override
	public void connectDB() {
		System.out.println("DBDAO.connectMySQL()");
	}
	
}

// Main

package p03;

public class TestMain {

	public static void main(String[] args) {
		
		DBservice service = new DBservice();
		
		// MySQLDao dao = new MySQLDao();
		OracleDao dao = new OracleDao(); // 갈아끼울 때 얘만 하면 됨
		
		service.setDB(dao);
	}

}

```



## III. 중첩 클래스(nested class)

중첩 클래스란 클래스안에 또 다른 클래스가 정의되는 것을 의미한다. 

일반적인 클래스는  독립적으로 정의하고 사용되지만 중첩 클래스는 멤버형태로 클래스를 포함할 수 있다.

중첩되는 클래스의 개수는 제한이 없다.

어떤 클래스가 특정 클래스에서만 사용된다고 가정하면, 이를 독립적인 클래스로 작성하기보다는 중첩 클래스로 작성하는 것이 관리하기 쉬워진다.

대표적인 형태가 GUI 이벤트를 처리하는 경우이다. GUI 화면을 구성하는 클래스가  있고 화면에서 발생되는 이벤트를 처리하는 클래스가 있는 경우에 이벤트를 처리하는 클래 스는 GUI 클래스가 없으면 불필요한 클래스이다. 따라서 독립적인 클래스로 정의하지 않고  GUI 클래스의 중첩 클래스형태로 작성하면 화면 구성부분과 이벤트 처리부분이 클래스형태 로 분리되었지만 같이 사용되어 관리 면에서 효율적이다. 또한 은닉화(Encapsulation)을 통 해 코드의 복잡성을 감소시킬 수 있고 코드의 가독성 및 유지보수성을 향상 시킬 수 있는  장점이 있다.

- 중첩 클래스를 포함하는 바깥 클래스를 Outer 클래스라고 하며, 내부에 포함된 클래스를 중첩클래스 또는 Inner 클래스라고 한다.

```java
public class Outer{
    
    class Inner{
        
    } // end Inner
} // end Outer
```

### 1. Inner 클래스 특징

1. Inner 클래스는 Outer 클래스의 멤버를 마치 자신의 멤버처럼 사용할 수 있다. 
2. Outer 클래스 멤버의 접근 지정자가 **private일지라도 접근 할 수 있다.**
3. Inner 클래스는 static 선언이 가능하다. 
   - Inner 클래스만 static 클래스로 설정 할 수 있다. 
4. (JAVA 16 이전) Inner 클래스 안에는 **static 변수를 선언할 수 없다.**
   - **단, static으로 설정된 Inner class에는 static 변수를 선언 가능하다.**
   - 그런데, 내부 클래스가 static이면, 반대로 Outer 클래스의 멤버에 접근이 불가능하다.
     - 생성 시점이 내부가 먼저라서 그렇다.
   - 하지만 **JAVA 16부터는, Inner 클래스 내부에 static 변수를 선언할 수 있다.**
5. Inner 클래스의 접근은 반드시 Outer 클래스를 통해서 접근해야 한다. 
   - 단, static Inner 클래스는 직접 접근이 가능하다.
6. 소스 파일을 컴파일을 하면 Inner 클래스는 `Outer$Inner.class` 형식으로 클래스 파일이 생성된다.
7. 정의되는 위치에 따라서 4가지 형태의 Inner 클래스가 제공된다.



### 2. Inner 클래스 종류

![image-20230414110147996](C:\Users\bizyoung93\Desktop\TIL\10_Java\08_interface.assets\image-20230414110147996.png)

#### 1) member Inner class

객체를 생성해야만 사용할 수 있는, Outer 클래스의 변수, 메서드와 같은 수준으로 선언된 **static 키워드를 사용하지 않은 Inner 클래스를 의미**한다.

Inner class를 사용하기 위해서는 **반드시 Outer 클래스를 먼저 객체 생성해야 한다.**

```java
// 선언 방법
public class Outer {
    // Outer class의 멤버 형태로 선언한다.
    class Inner {
        
    } // end Inner
} // end Outer

public class Main {
    public static void main(String[] args) {
        
        Outer myOuter = new Outer();	// Outer 객체생성 필수
        Outer.Inner myInner = myOuter.new Inner();	// Outer.Inner 변수에, myOuter를 통해 생성한 객체를 넣는다.
    }
}
```

- 사용예시

```java
package p04;


class Outer {
	int a = 10;
	private int b = 20;
	static int c = 30;
	
	class Inner {
		int d = 40;
		// static int f = 50; 버전에 따라, static 사용 불가
		
		public void printInner() {
			System.out.println(a);
			System.out.println(b);		// private에 접근 가능
			System.out.println(c);
			System.out.println(d);
		}
	}
	
	// 내부에서 Inner class에 접근할 수 있다.
	public void info() {
		Inner myInner = new Inner();
		myInner.printInner();
	}
}

public class Main {

	public static void main(String[] args) {
		Outer myOuter = new Outer();
		myOuter.info();					// 내부접근을 통한 출력
		
		Outer.Inner myInner = myOuter.new Inner();
		myInner.printInner();			// 외부접근을 통한 출력
	}

}

```



#### 2) local Inner class

- 메서드 안에서 정의하고 사용하는 클래스이다.

- 잘 안쓴다.

```java
public class Outer {
    
    public void outerMethod () {
        class Inner {				// outer의 메서드 내에서 Inner 정의
            
        }
        Inner inner = new Inner()	// 생성
    }
}
```



#### 3) static Inner class

static이 붙은 Inner class

일반적으로 클래스에는 static이 붙을 수 없지만, Inner class에서는 가능하다

일반 Inner 클래스에는 static 변수를 포함할 수 없지만 static Inner 클래스로 정의하면 가능하다. 

단, static Inner class에서는 static 변수를 제외한 Outer 클래스의 멤버에 접근할 수 없다.

또한 **Outer 클래스를 생성하지 않아도 Inner 클래스에 직접 접근**할 수 있다.

프로그램이 실행될 때 만들어진다.

```java
public class Outer {
    static class Inner {
        
    }
}
```

- 예시

```java
package p04;


class Outer {
	int a = 10;
	private int b = 20;
	static int c = 30;
	
	static class Inner {
		static int d = 40;
		
		public void printInner() {
			// System.out.println(a);  // static 선언되지 않은 외부 변수에 접근 불가능
			// System.out.println(b);		
			System.out.println(c);
			System.out.println(d);
		}
	}
	
}

public class Main {

	public static void main(String[] args) {
		// 멤버 Inner 클래스 사용시, 아우터 인스턴스를 반드시 만들어 주어야 한다.
		// Outer myOuter = new Outer();
		// Outer.Inner = myOuter.new Inner();
		
		// static Inner class 사용시, Outer class를 만들어주지 않고 Inner class 객체를 바로 만들어 사용 가능하다.
		Outer.Inner myInner = new Outer.Inner();
		myInner.printInner();
        
        // static Inner class 사용시, Inner class에 직접 접근이 가능하다
		System.out.println(Outer.Inner.d); 
	}

}

```



#### 4) 익명 클래스

anonymous Inner class는 Local Inner 클래스의 변형된 형태이다.

직접 클래스명을 지정하지 않으며 단지 인스턴스의 생성과 메서드 선언만을 정의한다.

일반적으로 **인터페이스 또는 추상클래스를 구현하는 클래스**로 자주 사용된다.

익명클래스를 함수형 프로그래밍(Functional Programming) 기반으로 확장 표현한 것이 람다(lambda)식이다.

```java
// 인터페이스 혹은 추상클래스 정의
public interface InterfaceName {
    public abstract void methodName();
}

// 익명 클래스
InterfaceName myInterface = new InterfaceName () {
    @Override
    public abstract void methodName() {}
    
};	// 세미콜론 필수!

// 익명 클래스의 메서드 사용
myInterface.methodName();


```

- 예시

```java
package p04;

interface Flyer {
	
	public abstract void a();
}

class Bird implements Flyer {
	
	@Override
	public void a() {
		System.out.println("Bird.a()");
	}
}

public class TestMain {
	public static void main(String[] args) {
		
		// 1. 인터페이스를 클래스 선언 후 사용
		Flyer myFlyer = new Bird();
		myFlyer.a();	
		
		
		// 2. 익명 클래스 사용
		// new까지만 입력 후 ctrl + space
		Flyer f2 = new Flyer() {
			@Override
			public void a() {
				System.out.println("Anonymous.a()");
			}
		};
		f2.a();
	}

}

```



##### 4-1) 람다식

함수형 프로그래밍 기반의 람다 표현식

**기능에 집중한 표현식이다.**

익명 클래스를 람다식으로 만든다.

단 이때, 해당 인터페이스 내부에 **단 하나의 추상 메서드만 있어야한다.**

- **여러 개의 추상 메서드가 있으면 익명 클래스까지 밖에 못한다.**
- 일반 메서드나 상수, static 메서드는 여러 개 있어도 상관없다.

- 인터페이스에 `@FunctionalInterface`를 주면, **인터페이스가 단 하나의 추상 메서드를 가지도록 강제할 수 있다.**

형태는 다음과 같다.

`Interface variable = (int a, int b) -> {...}`

실행은 `variable.method();`로 한다.

parameter의 자료형을 생략해 (a, b)로 작성 가능하며,

return이 있는 추상 메서드의 경우, 블록에 return만 작성하거나,

return이 없는 추상 메서드의 경우 실행문이 단 한줄이라면 {}도 생략 가능하다.

또한, 매개변수가 하나라면, ()도 생략 가능하다.

따라서, 가장 축약된 형태의 람다식은 다음과 같다.

`Interface variable = n -> ...`

```java
package p04;

// 인터페이스 메서드 1 => no params, no return
@FunctionalInterface
interface Flyer {
	public abstract void a();
	// public abstract void b(); // @FunctionalInterface => 추상 메서드 여러개는 에러가 난다
								 // 람다식 사용 시, 해당 어노테이션이 없어도 에러는 나지 않지만 붙여주는 것이 관례이다.
}

// 인터페이스 메서드 2 => params, no return
@FunctionalInterface
interface Flyer2 {
	public abstract void b(int n, int n2);

}

// 인터페이스 메서드 2-2 => 인자가 하나일 때
@FunctionalInterface
interface Flyer2_2 {
	public abstract void b(int n);
}

//인터페이스 메서드 3 => no params, return
@FunctionalInterface
interface Flyer3 {
	public abstract int c();
}

//인터페이스 메서드 4 => params, return
@FunctionalInterface
interface Flyer4 {
	public abstract int d(int n, int n2);

}


public class TestMain {
	
	public static void main(String[] args) {
		
		// 익명 클래스 사용
		Flyer f1 = new Flyer() {
			@Override
			public void a() {
				System.out.println("Flyer.a()");
			}
		};
		
		f1.a();
		
		// 인터페이스를, 익명클래스조차 만들지 않고 사용
		// 람다 표현식(lambda expression, arrow expression)
		// 자바스크립트: =>, 자바: ->
		Flyer l1 = () -> {
			System.out.println("Flyer.a()");
		};
		l1.a();
		
		// 축약된 람다 표현식
		// 실행문이나 return이 한 줄일 때는, {}가 없어도 된다.
		Flyer ll1 = () -> System.out.println("Flyer.a()");
		l1.a();
		
		
		// 두번째 형태의 익명 클래스
		Flyer2 f2 = new Flyer2 () {
			@Override
			public void b (int n, int n2) {
				System.out.println("n: " + n + " || n2: " + n2);
			}
		};
		f2.b(10, 20);
		
		// 두번째 형태의 람다 표현식
		Flyer2 l2 = (int n, int n2) -> {
			System.out.println("n: " + n + " || n2: " + n2);
		};
		l2.b(10, 20);
		
		Flyer2 ll2 = (n, n2) -> System.out.println("n: " + n + " || n2: " + n2);
		ll2.b(10, 20);
		
		// 인자가 하나일 때는, 더 축약 가능하다
		Flyer2_2 lll2 = n -> System.out.println("n: " + n);
		lll2.b(1);
		
		// 세번째 형태의 익명 클래스
		Flyer3 f3 = new Flyer3 () {
			@Override
			public int c () {
				return 100;
			}
		};
		
		System.out.println(f3.c());
		
		// 
		Flyer3 l3 = () -> {
			return 100;
		};
		
		System.out.println(l3.c());
		
		// 람다표현식 3 => 리턴만 있을때는, 바로 리턴을 쓸 수 있다.
		Flyer3 ll3 = () -> 100;
		System.out.println(ll3.c());
		
		
		// 네번째 형태의 익명함수
		Flyer4 f4 = new Flyer4() {
			@Override
			public int d (int n, int n2) {
				return n + n2;
			}
		};
		
		Flyer4 l4 = (int n, int n2) -> {
			return n + n2;
		};
		
		Flyer4 ll4 = (n, n2) -> n + n2;
		
		System.out.println(l4.d(10, 20));
		
		System.out.println(ll4.d(10, 20));
	}
	

}

```

