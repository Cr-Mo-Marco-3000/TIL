# Class Relationship

자바에서 클래스들은 여러 가지 관계를 가진다.

## I. 클래스들간의 관계

### 1. has a 관계

한 객체와 다른 객체가 포함관계인 경우를 의미한다.

예를 들어 자동차 has a 엔진, 자동차 has a 바퀴등의 관계가 있다.

whole-part 관계 라고도 한다.

has a 관계에는 다음과 같은 두 가지 관계로 나눌 수 있다.

#### 1. 집합관계(Aggregation Relationship)

whole과 part간의 lifecycle이 다른 경우에 해당된다.

예를 들어, `자동차 has a 라디오` 관계의 경우, 

자동차 객체가 라디오 객체를 포함하고 있지만 라디오 객체가 없어도 자동차 객체는 존재할 수 있다.

UML로 표현한 집합관계이다.

![image-20230411101514834](C:\Users\bizyoung93\Desktop\TIL\10_Java\07_class_relationship.assets\image-20230411101514834.png)

#### 2. 구성관계(Composition Relationship)

whole과 part간의 lifecycle이 같으 경우에 해당된다.

예를 들어, `자동차 has a 엔진` 관계의 경우, 엔진 객체가 없는 자동차 객체는 존재할 수 없다.

UML로 표현한 구성관계이다.

![image-20230411101632077](C:\Users\bizyoung93\Desktop\TIL\10_Java\07_class_relationship.assets\image-20230411101632077.png)



#### 3. 자바코드를 사용한 관계 표현

**Car 클래스 내에 인스턴스로 Engine 클래스를 선언**함으로써 has a 관계를 표현할 수 있다.

일반적으로 가장 많이 사용되는 관계이다.

```java
class Car {
    Engine engine;
    
    public Car(){
        this.engine = new Engine();
    }
}

class Engine {
    
}
```



### 2. Is a 관계

비슷한 속성 및 동작을 가진 객체들 간의 관계이다. 

예를 들어 대학생 객체, 고등학생 객체, 중학생 객체, 초등학생 객체들은 모두 공통된 개념의 학생 객체들이다. 개발자, 부장, 과장, 엔지니어, 비서 등은 모두 공통된 개념의 직원 객체들이다. 

이렇게 각각의 객체와 공통된 객체간의 관계를 살펴보면 다음과 같이 is a 관계가 성림된다. 

`대학원 is a 학생`

`개발자 is a 직원`

비슷한 개념들의 객체들은 공통된 속성 및 동작을 가지고 있기 때문에, 이를 추출해서 상위 개념의 객체를 생성하고, 하위 개체들은 이를 상속받아서 사용할 수 있다.

정리하면 is a 관계가 성립되는 객체들은 자바의 상속(Inheritance)기법을 적용 하여 객체지향 프로그래밍 개발시 얻을 수 있는 다양한 장점들을 사용할 수 있도록 코드를  구성하는 것이다.



## II. 상속(Inheritance)

객체들 간에 is a 관계가 성립되면 자바의 상속기법을 적용시킬 수 있다.

### 1. 특징

자바 상속의 특징은 다음과 같다.

1. 객체 간에 is a 관계가 성립되어야 한다.

2. 부모클래스의 멤버(인스턴스 변수, 클래스 변수, 메서드 등)를 자식클래스가 **선언 없이 사용 가능**하다. 
   - 단, 부모 멤버중에서 **private로 지정**한 멤버와 **생성자**는 **상속이 불가능**하다.  
   - 자바는 **단일 상속 (Single Inheritance) 만 지원**한다. 
     - 즉, 하나의 자식 클래스는 단 하나의 부모 클래스만 가질 수 있다.
     - 부모 클래스는 여러 개의 자식 클래스를 갖는 것이 가능하다.
3. UML 표기법으로 **실선**을 이용한 빈 삼각형 화살표 을 이용한다.
4. 상속을 자바코드에서는 extends 키워드로 표현한다.
5. API 및 사용자가 만든 클래스들은 모두 상속 관계인 계층구조로 되어있다. 
   - **가장 상위에  있는 클래스는 java.lang.Object 클래스이며 최상위 클래스라고 부른다.**
   - **따라서 모든 클래스는 Object 클래스를 자연스럽게 상속받는다.**

