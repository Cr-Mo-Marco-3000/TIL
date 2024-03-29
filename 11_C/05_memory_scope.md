

# 변수와 메모리, 스코프

## I. 변수와 메모리 저장위치

- 실행되어 메모리에 올라가 있는 프로그램을 프로세스라고 말한다. 

- 프로세스는 메모리의 영역을 할당 받아 실행되다가 프로그램이 종료되면 그 메모리 영역은 운영체제에게 제어권이 넘어가게 된다.

- 다음은 프로세스 실행 시 메모리의 서로 다른 영역에 데이터를 저장함을 보여준다.

  - 각 영역은, 물리적으로 구분된다.

- 메모리의 영역

  - 스택 세그먼트
    - 매번 초기화됨
    - **지역변수 할당**, 임시데이터 저장
  - 힙 세그먼트
    - 동적 메모리 할당 영역

  - 데이터 세그먼트
    - 한번만 초기화
    - **전역변수와 정적변수 할당**
  - 코드 세그먼트
    - 프로그램의 실행 코드
      - 즉, **함수 살당**

- 메모리에 할당된 변수의 주소를 확인하기 위해 주소연산자 `&`를 확인할 수 있다.



### 스택 세그먼트

> 지역변수 저장

- **재활용되는 공간**
  - 프로세스 실행 중 할당이 할당된 메모리를 반환하기도 함
- 지역변수는 생성과 소멸 반복
- 변수가 할당된 영역은 0을 보장받지 못함
  - 재활용 공간이므로 어떤 값이 남아 있을지 모름



### 힙 세그먼트

> 동적메모리 할당

- **재활용되는 공간**
- **포인터 사용**



### 데이터 세그먼트

> 전역변수, 정적변수 할당

- 재활용하지 않음
  - 프로세스가 끝나기 전까지 할당된 메모리를 반환하지 않음

- 한 번 변수가 할당되면 프로세스가 종료될 때까지 변수 영역은 **소멸되지 않음**
  - 변수에 할당된 값은 변경될 수 있음
- 프로그램이 종료될 때 까지 변수는 값 유지 가능
- 변수가 할당된 영역은 항상 0부터 시작함



### 코드 세그먼트

- 함수의 실행코드 적재
- **불변코드 영역**이라고 부름



#### 변수의 범위(scope)와 생존시간(life time)

- 스코프란 변수를 접근할 수 있는 영역, 즉 변수를 사용 가능한 영역
  - 가시성이라고도 함
- 생존시간은 변수가 메모리에 얼마나 오랫동안 남아있는지를 뜻함
- **변수의 범위와 생존시간**은 **선언위치**, 변수 선언 시 **형 수정자**에 따라 달라진다. 변수의 종류는 **지역변수, 전역변수, 정적변수**가 있다.



## II. 지역 변수 

- local variable

- 프로그램에서 가장 많이 사용되는 변수
- **기본적으로 블록 스코프**
  - 함수 내부의 블록도 각각의 스코프

- 함수 안에서 선언되고 함수 내에서 참조된다.
- **함수가 호출될 때 생성**되고, **함수가 종료될 때 소멸**된다
- **매개변수도 지역변수이다.**
  - 인자를 전달받는 매개변수 역시 자식함수에서 사용되는 지역변수이다.

```c
void func1() {
    int count = 100; // 지역변수 선언(함수 호출 시 할당)
    printf("count : %d \n", count);
} // 여기서 지역변수가 소멸된다(함수 종료)

void func2( int count ) { // 매개변수는 지역변수이다.
    printf("count : %d \n", count);
} // 함수 종료 시 매개변수(지역변수)도 소멸한다.
```



### 1) 함수 내부에 선언되며, 다른 함수에서 선언한 지역변수에 접근할 수 없다.

- 지역변수는 변수가 선언된 함수 안에서만 사용할 수 있다.

```c
#include <stdio.h>

void func(void);

int main(void) {
	int count = 50; // 지역변수
	
	func();

	return 0;
}

void func(void) {

	printf("사용 불가 : %d", count); // 오류 다른 함수의 지역변수를 사용할 수 없다.
	
	return;
}

```



