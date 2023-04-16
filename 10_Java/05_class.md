# Class

자바에서는 모든 객체가 클래스로 정의되어지며 가장 작은 실행단위이다.

클래스를 통해서 자바프로그램 개발에 필요한 데이터 및 처리작업을 수행할 수 있다.

### 객체란?

현실세계에 존재하는 사물을 의미한다.

- 객체 구성요소 2가지

  - 속성
    - 객체를 나타내는 특성(성질)
    - => 변수, 필드

  - 동작
    - 객체의 기능
    - => 메서드

- 추상화(모델링)
  - 프로그램 개발하기 위해서 필요한 객체/속성/동작 추출
  - 순서
    1. 의뢰
    2. 분석
       - 고양이 객체를 뽑아냄
    3. 설계
       - 고양이 객체를 클래스로 설계해냄
       - 클래스 다이어그램 그림(UML: Unified Modeling Language 이용)
    4. 구현
       - 인스턴스
    5. Test
    6. 배포

### 객체지향의 3요소

1. 은닉화
2. 상속
3. 다형성

## I. 클래스

- 형식

```java
modifier class Classname {
    [instance variable]
    [method]
    [constructor]
}
```

### 1. 지정자(modifier)

- 특정 목적을 위해서 사용하는 키워드를 의미
- 클래스, 변수, 메서드 선언에 사용할 수 있고 생략이 가능하다.

#### 1. 일반 지정자

- static, final, abstract

#### 2. 접근 지정자

- private, protected, (default), public
- 일반적으로 클래스는 public을 사용

- 일반 지정자와 접근 지정자는 같이 사용 가능하다.



### 2. 클래스명

- 클래스를 가장 잘 표현할 수 있는 의미 있는 이름으로 지정
- 명사형으로 작성, 첫 글자는 대문자로 지정



### 3. 클래스의 3가지 구성요소

1. 인스턴스 변수
   - 클래스 구성요소인 속성값을 저장하기 위한 용도
   - 멤버변수 라고도 부름
2. 메서드
   - 인스턴스 변수에 저장된 속성 값을 수정하거나 조회 또는 
3. 생성자
   - 인스턴스 변수를 초기화 하는 역할
   - 즉, 변수에 데이터를 맨 처음 지정할 때 사용됨
   - 메서드를 이용해서 초기화를 하는 것도 가능하지만 생성자를 이용해서 초기화를 하는 것을 권장



### 4. 클래스의 기본적인 구성

해당 순서에 따른다.

1. 변수
2. 생성자
3. 메서드
   - setter
   - getter
     - setter와 getter는 쓰든, 쓰지 않든 기본적으로 만들어주고 사용한다.
   - 추가적인 메서드들

## II. 클래스의 구성요소

- 인스턴스 변수는 데이터가 실제로 저장되는 곳
- 생성자를 통해 변수에 데이터를 맨 처음 저장
- 메서드는 저장된 데이터를 수정, 삭제, 조회
- **클래스를 사용하려면 객체생성(instance화)는 반드시 선행되어야 한다.**



### 1. 인스턴스 변수

- 클래스를 통해서 객체 생성된 인스턴스에 필요한 데이터를 저장하는 곳
- 클래스를 인스턴스화(객체생성)할 때마다 메모리에 새로 생성됨
  - 각 인스턴스마다 서로 다른 데이터로 관리
- 소문자로 작성
- 힙 영역에 저장됨

- 형식
  - `[지정자] 데이터형 변수명;`

- **자동으로 기본값이 저장됨**
  - 정수형 0
  - 실수형 0.0
  - 논리형 false
  - 참조형 NULL
  - **메서드 안에서 선언된 변수는 로컬변수**
    - **초기화가 되지 않으므로 주의**



### 2. 메서드

클래스의 기능적인 면을 표현할 때 사용하고 일반적으로 인스턴스 변수에 저장된 데이터를 수정, 조회 및 중복코드 처리시 사용

**멤버 메서드라고 하며 클래스를 인스턴스화 할 때마다 매번 생성되지는 않고, 메서드 코드에 대한 주소만 갖고 있다가 이를 공유해서 사용됨**

- 메서드 코드 저장 장소
  - JAVA 8버전 이전: Method Area에 저장
  - 이후: OS가 관리하는 MetaSpace 영역

- 모두 동일한 코드를 사용하기 때문
- 소문자로 작성

객체 생성 후 메서드 호출 작업을 해야 동작한다.

호출하는 메서드와 호출 당하는 메서드가 존재한다.

다음과 같은 2가지로 구분될 수 있다.