![image-20230411102716182](C:\Users\bizyoung93\Desktop\TIL\10_Java\07_class_relationship.assets\image-20230411102716182.png)

- Employee는 부모 클래스, Manager와 Engineer는 자식 클래스이다.
- 자식 클래스는, 부모 클래스의 subClass라고 표현한다.



### 2. 형식과 주의점

- **반드시 알아두어야 할 상속과 생성자 특징 두가지**

  1. 부모 클래스의 생성자(메서드)와 private 지정된 멤버는 자식 클래스에게 상속되지 않는다.

  2. 자식 클래스를 객체 생성할 때는 자동으로 부모 클래스를 먼저 객체 생성한 후 자신의 클래스가 생성된다.
     - 부모가 먼저 생성되어야 부모가 가지고 있는 멤버를 자신이 사용할 수 있기 때문이다.

- 형식
  - `public class 자식클래스 extends 부모클래스 {}`



- 주의할 점

  - 기본적으로, **자식 클래스의 생성자 첫줄**에서는 **부모 클래스 생성자**를 반드시 호출해야 한다.

    - 부모 클래스를 먼저 생성하기 위해서이다.

    - 호출 방법은 생성자 오버로딩할 때 `this(args)` 키워드를 사용하듯이 `super(args)` 키워드를 사용한다.

  - 만약 super 키워드를 명시적으로 작성해주지 **않았을 경우**, 부모의 **기본 생성자**를 자식의 생성자 첫줄에서 **암묵적으로 실행**하게 된다.

  - 따라서, super 키워드를 사용하지 않았을 때는 부모 클래스에는 기본생성자가 반드시 존재해야 한다!
    - 자식 클래스에서 super 키워드를 쓰지 **않았고** 부모 클래스에 **다른 오버로딩 생성자를 작성**했을 때는, 부모 클래스에서 기본 생성자는 사라지므로 명시적으로 기본 생성자를 표시해주어야 한다.

#### 예시 1: 부모 클래스에 기본 생성자가 필수인 경우

```java
package my_employee;

public class Inheritance {

	public static void main(String[] args) {
		Manager mng = new Manager("김현영", 20000000, "개발");
		Employee emp  = new Employee("이팔팔", 10000000);
		System.out.println(emp.getEmployee());
		System.out.println(mng.getManager());
		
	}

}

class Employee {
	String name;
	int salary;
	
	public Employee () {} 						// 아래의 생성자 때문에 기본 생성자가 사라진다.
	
	public Employee (String name, int salary) {	// 얘가 없으면 기본 생성자가 존재하기 때문에 위 코드의 정의가 필요 없다.
		this.name = name;
		this.salary = salary;
	}
	
	public String getEmployee() {
		return this.name + "'s 월급: " + salary;
	}

}

class Manager extends Employee {
	
	String department;
	
	public String getManager () {
		return this.name + "'s 월급: " + salary + ", 부서: " + department;
	}
	
	public Manager(String name, int salary, String department) {	// 첫 줄에서 부모 클래스의 기본 생성자가 암묵적으로 호출된다.
		this.name = name;
		this.salary = salary;
		this.department = department;
	}
}
```



#### 예시 2: 부모 클래스에 기본 생성자가 필요 없는 경우

```java
package my_employee;

public class Inheritance {

	public static void main(String[] args) {
		Manager mng = new Manager("김현영", 20000000, "개발");
		Employee emp  = new Employee("이구망", 10000000);
		System.out.println(emp.getEmployee());
		System.out.println(mng.getManager());
		
	}

}

class Employee {
	String name;
	int salary;
	static int cnt;

	public Employee (String name, int salary) {						// 기본 생성자는 사라진다.
		this.name = name;
		this.salary = salary;
	}
	
	public String getEmployee() {
		return this.name + "'s 월급: " + salary;
	}

}

class Manager extends Employee {
	
	String department;
	
	public String getManager () {
		return this.name + "'s 월급: " + salary + ", 부서: " + department;
	}
	
	public Manager(String name, int salary, String department) {  	  // 자식의 생성자에서 super 키워드를 사용해서 부모 생성자를 호출했다.
		super(name, salary);										  // 따라서 부모 클래스에 기본 생성자가 필요 없다.
		this.department = department;
	}
}
```