### 2) 다른 함수에서 동일한 변수명을 사용할 수 있다.

- 지역변수는 같은 이름이라도 속한 함수가 다르면 다른 변수이다.
- 같은 이름이어도, 변수에 **할당되는 메모리 주소가 다르다**.

```c
#include <stdio.h>

void func(void);

int main(void) {
	int count = 50; // 지역변수
	
	printf("이 카운트는 아래와 다른 카운트입니다! 변수값: %d, 메모리 주소: %p \n", count, &count); // 서로 주소가 다르다.
	
	func();

	return 0;
}

void func(void) {

	int count = 150;
	
	printf("이 카운트는 위와 다른 카운트입니다! 변수값: %d, 메모리 주소: %p \n", count, &count); // 서로 주소가 다르다.
	
	return;
}

```

### 3) 지역변수를 인자로 전달하여 다른 함수에서 사용할 수 있다.

- 자식함수는 매개변수를 두어 받은 인자를 저장한다.
  - 모함수에서의 변수 메모리 주소와 매개변수의 주소는 다르다.
- **매개변수**는 함수 내에서만 사용하는 **지역변수**이다.



### 4) 함수 내부의 블록

- 함수 내에서 선언되는 지역변수는 블록의 시작부분에서 선언된다.
  - 만약 함수 내부에 다른 코드 블록이 있다면, 서로 다른 스코프를 갖되 내부 블록에서는 외부 블록의 변수를 참고할 수 있다.
  - 어떤 변수를 찾을 때는, 해당 블록에서 선언된 변수를 우선해서 찾는다.
- 각 함수는 블록이고, 함수 안에서 선언된 블록은 독립된 스코프를 갖는다.
  - 어떤 변수를 외부 스코프에서와 동일한 변수명으로 다시 선언하고 사용해도, 외부 스코프에는 영향을 미치지 않는다.
  - 내부 블록에서는 외부에서 선언된 값을 참고할 수 있지만, 외부 블록에서 내부 블록에 선언된 값을 찾는 것은 불가능하다. 


```c
// function_test.c
#include <stdio.h>

// 함수: 어떤일을 처리하는 논리적인 코드들의 집합

int main(void) {

	int a = 3;
	int i = 2;

	for (int i = 0; i <= 5; i++) { // inner i 재선언 => inner i 할당됨
        int a = 100; // a 재선언
		int c = 4; // c 선언
		printf("inner a: %d,	", a); 
		printf("inner i: %d \n", i);
	} // inner a, inner c, inner i 반납됨

	printf("outer a: %d,	", a);
	printf("outer i: %d \n", i);
	// printf("c 탐색 불가 : %d \n", c); 탐색 불가 


	return 0;
}

```



## III. 전역 변수

- global variable
- 전역변수는 **함수 외부**에 선언되며, 프로그램 전체에 걸쳐 유효하고 프로그램 어디에서나 전역변수를 사용할 수 있다.
- **즉, 모든 함수가 전역 변수를 공유한다.**
- 같은 이름의 전역 변수는, 한 프로그램에 하나만 존재해야 한다.
- Data Segment에 저장되기 때문에 프로세스가 종료될 때까지 데이터는 소멸되지 않는다.
  - **값은 바뀔 수 있지만, 할당된 메모리 영역이 반납되거나 바뀌지 않는다는 것을 의미함에 주의**
- 지역변수명과 전역변수명은 반드시 일치하지 않아도 된다.
  - 이름이 같다면 해당 스코프의 지역변수를 참조하게 된다.
  - **다만, 올바른 코딩 스타일이라고 할 수 없기에 다르게 지정하자.**
- **전역 변수를 쓰지 말자.**

```c
#include <stdio.h>

void func1(void);
void func2(void);

int salary = 2700000; // 전역변수 선언

int main(void){
    
    printf("main() salary: %d, memory: %p", salary, &salary); // 전역 변수 접근
    
    func1();
    
    printf("\nmain() salary: %d, memory: %p \n", salary, &salary); // 전역 변수의 값이 변경되어 있음

    func2();
    
    return 0;
}

void func1(void) {
    printf("main() salary: %d, memory: %p", salary, &salary); // 전역 변수 접근
    salary += 100000; // 전역 변수 수정
    
}

void func2(void) {
    int salary = -500;
    printf("감봉: %d, memory: %p", salary, &salary); // 로컬 변수 접근
    
}
```