- caller 메서드
  - 특정 동작을 수행하는 메서드를 호출하는 메서드를 의미한다.
  - 가변인자를 사용할 때는 `...`를 사용한다.
- worker 메서드
  - caller 메서드에 의해서 호출되어 실제로 특정 작업을 수행하는 메서드이다.
  - 일반적으로 메서드라고 하면 **worker 메서드**를 의미한다.
  - worker 메서드는 역할에 따라서 getter와 setter 2가지로 구분된다.
    - getter와 setter는 변수를 만든 수 eclipse 툴에서 생성 가능하다.
      - 해당 메서드들은 쓰든, 안쓰든 습관적으로 만들어 놓는 것이 좋다.
      - 은닉화(Encapsulation)를 위해 쓴다. 인스턴스 변수는 private로 지정하고 메서드를 통해 접근
      - 유효성을 검증하려는 목적도 있다.
        - 직접 접근 시에는 에러가 뜨게 하고(private 지정)

#### 1. setter

인스턴스 변수에 저장된 데이터를 수정할 목적으로 사용된다.

메서드 이름은 `set변수명`으로 지정한다.

- camelCase를 사용하기 때문에, 변수명의 첫 글자는 대문자를 붙인다.
  - setAge

#### 2. getter

- 인스턴스 변수의 데이터를 조회할 목적으로 사용된다.
- `get변수명`으로 지정한다.



#### 메서드의 형식

- 모두 소문자로 작성한다.

```java
/*
[지정자] 리턴타입 메서드명 ([파라미터, ...]) {
    
    // 실행문
    
    [return 결과값;]
}
*/

public static void main (String[] args) {
    
    
}
```

- 지정자는 일반, 접근 지정자 모두 사용 가능하며 일반적으로 public 접근지정자를 사용한다.

- 호출한 곳(caller)에서 호출된 곳(worker)로 넘어가게 되며, 호출된 곳의 작업이 모두 끝나면 호출한 곳으로 복귀한다.

  - return 값을 가지고 복귀하는 메서드가 주로 getter 메서드 형태이다.

- parameter를 넘겨 데이터를 인스턴스 변수에 저장할 수 있다.

  - setter 메서드가 주로 이런 형식이다.

- 결과값이 없을 때는 `return;`을 사용하거나 `return`을 명시하지 않고, 리턴타입에 void를 **반드시** 지정한다.

  

#### 메서드의 호출

메서드를 호출할 때는 **메서드명과 인자 리스트가 반드시 일치**해야 한다.



#### main 메서드

main 메서드는 명시적으로 후출하지 않아도 실행될 수 있는 유일한 메서드이자, 프로그램의 시작점이다.

main method는 static 메서드이다.

하나의 애플리케이션에서 main 메서드를 가진 클래스는 반드시 존재하며 또한 하나의 클래스에서만 정의할 수 있다.

main 메서드를 갖고 있는 클래스를 핸들링 클래스라고 부른다.

형식은 반드시 다음과 같이 정의해야 자동 실행된다.

`public static void main(String[] args) {}`

- 핸들링 클래스의 역할
  1. main에서, new를 이용해서 클래스 로딩(메모리에 클래스를 올리는 것)을 한다.
  2. 값을 직접, 또는 간접 참조로 저장하거나 조회한다.



### 3. 생성자(constructor)

인스턴스 변수를 초기화하는 역할이다.

인스턴스 변수에 직접 접근해서 초기화하는 방법은, 초기화 시점이 매우 늦기 때문에, 생성자를 이용해서 초기화를 하는 것이 가장 빠르고 가장 바람직한 방법이다.

영역이 생성되며 바로 초기화하는 것이기 때문이다.

인스턴스 생성 시 **반드시 호출해야 한다.**

setter 메서드를 이용해서 생성할 수도 있지만, **일반적으로 생성자를 이용해서 초기화**를 하고 setter 메서드를 이용해서 수정한다.

**생성자도 메서드처럼 호출되어야 수행되며 필요에 따라 여러 개 정의가 가능하다.** 

메서드와 차이점은 **1) 리턴타입이 없고**, 반드시 **2) 클래스명으로 생성자 이름을 지정**해야 된다.

접근지정자에는 **일반적으로 public을 사용**하며, 파라미터를 이용해 인스턴스 변수를 초기화한다.

- 형식
  - `[접근지정자] 클래스명 ([파라미터]) {}`

- 예시

```java
public class Student {
    
	// 인스턴스 변수 2개
	String name;
	int age;

    public Student(String n, int a) {
        name = n;
        age = a;
    }
}
```

- 생성자 호출 코드
  - `new 클래스명([args...]);`