#### 예시 3: 생성자 호출 로직

- 부모 생성자에서 Object 클래스의 기본 생성자를 생성하게 된다.

```java
package my_employee;

public class Inheritance {

	public static void main(String[] args) {
		Manager mng = new Manager();
	}

}

class Employee {
	String name;
	int salary;
	
	public Employee () {
		// super(); // Object 클래스 호출
		System.out.println("Employee 기본 생성자!");
	} 
	
	public Employee (String name, int salary) {
		this.name = name;
		this.salary = salary;
		System.out.println("Employee 이름 월급 생성자!");
	}
}

class Manager extends Employee {
	public Manager() {
		System.out.println("자식 생성!");
	}
}
```

### 3. super

this는 자기 자신의 인스턴스, super는 부모 클래스의 인스턴스를 의미한다.

super 키워드는 상속관계의 **하위클래스에서 상위클래스의 구성요소를 명시적으로 호출**할  때 사용되는데

어차피 상속받기 때문에 하위클래스에서 상위클래스의 멤버를 사용할 수 있으나, 특별한 경우에는 super를 사용해야 한다.

1. 부모클래스의 멤버와 자식클래스의 멤버가 이름이 동일한 경우

   - `super.부모멤버` 형태로 사용
   - 거의 사용되지 않는데, 부모의 인스턴스를 중복 선언하는 것이므로 잘못 설계된 클래스 구조이다.

   ```java
   public class Person {
   	int age = 20;
   }
   
   public class Man extends Person{
   	int age = 40;
    	public void getInfo() {
    		System.out.println( age ); //40 출력 , this.age에서 this생략
    		System.out.println( super.age ); // 20 출력
   	}
   }
   ```

   

2. **자식 생성자**의 **첫 라인에서** 명시적으로 **부모의 생성자를 호출**하는 경우

   - `super();`

   - 명시적으로 부모 생성자를 호출 하는 이유는 선언된 곳(부모 클래스)에서 초기화 작업을 하기 위한 목적이다.
     - 객체지향적인 코딩이고, 자식쪽에서의 코드양을 줄여줄 수 있다.
     - `this.부모인스턴스변수 = 매개변수`형식으로 자식 생성자에서 넣어줘도 들어가긴 한다.
     



- 사용예시

```java
package my_employee;

public class Inheritance {

	public static void main(String[] args) {
		Manager mng = new Manager("김현영", 20000000, "개발");
		Employee emp  = new Employee("이구망", 10000000);
		
		System.out.println(emp.getEmployee());
		System.out.println(mng.getEmployee());
		
	}

}

class Employee {
	
	String name;
	int salary;
	static int cnt;
	
	public Employee (String name, int salary) {	
		this.name = name;
		this.salary = salary;
	}
	
	public String getEmployee() {
		return this.name + "'s 월급: " + salary;
	}
}

class Manager extends Employee {
	
	String department;
	
	public Manager(String name, int salary, String department) { 
		super(name, salary);										 
		System.out.println(this.name);
		this.department = department;
	}
	
	public String getEmployee() {		
		return super.getEmployee() + ", 부서: " + department;		// 부모의 getEmployee 메서드와 동일한 이름이지만, super를 붙여 구별
	}
}
```



## III. 접근지정자(Access Modifier)

외부 클래스가 특정 클래스내의 인스턴스 변수나 메서드의 접근을 제어 할 수 있도록 

클래스, 메서드, 인스턴스 변수, 생성자를 선언할 때 ‘접근 지정자’를 같이 사용할 수 있다.

- 접근 지정자 4가지
  - default 지정자는 아무것도 적지 않은 경우를 나타낸다.
  - 아래 표에서의 상속 관계는, 같은 패키지의 상속관계가 아니라 다른 패키지의 상속관계를 의미한다.
    - 또한 자식에서 부모를 참조하는 것을 말하는 것이지, 반대가 아니다.

![image-20230411133546859](C:\Users\bizyoung93\Desktop\TIL\10_Java\07_class_relationship.assets\image-20230411133546859.png)

- 일반적으로 클래스와 메서드는 public으로 지정한다.