## IV. 접근 수정자를 사용해 선언하는 변수

> extern, static, auto, register
>
> auto와 register 수정자는 잘 쓰이지 않는다.

### 1. auto 수정자

- 지역변수를 선언할 때 사용되는 수정자
- B언어와 호환성을 갖기 위해 제공되지만 현재는 거의 사용되지 않는다.
- `auto int num;`

### 2. register 수정자

- 변수를 메모리가 아닌 CPU 내의 register에 저장함을 의미한다.
- 따라서 변수를 메모리에 두는 것보다 더 빠른 연산과 접근을 보장받지만, CPU 내의 regiser의 수는 제한되므로 프로그래머에게 임의대로 원하는 만큼 사용될 수 없다.
- `register int num`



### 3. static 수정자

- 정적 변수를 선언할 때 사용한다.

- 전역 변수와는 달리, 정적 변수는 단 한 번 초기화된다.

  - 전역 변수는 함수가 실행되고 그 안에서 사용될 때 마다 초기화된다.

- 정적 변수의 특징

  1. 함수 안에 선언된 정적변수는 **데이터 세그먼트 영역에 저장**된다.
     - 따라서 프로세스가 끝날 때 소멸된다.

  2. 함수 안에 선언된 정적변수는 다른 함수에서 정적변수 사용 불가능
  3. 하나의 함수를 여러 번 호출 시 변수의 마지막 값을 지속적으로 사용가능
     - 해당 정적 변수를 초기화시키는 코드는, 다시 실행된 같은 함수 내부에서 만나면 무시된다.

```c
#include <stdio.h>

void funcD(void);
void funcE(void);

int main() {
	
	funcD();
	funcD();
	funcD();
	funcD();
	funcE();

	return 0;
}


void funcD(void) {
	
	int sum1 = 0; // 지역 변수 선언 => 함수 종료시 소멸
	static int sum2 = 1; // 정적 변수 선언 => 함수 종료시 소멸되지 않음
	printf("sum1: %d, sum2: %d \n", sum1 += 3, sum2+= 3);

}

void funcE(void) {

	// sum2++; 다른 함수에서 선언한 정적 변수 호출 불가
}
```



### 4. extern 수정자

- 전역변수는 관련된 여러 개의 파일에서 하나의 변수를 공유한다.
  - 따라서 구성하는 여러 파일에서 전역변수는 한번만 선언해야 한다.
- 컴파일러는 메모리 할당 크기를 위해 컴파일 시 모든 변수의 자료형과 크기를 알아야 한다.
  - 그런데 컴파일은, 각 `.c`파일마다 수행하기 때문에, 컴파일 단계에서는 다른 파일에 있는 전역변수를 인식할 수 없고, 컴파일 오류가 발생한다.
- 이 오류를 막기 위해 컴파일러에게 해당 이름을 가진 전역 변수가 다른 파일에 존재한다고 알려주는 수정자가 `extern`이다.

```c
// 첫 번째 파일 7_file1.c
#include <stdio.h>
#include "7_file.h" // 헤더파일 include => 컴파일 문서 참고

int salary = 2700000; // 전역변수 선언

int main() {
    
    mySalary(); // 7_file2.c에 존재하는 함수 => 함수 원형이 헤더파일에 존재
    
    printf("수령액: %d \n", salary);
    
    return 0;
}


// 두 번째 파일 7_file2.c

#include <stdio.h>
#include "7_file.h" // 헤더파일 include => 컴파일 문서 참고

// 해당 전역변수가 외부에서 선언된 전역변수임을 선언
// 이 코드가 없으면 컴파일러가 salary를 인식하지 못해 에러 발생

extern int salary;
void mySalary() {
    salary += SUDANG; // SUDANG은 헤더파일에 설정된 매크로상수이고, salary는 7_file1.c에 선언된 전역변수이다.
}
```