- **생성자를 호출할 때는 메서드와 같이 인자를 파라미터와 정확히 맞춰주어야만 한다.**

#### 기본 생성자 (derault constructor)

모든 클래스에는 자동으로 기본 생성자가 생성되며, 다음과 같은 **파라미터 없는 형식**을 갖는다.

- 자동으로 생성되는 생성자, 혹은 파라미터 없는 형식을 가진 생성자를 기본 생성자라고 부른다.

기본 생성이므로, 접근지정자에는 **클래스 선언시 사용한 접근지정자를 따르며** 생성자의 파라미터가 없다.

- 형식
  - `[접근지정자] 클래스명 () {}`

내부적으로는 자동으로 기본 생성자가 삽입되지만, 개발자가 **명시적으로 생성자를 지정하면 기본 생성자는 자동 생성되지 않는다.**



## III. 객체 생성

클래스를 정의한 후에는 반드시 객체를 생성해야 클래스를 사용할 수 있다.

new 키워드와 함께 생성자를 호출하는 작업으로서, 클래스 내의 인스턴스 변수와 메서드를 메모리에 생성시키는 작업이다.

- 형식
  - `클래스형 변수명 = new 클래서형([값...])`

값을 저장할 수 있는 파라미터 있는 **생성자를** 호출하거나, 파라미터 없는 **기본 생성자**를 호출할 수 있다.

메서드와 마찬가지로 생성자 이름과 인자 리스트가 일치되어야 한다.

new를 사용해서 생성자를 호출하면 클래스의 멤버가 메모리에 생성이 된다. 

- 인스턴스 변수는 힙 영역에, 메서드는 메서드 영역에 생성이 된다.
  - JAVA 8 버전부터는 다를 수 있다.

- 해당 메모리 위치를 변수에 저장한 후 참조(참조 데이터형: 클래스)하는 것이다.

클래스의 멤버에 접근하기 위해 참조형 변수와 .(dot)를 이용한다.

- 같은 클래스안의 메서드 및 인스턴스 변수에 접근하기 위해서는 다음과 같이 `.`를 사용하지 않고 **바로 접근할 수 있다.**

```java
public class Myclass {
    
    String name;
    
    public void setName(String n) {
        name = n; // name 그대로 호출 가능
    }
}
```

### 1. 인자 전달

- 원시형 변수를 인자로 전달하면, 파라미터(일종의 지역변수)에는 값이 복사되어 전달된다
- **참조 데이터형을 전달하면, 메모리 주소값이 복사**되어 전달되기에 한쪽 값이 변경되면 다른쪽에도 영향을 미친다.
  - call by reference
  - 배열 문서도 참조


```java
package practice;

public class StudentTest {

	public static void main(String[] args){
		Student hyun = new Student("김현영", 31);
		
		int zero = 0;
		int[] zeroArray = new int[5];
		
		hyun.giveValue(zero);
		hyun.giveRef(zeroArray);
		
		
		// 원본 값에 변화가 있을까?
		System.out.println(zero); 	// 없음: 0출력
		
		for(int x: zeroArray) {
			System.out.println(x);	// 있음: 1 1 1 1 1 출력
		}
		
	}
}

// =======================================================================

package practice;

public class Student {
	
	String name;
	int age;
	
	public Student(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	// 값을 받는 메서드 => 원본값에 영향 없음
	public void giveValue(int num) {
		num++;
	}

	// 주소를 받는 메서드 => 원본값에 영향 잇음
	public void giveRef(int[] nums) {
		for (int i=0; i < nums.length; i++) {
			nums[i]++;
		}
	}
}

```

### 2. 객체 소멸

인스턴스가 소멸되는 경우는 다양한 경우가 있지만, 대표적으로 객체가 참조되지 않는 경우가 있다.

다시 말해 어떠한 변수도 객체를 가리키고 있지 않는다면, 객체가 소멸한다는 것이다.

객체 소멸은 garbage collector에 의해 실행된다.



## IV. 메서드, 생성자 오버로딩

- 변수와 다르게 메서드와 생성자는 같은 클래스 내에서 같은 이름으로 여러 번 사용될 수 있으며, **같은 이름으로 된 메서드와 생성자를 오버로딩 메서드와 오버로딩 생성자라고 한다.**
- 기본적으로 이름이 동일하더라도 **인자 리스트가 다르면** 식별할 수 있기 때문에 가능하다.

- 오버로딩 메서드, 생성자를 작성하기 위한 규칙
  - 매서드 및 생성자 **이름이 같아야 한다.**
  - **인자 리스트는 반드시 달라야 한다.** (인자 개수 또는 인자 타입 또는 인자 순서)
    - 인자의 이름이 달라도 소용이 없다.
  - **리턴타입이 달라도** 위 두 항목이 같으면 오버로딩이 안된다.