- **일반적으로 인스턴스 변수는 private으로 지정**한다.
  
  - 외부에서의 직접 접근을 방지하고, 생성자와 메서드를 통해 검증 작업을 거친 후 저장 및 관리한다.
  
- private을 이용해서 클래스의 멤버(변수, 메서드)를 설정하면 두 가지 이점이 있다.

  1. 첫째는 외부에서 접근시 클래스의 상세한 구조(private로 된 멤버)를  알 필요가 없기 때문에 클래스간의 복잡성이 감소된다. 
  
  2. 두 번째는 직접 접근이 불가능하기  때문에 잘못된 데이터가 저장되는 것을 방지할 수 있다. 
  
- 이 개념을 객체지향에서는 은닉화(Encapsulation)라고 한다.

### 1. 같은 패키지에서의 접근지정자 사용

```java
package accessmodifier;

public class AccessModifier {

	public static void main(String[] args) {
		Sub mySub = new Sub();
		mySub.print();
	}
}

class Super {
	public int numPublic = 10;
	protected int numProtected = 20;
	int numDefault = 30;
	private int numPrivateSuper = 40;
    
	public int getNum() {
		return numPrivateSuper;
	}
}

class Sub extends Super {
	
	private int numPrivaetSub = 50;
	
	public void print() {
		System.out.println(numPublic);
		System.out.println(numProtected);
		System.out.println(numDefault);
		// System.out.println(numPrivateSuper); // => private 접근지정자를 씌운 변수에는 다른 클래스에서는 접근불가
		System.out.println(getNum());			// 상속받았기 때문에 메서드 사용가능
 		System.out.println(numPrivaetSub); 		// 같은 클래스 안에 정의된 변수는 private 이라도 접근가능
		
	}
}
```



### 2. 다른 패키지에서의 접근지정자 허용

```java
// main class

package accessmodifier;
import access_sub.Sub;

public class AccessFromOther {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sub mySub = new Sub();
	}

}


// Super class

package access_super;
import access_sub.Sub;

public class Super {
	public int numPublic = 10;
	protected int numProtected = 20;
	int numDefault = 30;
	private int numPrivate = 40;
	
	public void getNum5FromChild () {
		Sub mySub = new Sub();
		// System.out.println(mySub.num5); 	// 기본적으로 protected가 허락하는 참조관계는, 부모의 값을 자식이 참조할 수 있다는 것이지, 반대가 아니다.
		mySub.getNum5();					// 얘처럼 메서드를 통해 간접접근이 필요하다.
	}
}

// Sub class

package access_sub;
import access_super.Super;

public class Sub extends Super {
	
	protected int num5; 					// protected라도 부모에서는 참조 불가능
	
	public Sub() {
		System.out.println(numPublic);		// public	 &
		System.out.println(numProtected);	// protected => 둘은 자식에서 참조 가능
		
		// System.out.println(numDefault);		// default &
		// System.out.println(numPrivate);		// private 	 => 둘은 상속관계에서 직접 참조 불가능
	}
	
	public int getNum5 ( ) {
		return num5;
	}
}

```



## IV. 메서드 오버라이딩

하위 클래스에서 부모 클래스의 메서드를 재정의해서 사용하는 것이 메서드 오버라이딩이다.

**오버로딩과 구분하자.**

=> 오버로딩(과적)은 생성자, 메서드를 같은 이름, 다른 인자로 여러 개 생성하는 것

규칙은 다음과 같다.