- 대표적인 오버로딩 메서드가 `println()`, `print()` 메서드이다
  - 같은 이름의 메서드가, 서로 다른 다양한 인자를 받아 다른 메서드 취급을 당한다.

- 오버로딩 생성자를 사용할 때 주의할 점은, 명시적으로 파라미터 있는 생성자를 지정하면 기본 생성자가 자동 생성되지 않는다는 것이다.
  - 따라서 기본 생성자도 따로 작성해 주어야 한다.



## VI. this

this는 객체생성 후에 힙 메모리에 생성된 자기 자신의 인스턴스를 의미 / 참조한다.

**즉, 인스턴스가 자기 자신을 가리킬 때 사용될 수 있다.** 

프린트를 찍었을 때, 인스턴스 자체의 주소가 나온다.

일반적으로 this 키워드는 생략하고 사용하지만, 반드시 사용해야 하는 경우가 있는데 대표적인 경우는 다음과 같다.

1. 인스턴스 변수와 로컬 변수명이 동일한 경우
   - 메서드 안에 선언된 로컬 변수명과 인스턴스 변수명이 동일할 때, `this.변수명`으로 인스턴스 변수를 참조할 수 있다.
   - 이때 this를 붙이지 않으면 로컬변수를 참조한다.
2. **생성자**에서 **다른 오버로딩 생성자**를 **호출**하는 경우
   - this([값]) 형식으로 사용된다.
   - 주의할 점은 반드시 **생성자 첫 라인에서 사용**해야 하며, **인자 리스트가 반드시 일치**해야 한다.
   - 여러 생성자에 인스턴스 변수를 초기화하는 코드를 중복적으로 작성하지 않고, 하나의 생성자에만 이를 작성한 뒤 다른 생성자에는 이를 요청해서 사용하게 해 코드량을 절약할 수 있다.

```java
package practice;

public class StudentTest {

	public static void main(String[] args){
		
		Student hyun = new Student("김현영"); 	 // 이름만 넣는 인스턴스 생성
		
		Student go = new Student("고유한", 19); // 이름과 나이를 넣는 인스턴스 생성
		
		System.out.println(hyun.name);
		System.out.println(go.name);
	}
}

//========================================================================

package practice;

public class Student {
    
    String name;
    int age;
    
    // 인자를 2개 받는 생성자
    public Student(String name, int age) {
        this.name = name; // this를 안 붙여주면 name이 지역변수인지, 인스턴스변수인지 알 수 없다.
        this.age = age;
    }
    
    // 인자를 하나만 받는 생성자
    public Student(String name) {
        // 이 생성자에서 초기화하지 않는다.
    	this(name, 19); // 얘가 없었으면 아래와 같이 써 주어야 함
        /*
        this.name = name;
        this.age = 19;
        */
    }
    

}

```

- getter, setter와 마찬가지`로 생성자도 이클립스로 편하게 생성할 수 있다.



## VII. package와 import문

서로 관련 있는 클래스파일들을 묶어서 **관리**하는 것을 패키지라고 한다.

#### 패키지를 사용할 때 유의점

- 패키지문은 반드시 한번만 사용 가능하다.
- 클래스 선언보다 먼저 선언되어야 된다.
- 패키지명은 계층구조(서브 패키지)를 가질 수 있다.
  - 보통 2 ~ 3단계를 권장한다.

  - 각 계층별로 폴더가 생성된다.

- 패키지명이 중복되면 식별이 불가능하기 때문에 안된다. 따라서 유일한 값인 도메인 형식으로 지정하는 것을 권장한다.
  - **도메인으로 지정하는 것이 관례**이다.
  - com.daou 같이
- 패키지가 없으면 default package라고 한다.
  - 소스파일에 패키지 키워드는 없다

- 패키지가 서로 다른 클래스들끼리는 기본적으로 접근이 불가능하다.(import문으로 해결)
- JDK에서 제공해준 JAVA API도 패키지로 되어 있다. 
  - 대부분의 패키지 이름이 java 또는 javax  로 시작되는데, 사용자 지정 패키지명으로 API 패키지명은 사용이 불가능하다. 

- 따라서  java로 시작되는 패키지명은 사용할 수 없다.package을 지정하지 않으면 패키지가 없는 것이 아니고 default 패키지라고 부른다.하나의 어플리케이션에는 동일한 이름의 클래스를 여러 개 지정할 수 없으나 패키지가  다르면 가능하다.



### 1. 패키지 컴파일

패키지로 만든 클래스파일은, 일반 컴파일이 아닌 패키지 컴파일을 해야 한다.

패키지 컴파일은 다음 형식을 따른다

`$ javac -d 클래스파일저장경로(.==현재위치) 패키지명.클래스파일.java`



### 2. import문

기본적으로 패키지가 서로 다른 클래스 파일들은 접근이 불가능하다(다른 폴더에 접근 불가). 하지만 import 문을 사용하게 되면 패키지가 서로 달라도 접근 가능하다. 

import 문은 접근할 클래스파일의 패키지를 알려주는 용도로 사용된다.

`import 패키지명1.패키지명2.클래스명;`

import한 클래스를 사용할 때는, 클래스명만 명시해도 되고, 만약 여러 클래스와 이름이 겹칠 때는 패키지까지 명시해 주어야 한다.

`패키지명1.패키지명2.클래스명 = new 패키지명1.패키지명2.클래스명();`

#### import 사용 시 유의점

- import문은 여러 번 사용가능하다. 
- 클래스 선언보다 먼저 사용해야 되며 패키지 선언보다는 나중에 사용한다. 
- 클래스명 대신에 모든 클래스를 의미하는 * 를 사용할 수도 있다. 
- 하지만 가독성이 떨어지므로 권장하지 않는다. 
- API 중에서 **java.lang 패키지는 import 하지 않아도 되는 유일한 패키지**이다. 
- java.lang  패키지에는 String, Object 등 일반적으로 가장 많이 사용하는 클래스파일들의 패키지이기 때문에 명시적으로 import 하지 않아도 자동 import가 된다.  
- 결국 java.lang 패키지를 제외한 모든 클래스는 패키지가 서로 다르면 반드시 import 해 야 된다.



## VIII. static

클래스 변수와 클래스 메서드는 클래스 파일을 실행하면 메모리에 자동으로 로딩된다.

그 후 인스턴스를 생성할 때마다 인스턴스 변수와 메서드가 메로리에 로딩되고, 인스턴스 메서드가 실행되면 지역변수가 메모리에 로딩된다.

즉 클래스(클래스 정보와 static 멤버들)는 단 한번 생성되며, 생성된 여러 인스턴스에서 이를 공유하여 사용한다.

**static 변수는 ‘클래스’와 관계가 있으며 인스턴스 변수는 ‘인스턴스’와 관계가 있고 로컬 변수는 ‘메서드’ 와 관계가 있다.**



### 1. static 키워드의 특징

1. 클래스, 변수, 메서드의 지정자로 사용할 수 있다.

   1. 클래스에 사용될 때는 **Inner Class(중첩 클래스)에서만 사용**된다.

   2. static 변수는 클래스 변수라고 불리듯이 모든 인스턴스에서 공유해서 사용할 데이터를 만들 때 사용한다.

   3. static 메서드는 인스턴스 생성 없이 메서드를 사용하고 싶을 때 사용한다.

2. 단 한번, 프로세스가 생성될 때 생성되고 종료될 때 소멸한다. 또 자동으로 초기화된다.
   - **일괄적으로 선언된 다음 순서대로 초기화된다.**
   - 초기화되는 순서는 아래 초기화 블록 참고

3. 프로세스가 생성될 때 생성되므로 객체생성과 관련이 없다.

4. **생성된 모든 인스턴스에서 클래스명으로 접근이 가능하고 공유도 가능하다.**
   - 해당 클래스 뿐 아니라 다른 클래스의 인스턴스에서도 `클래스명.`으로 접근이 가능하다
   - 인스턴스를 통해서 클래스에 접근 가능하지만, 지양되는 방식이다.

5. **static 메서드는 오버라이딩이 불가능하다.**

6. static 메서드내에서 인스턴스 변수 접근이 불가능하다. 생성시점이 다르기 때문이다.

7. static 블록을 이용하여 어플리케이션에서 필요한 초기화 작업(파일 및 DB 연동)을 할 수 있다.

8. **프로그램 실행시, 만약 해당 클래스가 사용되는 경우 에만 메모리에 올라간다.**

   - static으로 명시된 멤버들은 모두 올라간다.

   - 단, 사용되지 않는 클래스 정보는 올라가지 않는다.

9. static으로 선언된 변수, 메서드는 Java 8 이전 버전에서는 method Area, 이후에는 Metaspace 영역에 저장된다.

```java
package counter;

public class Counter {
	
	public static void main(String[] args) {
		
		System.out.println(Inst.count);		 // 클래스 변수를 그대로 출력 => 인스턴스 생성 횟수
		
		Inst myInst = new Inst();			 // 인스턴스 생성
		
		System.out.println(myInst.getNum()); // 인스턴스가 배정받은 번호를 출력
		
		Inst myInst2 = new Inst();
		
		System.out.println(myInst2.getNum());
		
		System.out.println(Inst.count);		// 클래스 변수를 그대로 출력 => 인스턴스 생성 횟수
	}
}