1. 상속이 전제되어야 한다.
2. **메서드 이름이 반드시 동일해야 된다.**
3. 메서드 **리턴타입**이 반드시 **동일**해야 된다. 
   - 단, 상속관계인 경우에는, 보다 작은 타입으로 재정의 가능하다.
   - 작은 타입이란 여러 가지를 의미한다: [참고](https://stackoverflow.com/questions/14694852/can-overridden-methods-differ-in-return-type)
4. 메서드 **인자 리스트**가 반드시 **동일**해야 된다.
5. 접근 지정자는 부모의 레벨보다 **같거나 확대**만 가능하다.
   - 확대란, 더 넓은 접근을 가능하게 하는 것을 의미한다.
   - 예컨데, (default) -> protedted -> public의 방향을 의미한다.
6. 예외 클래스는 부모의 클래스보다 계층적으로 같거나 하위 클래스만 사용 가능하다.
7. **static, final, private** 지정자를 가진 메서드는 **오버라이딩이 불가능**하다.
8. 오버라이딩 된 메서드라는 것을 컴파일러에게 알려주기 위해 `@Override` **어노테이션을 사용**한다.
   - 사용하지 않아도 되지만 사용하는 것이 좋다.
9. 오버라이딩 한 후, 상위 메서드의 리턴값을 그대로 활용하기 위해 `super.methodName()`을 사용할 수도 있다.
10. IDE에서는 간편하게 오버라이딩 메서드를 생성 가능하다.

- 예시

예를 들어, Super 클래스에서 선언한 sayEcho 메서드를 오버라이딩 하는 경우

`Object sayEcho(String myStr) throws Exception {}`

Sub 클래스에서 오버라이딩한 sayEcho 클래서는 다음과 같은 형식을 가질 수 있다.

`@Override`

`String sayEcho(String myStr) {}`

1. 메서드 이름은 sayEcho로 **반드시 동일**
2. 인자 리스트도 `String` 한개로 **반드시 동일** => 이름은 달라도 상관없다.

3. 리턴타입이 Object이므로, Object와 같거나 Object의 서브타입인 String으로 리턴값을 재정의 가능

4. 하위 메서드에서는 부모에서 사용된 예외클래스 보다 계층적으로 같거나 하위 클래스를 지정할 수 있다. 

```java
package method_overiding;

public class MethodOveriding {

	public static void main(String[] args) {
		Sub mySub = new Sub();
	}

}


class Super {
	
	static int myInt=1;
	
	Object sayEcho(String myStr) throws Exception {
		return new Object();
	}
}

class Sub extends Super {
	
	@Override
	String sayEcho(String myStr) {

		return "ㅇ";
	}
	
}
```

### 예시

```java
package com.method_overiding;

public class MethodOveriding {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee myEmp = new Employee("김현영", 31);
		Manager myMng = new Manager("김기태", 32, "개발");
		
		System.out.println(myEmp.getEmployee());
		System.out.println(myMng.getEmployee());
		
	}

}

class Employee {
	
	String name;
	int age;
	
	public Employee(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public String getEmployee () {
		return name + ": " + age;
	}
}

class Manager extends Employee {
	
	String department;
	
	public Manager(String name, int age, String department) {
		super(name, age);
		this.department = department;
	}
	
	@Override
	public String getEmployee () {
		return super.getEmployee()+ ": " + department; // 오버라이딩하며 super의 메서드를 사용한다.
	}
}
```



### 참고: static, final, private

- 셋 다 메서드에 붙여주면 오버라이딩이 불가능하다는 공통점이 있다.

1. static
   - static 변수는 상속 가능
   - static 메서드는 상속은 가능, **오버라이딩 불가능**

2. final
   - 클래스에 사용하면 **상속이 불가능**
   - 메서드에 사용하면 **오버라이딩이 불가능**
   - 변수에 사용하면 **값 변경**이 **불가능**

3. private
   - private 클래스는 상속이 불가능!
   - private 메서드는 **오버라이딩이 불가능!**



## V. 다형성(Polymorphism)

자바에서, 기본 데이터형은 같은 계열이고 더 큰 타입이면 다른 타입의 변수에도 저장이 가능하다.

예를 들어 `long` 변수에는 byte, short, int, long 데이터형을 저장 가능하다.

기본 데이터형과 마찬가지로 참조 데이터 형에서도 1) 같은 계열이고 2) 큰 타입이면 하나의 변수가 여러 클래스 타입의 객체를 저장할 수 있다.

1. 같은 계열은, 상속을 의미하고
2. 큰 타입은, 부모 클래스를 의미한다.

즉, 상속관계의 계층구조에서 **상위타입의 변수**로 모든 **하위타입을 참조**할 수 있는 특성을 다형성이라고 한다.

**해당 변수는 Employee 타입이면서 실행할 때 동적으로 생성한 클래스 타입을 참조하게 된다.** - 동적 바인딩

![image-20230412110533469](C:\Users\bizyoung93\Desktop\TIL\10_Java\07_class_relationship.assets\image-20230412110533469.png)

### 1. 특징

다형성은 다음과 같은 특징을 갖는다.

1. 반드시 상속관계가 전제되어야 한다.
2. 코드는 `부모 타입 = 자식 타입` 형식으로 사용된다.
   - 만약 부모 타입에 저장된 자식 타입의 실제 데이터형을 알아내려면 instance of 연산자를 사용한다.
3. `자식 타입 = 부모 타입` 형식으로 사용하기 위해서는 강제 형변환 시켜야 한다.
4. **서로 다른 데이터를 배열에 저장**하거나 **서로 다른 데이터를 하나의 메서드에 전달**하는 경우 다형성을 활용할 수 있다.

### 2. 동적 바인딩

- 실행할 당시의 객체 타입을 기준으로 실제 실행할 메서드를 호출하는 것을 **동적 바인딩(Dynamic Binding)**이라고 한다.
- 컴파일 시점에서의 getEmployee()는 Employee 클래스의 메서드로 인식하고, 런타임에서는 Manager의 메서드로 인식된다.
- 주의할 점은, 메서드에서만 동적 바인딩이 발생한다는 것이다.
  - **변수같은 경우는 컴파일 단계와 실행단계 모두에서 부모 인스턴스의 변수로 인식한다.**
  - 즉, `Parent p  = new Child();` 형태로 동적 바인딩을 했을 경우,
  - 만약 부모와 자식 클래스에 동일한 인스턴스 변수명이 존재한다면
  - `p.variable`로 참조했을 경우, **부모의 인스턴스 변수를 우선적으로 참조**하게 된다.

```java
package abstractclass;


public class MethodOveriding {

	public static void main(String[] args) {
		Employee myEmp = new Employee("김현영", 31);
		System.out.println(myEmp.getEmployee());
		
		
		// Employee 변수에 Manager Instance를 넣었을 경우
		myEmp = new Manager("김기태", 32, "개발");  // myEmp 변수는 동적으로 Manager 클래스를 참고
		System.out.println(myEmp.getEmployee()); // 따라서 Employee 클래스의 getEmployee가 아닌 Manager의 getEmployy를 참조하게 된다.
		
		System.out.println(myEmp.name);			 // 동적 바인딩은 변수에서는 발생하지 않는다 => 부모의 변수를 참조하게 된다.
		// System.out.println(myEmp.sex);		 // 동적 바인딩이 발생하지 않기 때문에, 자식에만 존재하는 변수를 참조할 수 없다.
		
		// Manager에 Manager 인스턴스럴 넣었을 경우
		Manager myMng = new Manager("김기태", 32, "개발");
		System.out.println(myMng.name);			 // 여기서는 정상적으로 자식의 변수를 참조한다.
												 // 자식에 해당이름의 인스턴스 변수가 없을 경우에는, 부모의 변수를 참조하게 된다.
	}									

}

class Employee {
	
	String name;
	int age;
	
	public Employee(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	public String getEmployee () {
		return name + ": " + age;
	}
}

class Manager extends Employee {
	
	String department;
	String name;
	String sex;
	
	public Manager(String name, int age, String department) {
		super(name, age);
		this.department = department;
	}
	
	@Override
	public String getEmployee () {
		return super.getEmployee()+ ": " + department; // 오버라이딩하며 super의 메서드를 사용한다.
	}
}
```

### 3. 다형성 응용

- 다형성을 이용하여, 메서드를 여러 개 만들거나 오버라이딩하는 귀찮은 방식을 배제하고 하나의 메서드로 상속관계에 있는 다양한 인스턴스를 구분할 수 있다.
  - 즉, 부모 클래스인 Employee 클래스에서 모든 하위 클래스의 세밀한 구현까지 작성한 후, 구별해서 사용하는 것이다.
- 이 때, instanceof 연산자를 이용한다.
  - instanceof 연산자는 해당 변수의 자료형이 아니라, 변수에 저장된 실제 인스턴스가 어떤 클래스의 인스턴스가 맞으면 true를 반환한다.
  - 주의할점은, instanceof 연산자는 부모 클래스에 걸어줘도 true를 반환한다는 것이다.
  - 따라서 if 등으로 비교할때는, 가장 상위의 클래스를 가장 밑으로 내려주어야 한다.