class Inst {

	static int count;
	int num;
	
	public Inst () {
		count++;
		num = count;
	}
	
	public int getNum () {

		return num;
	}
}
```



#### 참고: 변수별 특징

![image-20230410095825357](C:\Users\bizyoung93\Desktop\TIL\10_Java\05_class.assets\image-20230410095825357.png)



### 2. static method 사용

- static 메서드의 예시
  - Integer.parseInt();

```java
package counter;

public class Counter {
	
	public static void main(String[] args) {
		
		System.out.println(Inst.count);		 // 클래스 변수를 그대로 출력 => 인스턴스 생성 횟수
		
		Inst myInst = new Inst();			 // 인스턴스 생성
		
		System.out.println(myInst.getNum()); // 인스턴스가 배정받은 번호를 출력
		
		Inst myInst2 = new Inst();
		
		System.out.println(myInst2.getNum());
		
		System.out.println(Inst.count);		 // 클래스 변수를 그대로 출력 => 인스턴스 생성 횟수
		System.out.println(Inst.getCount()); // 클래스 메서드를 인스턴스를 통하지 않고 사용 
		
	}
}

class Inst {

	static int count;						// 클래스 변수
	int num;								// 인스턴스 변수
	
	public static int getCount () { 	// static 메서드 선언
		// return num;						// 인식 못함 => static 메서드가 먼저 선언되기 때문
		
		return count;
	}
	
	public Inst () {						// 생성자			
		count++;
		num = count;
	}
	
	public int getNum () {

		return num;
	}
}
```



### 3. 초기화 블록

클래스에서 생성자와 비슷한 역할의 **초기화 작업**을 할 수 있는 2가지 블록이 제공된다.



#### 주의할 점

1. **초기화 블록이지 선언 블록이 아니다!** 
   - 선언은 바깥에서 해 주어야 하고, 내부에서 선언했을 때는 로컬 변수로 취급된다.
2. 한 순서의 초기화가 다 끝나야지 다음 단계의 초기화가 실행된다.
   - 모든 변수에 기본값이 할당된 후, 명시적 초기화가 들어가고, 모든 명시적 초기화가 끝난 후 블록 초기화가 들어간다.

3. 같은 순서에 있는 선언 및 초기화는 코드 위에서 아래로 순차적으로 수행된다.

   

#### 1. 인스턴스 초기화 블록

- 인스턴스 변수의 초기화에 사용할 수 있다.
- **객체를 생성 할 때마다 수행된다.**
- **일반적으로 생성자를 사용하기 때문에 잘 사용되지 않는다.**
- **생성자보다 인스턴스 초기화 블록이 먼저 수행된다.**
  - 초기화 순서는 기본값 => 명시적 초기화 => 블럭 초기화=> 생성자 실행 순서이다

```java
public class Test {
    
    {
        // 인스턴스 초기화 블록
    }
}
```



#### 2. static 초기화 블록

- **static 변수의 초기화 및 프로그램 시작시 초기화 작업이 필요한 경우에 사용한다.**
- 프로그램 시작 시 단 한번 수행된다.
- static 변수들이 생성된 후에 바로 static 초기화 블록이 static 변수들을 초기화한다.
- 초기화 순서는 기본값 => 명시적 초기화 => 블록 초기화 순서이다.

```java
public class Test {
    static {
        // static 초기화 블록
    }
}
```



3. 아래 코드에서의 초기화 블록 순서

   - static 변수 => static 초기화 블록 => 인스턴스가 생성될 때마다 (instance 변수 => instance 초기화 블록 => instance 생성자)

   - 단, 모든 경우에서 저런 건 아니다.
     - static 변수 초기화 중 인스턴스가 생성될 경우에는 순서가 달라질 수 있다.

```java
package counter;

public class Counter {
	
	public static void main(String[] args) {
		
		Block myInst = new Block();
		Block myInst2 = new Block();
		
	}
}


class Block {
	
	static String staticVal = "static 변수! =>"; 
	
	// static 초기화 블록
	static {
		System.out.println(staticVal);
		System.out.println("static 초기화 블록! =>");
	}
	
	String instVal = "인스턴스 변수!";
	// 인스턴스 초기화 블록
	{
		System.out.println(instVal);
		System.out.println("인스턴스 초기화 블록! =>");
	}
	