```java
class Animal {}
class Mammal extends Animal {}
class Cat extends Mammal {}

// 아래 코드는 전부 true를 반환한다.
Cat cat = new Cat();
if (cat instanceof Animal) {
    System.out.println("cat is an Animal");
}
if (cat instanceof Mammal) {
    System.out.println("cat is a Mammal");
}
if (cat instanceof Cat) {
    System.out.println("cat is a Cat");
}
```

- 대부분의 API는 다형성을 이용해서 구현되어 있다.

- 응용 예시

```java
package com.poly;

class Employee {
	
	// main 메서드에서 실행한 모든 메서드는 여기로 들어온다.
	// 모든 경우의 인스턴스를 포괄할 수 있는 Employee 변수를 사용한다.
	public void taxRate(Employee e) {
		// 순서를 주의해야 한다. => 받은 세 가지 인스턴스 모두 부모 클래스로 instanceof를 찍어주면 true가 나온다
		// 즉 해당 경우를 맨 아래로 내려주어야 한다.
		if (e instanceof Manager) {
			// 해당 경우에 속할 경우 캐스팅을 통해 사용한다.
			Manager mng = (Manager)e;
			System.out.println("매니저");
		} else if (e instanceof Engineer) {
			Engineer eng = (Engineer)e;
			System.out.println("엔지니어");
		} else if (e instanceof Employee) {
			System.out.println("임플로이");
		}
	}
}

class Manager extends Employee {}

class Engineer extends Employee {}

public class Main {

	public static void main(String[] args) {
		
		// 인스턴스 생성
		Employee emp = new Employee();
		Manager mng = new Manager();
		Engineer eng = new Engineer();
		
		// 아래와 같이 해 주어도 상관은 없다.
		// 다형성 때문에 껍데기만 달라지기 때문이다.
		// Employee emp = new Employee();
		// Employee mng = new Manager();
		// Employee eng = new Engineer();
		
		// 같은 메서드에 넘겨준다. => 해당 메서드는
		emp.taxRate(emp);
		mng.taxRate(mng);
		eng.taxRate(eng);
	}

}
```



### 4. 다형성 응용2 : 배열 관리

- 다음 예는 다형성을 이용해서 배열을 좀 더 효율적으로 사용할 수 있는 방법이다. 

- 시나리오는 애완동물 관리 프로그램을 개발할 목적이며 자식 클래스로 Cat과 Dog을 만들고  부모 클래스로 Pet 클래스를 작성하고 생성된 Cat과 Dog은 Pet 배열을 사용하여 관리하 도록 구현한다. 

- **Object 배열을 만들면, 모든 종류의 객체를 저장할 수 있다.**

```java
package pet;

public class Main {

	public static void main(String[] args) {
		Pet [] pets = {
			new Cat("앙뇽이", 24, "수컷", "노란색"),
			new Dog("댕댕이", 2, "암컷", "코카스패니얼")
		};
		
		System.out.println(pets[0].getPet());
		System.out.println(pets[1].getPet());
	}
	
	
}


class Pet {
	String name;
	int age;
	String gender;
	
	public Pet (String name, int age, String gender) {
		this.name = name;
		this.age = age;
	}
	
	public String getPet() {
		return "이름:" + name + age;
	}

}



class Cat extends Pet {
	
	String color;
	
	public Cat(String name, int age, String gender, String color) {
		super(name, age, gender);
		this.color = color;
	}
	
	@Override
	public String getPet() {
		return "이름:" + name + age + color;
	}
}

class Dog extends Pet {
	
	String species;
	
	public Dog(String name, int age, String gender, String species) {
		super(name, age, gender);
		this.species = species;
	}
	
	@Override
	public String getPet() {
		return "이름:" + name + age + species;
	}
}
```



### 5. 형변환

다형성을 이용해서 객체를 생성한 후, 자식에만 존재하는 멤버에 접근하려면 형변환이 필요하다.

`Pet p = new Cat("야용", "암컷", 2);`

Cat 에만 있는 변수에 접근하려면, 캐스팅이 필요하다.

`Cat c = (Cat)p;` 필요



## VI. Object 클래스

Object 클래스는 모든 클래스의 최상위 클래스이다. 명시적으로 extends를 하지 않아도 자동으로 상속을 받는다.

**따라서 모든 클래스는 Object 클래스의 메서드를 선언 없이 사용할 수 있고 오버라이딩 메서드를 작성하는 것도 가능하다.**

대표적으로 두 가지가 있다.

### 1. equals()

객체의 값을 비교(동등비교) 할 때 사용한다.

기본 데이터형의 값 비교시에는 `==`를, 인스턴스의 값 비교시에는 equals 메서드를 사용한다.

비교되는 객체가 정해져 있지 않기 때문에 equals 메서드의 파라미터는 모든 클래스가 저장될 수 있도록 다형성을 적용하여 최상위 클래스인 Object형으로 파라미터를 지정한다.

일반적으로 String, Integer등의 대부분의 API는 이미 equal를 사용할 때 정상적으로 값을 비교할 수 있도록 구현되어 있다.

#### 주의점

Object 클래스의 equals 메서드를 살펴보면 값 비교를 == 연산자를 이용해서 구현되어 있다. 

- 즉, 주소값 비교로 구현되어 있다.

따라서 Object 클래스의 equals메서드를 하위 클래스에서 재정의 없이 사용하면 실제 값을 비교하지 않고 위치 값을 비교하게 된다.

원하는 결과를 얻기 위해서 실제 값을 비교하도록 재정의해야 되며 추가로 hashCode() 메서드까지  재정의해야 된다.

IDE에서 해당 클래스에서 우클릭 => source => equals() & hashcode로 간편하게 구현 가능하다.

- false가 뜨는 예시

```java
package pet;

public class Main {

	public static void main(String[] args) {
		
		Person person1 = new Person("김현영", 31);
		Person person2 = new Person("김현영", 31);
		
		System.out.println(person1.equals(person2));
	}
	
	
}

class Person {
	String name;
	int age;
	
	public Person (String name, int age) {
		this.name = name;
		this.age = age;
	}
}
```

- .equals 오버라이딩 및 hashcode 구현 후

```java
package pet;

import java.util.Objects;

public class Main {

	public static void main(String[] args) {
		
		Person person1 = new Person("김현영", 31);
		Person person2 = new Person("김현영", 31);
		
		System.out.println(person1.equals(person2)); // false	
	}
	
	
}

class Person {
	String name;
	int age;
	
	@Override
	public int hashCode() {
		return Objects.hash(age, name);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Person other = (Person) obj;
		return age == other.age && Objects.equals(name, other.name);
	}

	public Person (String name, int age) {
		this.name = name;
		this.age = age;
	}
}
```



### 2. toString() 

객체를 문자열로 변경시키는 메서드

toString() 메서드는 객체를 참조하는 **참조형 변수를 print & println 메서드를 사용하여 콘솔에 출력할 때 자동으로 호출**된다.

- 객체를 문자열로 변경시켜야 콘솔에 출력이 가능하기 때문이다.

```java
import java.util.Date;

Date d = new Date();

// 아래 두 코드는 같은 코드이다.
System.out.println(d);
System.out.println(d.toString())
```

- 기본적으로, Object 클래스에 있는 toString()은 `클래스명@16진수` 형태로 뽑혀 나온다.
  - 따라서 다른 여타 API에서는, toString() 메서드를 오버라이딩해서 사용한다.

즉, 사용자가 임의로 만든 클래스는 toString()을 씌워도 참조값(주소값)이 출력되기 때문에, 임의로 구현해 주어야 한다.

역시 IDE를 사용하면 간단하다.

```java
package pet;

import java.util.Date;
import java.util.Objects;

public class Main {

	public static void main(String[] args) {
		
		Date date = new Date();
		
		System.out.println(date);				// 값을 출력
		System.out.println(date.toString());	// 오버라이드 되어 있음
		
		
		Person person = new Person("김현영", 31);
		
		System.out.println(person);				
		System.out.println(person.toString());
		
	}
}

class Person {
	String name;
	int age;
	
// 얘가 없으면 주소값을 출력
//	@Override
//	public String toString() {
//		return "Person [name=" + name + ", age=" + age + "]";
//	}

	public Person (String name, int age) {
		this.name = name;
		this.age = age;
	}
}
```