	public Block () {
		System.out.println("인스턴스 생성자! => ");
	}

	
}
```



### 4. 싱글톤 디자인 패턴

단 하나의 인스턴스만을 생성하기 위한 패턴이다.

다음 step으로 구현한다.

1. 외부에서 객체를 생성하지 못하도록 생성자의 접근 지정자를 private으로 지정한다.
   - private 지정자는 같은 클래스 내부에서만 접근 가능하게 한다.
2. 한 번은 생성해야 하기 때문에 자신의 클래스에서 객체생성 코드를 사용한다. static 지정자를 사용하여 프로그램 실행시 단 한번 생성된다.

특정 클래스의 참조값을 얻을 때, new를 사용하지 않고 다음과 같은 구조로 사용하면 싱글톤 디자인 패턴이 적용된 코드라고 생각할 수 있다.

`클래스명 변수 = 클래스명.메서드();`

대표적으로, 캘린더 인스턴스가 있다.

```java
package bank;

public class Bankmain {

	public static void main(String[] args) {
		
		Bank myBank = Bank.getBank();				// 인스턴스의 참조값을 얻기
		System.out.println(myBank.getName());		// 얻은 참조값 사용
		
	}
}


package bank;

public class Bank {
	private static Bank b = new Bank("신한은행");			// static 변수에 인스턴스를 할당 => 실행될 때 단 하나의 인스턴스만 생성
	
	String name;										// 인스턴스 변수: 은행이름
	
	private Bank(String name) { this.name = name; }		// 생성자
	
	public static Bank getBank() {						// 단 하나 생성된 인스턴스를 갖다 써야 하니까, b를 반환 
		return b;
	}
	
	public String getName() {							// 은행 이름을 불러오기 위한 메서드
		return name;
	}
}

```



#### 참고: Static 인스턴스 변수의 생성 순서

static변수와 static 초기화 블럭 static 메서드 등의 선언이 끝나야지만 인스턴스가 생성 가능한 것이 **아니다.**

싱글톤 패턴에서 볼 수 있듯이, static 변수 선언 중에도 인스턴스는 선언과 할당이 가능하다.

다만, 해당 인스턴스를 생성하기 전에 명시적으로 초기화된 static변수들만 정상적으로 출력하고, 이외에는 기본값을 출력한다.

이유는 선언 => 기본값 초기화 => 명시적 변수 초기화 => 블록 초기화 => 생성자 코드 실행으로 순차적으로 수행되기 때문이다.

즉, static 변수에 생성자를 통해 인스턴스가 할당되면, 아직 명시적으로 할당되지 않은 static 변수 및 static 블록 내부의 변수들은 기본값으로 초기화가 되어 있는 상태이므로, 그렇게 출력된다.

- 두번 출력 (1. 클래스가 로드될 때 static 변수인 myBlock에 인스턴스 생성 및 할당, 2, myInst에 인스턴스 생성 및 할당)되는데,  처음에는 staticVal2에 null이 출력되고, 이후에는 정상 출력된다.

```java
package counter;

public class Counter {
	
	public static void main(String[] args) {
		
		Block myInst = new Block();
		
	}
}


class Block {
	
	static String staticVal1 = "인스턴스 생성 이전에 선언된 static 변수"; 	
	static Block myBlock = new Block();
	static String staticVal2 = "인스턴스 생성 이후에 선언된 static 변수"; 	
	
	String instVal = "인스턴스 변수!";
	
	public Block () {
		
		System.out.println("인스턴스 생성자 실행! ");
		
		System.out.println("인스턴스 생성 이전에 선언된 static 변수 => 정상 출력 ");
		System.out.println(staticVal1);
		
		System.out.println("인스턴스 생성 이전에 선언된 static 변수: 처음에는 null 출력 ");
		System.out.println(staticVal2);
	}

	
}
```

- 얘도 두번 출력

```java
package counter;

public class Counter {
	
	public static void main(String[] args) {
		
		Block myInst = new Block();
		
	}
}


class Block {
	
	static String staticBlockVal1;
	static String staticBlockVal2;


	static {
		staticBlockVal1 = "스태틱 블록 내부, 인스턴스 생성 이전에 선언된 static 변수";
		Block myInnerBlock = new Block();
		staticBlockVal2 = "스태틱 블록 내부, 인스턴스 생성 이전에 선언된 static 변수";
	}

	
	public Block () {

		System.out.println(staticBlockVal1);
		
		System.out.println(staticBlockVal2);
	}
}
```



### 5. static import

static으로 정의된, 클래스 변수와 클래스 메서드를 사용할 때는 객체를 생성하지 않고 클래스명으로 접근한다.

`클래스명.메서드명();`

`클래스명.변수명;`

이때 매번 **클래스명을 사용하지 않고**, **변수와 메서드명만으로 접근할 수 있는 방법**이다.

코드는 간결해지지만 가독성이 떨어지기 때문에 잘 사용되지 않고 안드로이드 개발시 주로 사용된다.

```java
package static_import;
import static java.lang.Math.PI;
import static java.lang.Integer.parseInt;

public class myStaticImport {

	public static void main(String[] args) {
		
		System.out.println(Math.PI);
		System.out.println(Integer.parseInt("3"));
		
		// 동일
		System.out.println(PI);
		System.out.println(parseInt("3"));
	}
}
```

## IX. final 키워드

**변경되는 것이 마지막 이라는 의미로 사용된다.**

**즉, 금지의 의미이다.** 

final 키워드를 사용하면 다음과 같은 특징을 갖는다.

1. **클래스에 사용하면 상속이 불가능**하다. 대표적인 클래스가 java.lang.Math 클래스이다.

2. 변수에 사용하면 **값 변경**이 **불가능**하다.
   - 따라서 상수가 되며, 변수와 구분하기 위해 대문자로 표현한다.
   - C에서의 const 키워드와 비슷하다.
   - 상수의 일반적인 표현식
     - `public static final datatype myConst = value;`
     - public static을 사용하여, 외부에서 **객체 생성 없이 접근**할 수 있도록 함

​	3. 메서드에 사용하면 **오버라이딩이 불가능**하다.

```java
package myfinal;


final class A {
	
}

// class AA extends A {} => 클래스 상속 불가능

class B {
	public final void print () {
		
	}
}

class BB extends B {
//	public void print() {} => 메서드 오버라이딩 불가능
}

class C {
	public static final int myConst = 3; // but 값 변경 불가
	
}

public class MyFinal {
	public static void main(String[] args) {

		System.out.println(C.myConst);	// 외부 접근 가능
		
	}

}

```



## X. Varargs

- 근본적으로, 메서드 및 생성자 호출시 인자의 개수는 반드시 일치해야 한다.

- 그래서 가변적으로 인자의 개수를 주기 위해서 `...`를 사용한다.

- 가변 인자의 데이터형은 **하나로 일치**해야 한다
- 대표적으로 `printf`메서드가 이를 사용한다.

- 형식
  - `지정자 리턴타입 서드명(데이터형 ...변수명) {}`

```java
package myVarArgs;

import java.util.Arrays;

public class Varargs {

	public static void main(String[] args) {
		MyClass mc = new MyClass();
		
		mc.myIntArgs(1, 2, 3);
		mc.myStringArgs("너희", "어머니", "잘계시니?");
	}

}

class MyClass {

	public void myIntArgs(int ...x) {	
		System.out.println(Arrays.toString(x));		// 가변 인자는 배열 형태로 받는다.
		for (int i=0; i < x.length; i++) {
			System.out.println(x[i]);		
		}
	}
	
	public void myStringArgs(String ...x) {	
		System.out.println(Arrays.toString(x));		// 가변 인자는 배열 형태로 받는다.
	}
}


```



## XI. 배열로 객체 관리

- 말 그대로, 배열로 객체를 관리한다.
- 엄밀히 말하면, 인스턴스를 관리하는 것이다.
- 배열에 인스턴스 주소를 저장하고, 이를 갖다 쓴다.
- 형식
  - `Classname [] classArr = new Classname[n]`
- 3가지 방법

```java
package myVarArgs;

import java.util.Arrays;

public class Varargs {

	public static void main(String[] args) {
		
		// 방법 1.
		MyClass[] myArr1 = new MyClass[3]; 	// MyClass 배열 생성
		
		myArr1[0] = new MyClass("마굿간");	// 초기화 
		myArr1[1] = new MyClass("주유소");
		myArr1[2] = new MyClass("회사건물");	
		
		// 방법 2.
		MyClass[] myArr2 = {
				new MyClass("학원"),
				new MyClass("학교"),
				new MyClass("동물원"),
		};
		
		// 방법 3.
		MyClass[] myArr3 = new MyClass[] {
				new MyClass("게임"),
				new MyClass("하고"),
				new MyClass("있네"),
		};
	}	

}

class MyClass {
	
	String name;
	
	public MyClass (String name) {
		this.name = name;
	}
	
	public String getMyName () {
		return this.name;
	}
}


```

## XII. Method Area 정리

Java 8 버전 이전 기준으로, 메서드 Area에 저장되는 정보는 다음과 같다.

1. 클래스
2. static
   - main 메서드 등
3. method
   - 일반 인스턴스 method 등
4. 상수(리터럴)
