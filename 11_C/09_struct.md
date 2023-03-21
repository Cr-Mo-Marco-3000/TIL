# 구조체

## I. 구조체란?

구조체란 관련이 있는 여러 데이터들을 하나의 자료형으로 만들어 사용하게 하는 것

즉 사용자 정의 자료형을 만드는 것이다.

이 때, 데이터들의 집합은 자료형에 구애받지 않는다.

1. 사용자 정의 자료형으로 변수 선언
2. 구조체 변수로 메모리 할당
3. 하나의 변수이름으로 여러 형의 데이터 제어 가능

### 1. 구조체의 선언과 메모리 할당

- 구조체는 멤버라고 하는 값들의 모임
- 구조체의 멤버들은 서로 다른 타입으로 구성될 수 있는 통합 자료형이다.
- 선언문 구성요소
  - struct
    - 구조체 자료형에 대한 선언임을 컴파일러에게 알림
  - 구조체 자료형명(tag_name)
    - 새로운 구조체 형에 대한 이름
    - 사용자가 지정
    - 일반적으로 대문자로 선언
  - 자료형 멤버N
    - 구조체를 구성하는 구성 요소들을 작성
    - `int no[6];` 등 일반적인 선언문의 구성을 따름
  - 반드시 세미콜론으로 끝나야 한다.

```c
struct 구조체자료형명 {
    자료형 멤버1;
    자료형 멤버2;
    자료형 멤버3;
    ...
};
```

- 구조체 자료형 선언이 끝나면 자료형을 이용할 구조체 변수명을 기술할 수 있다.

```c
struct 구조체자료형명 {
    자료형 멤버1;
    자료형 멤버2;
    자료형 멤버3;
    ...
} 변수명 = { a, b, c, ...};
```

- 구조체 변수는 멤버들이 메모리에 **차례대로 할당**된다.
- 구조체를 할당할 때는 **같은 데이터끼리, 작은 데이터를 앞부분에 할당**하는 것이 유리하다

#### 구조체의 크기와 멤버 접근

구조체 변수 자료형의 크기를 얻기 위해 `sizeof()` 연산자를 사용한다.

구조체는 멤버와 멤버 사이에 빈 공간을 포함할 수 있기 때문에 단순히 멤버들의 할당 메모리 합으로 이를 구하면 안되고 꼭 sizeof() 연산자를 사용해야 한다.

이렇게 빈 공간을 포함하는 이유는 운영체제가 메모리에서 값을 읽어올 때 각 멤버의 메모리 할당 크기만큼이 아니라 32bit 운영체제 기준 4바이트, 64bit 기준 8바이트씩 읽어오기 때문이다. [참고](https://blog.naver.com/sharonichoya/220495444611)

구조체의 멤버에 접근할 때는 `.`를 이용한다.

```c
#include <stdio.h>
#include <string.h>
int main(void) {

	struct EMPLOYEE 
	{
		char name[20]; // 멤버(Member)
		int salary;
		float height;
		char comAddr[60];
	} emp;  // 구조체 변수 선언 == 구조체 정의
    
	// 구조체 변수 선언 => 이후에는 이렇게 한번에 값을 넣어줄 수 없다.
	struct EMPLOYEE emp2 = { "김현영", 5000, 175, "서울시 관악구"};
	
    // 구조체 변수와 구조체 자료형의 크기는 같다.
	printf("%d, %d \n", sizeof(emp), sizeof(struct EMPLOYEE)); 
	
    // 구조체 멤버 연산자 . => 변수값에 접근
	printf("%p, %p \n", &emp, &emp.salary); 
	
    // 멤버에 접근 => 컴파일러에 따라 초기화 없어도 실행(쓰레기값)이 될 수 있다.
	printf("%s, %d, %.2f, %s \n", emp.name, emp.salary, emp.height, emp.comAddr); 

	printf("성명 ?");
	gets(emp.name);

	printf("월급 ?");
	scanf("%d%*c", &emp.salary);

	printf("키(신장) ?");
	scanf("%d%*c", &emp.height);

	printf("회사주소?");
	gets(emp.comAddr);


	printf("%s, %d, %.2f, %s \n",
		emp.name, emp.salary, emp.height, emp.comAddr);

	tmp = emp; // 구조체 변수는 자료가 아니라 값이기 때문에, 대입이 가능하다.
	return 0;
}
```

### 2. 구조체의 선언과 정의

**구조체를 선언**한다는 것은 사용자 정의 자료형을 만드는 것과 같다.

해당 자료형으로 **구조체 변수를 선언**할 때 메모리 할당이 이루어지고, 이를 **구조체를 정의**한다고 한다.

위의 코드블럭에서 볼 수 있듯이 선언과 정의는 따로, 혹은 동시에 할 수도 있다.

- 구조체 변수를 선언할 때 초기화를 할 수 있다.
  - 초기화 이후에는, 한번에 값을 넣지 못하고 각 멤버별로 값을 넣어주어야 한다.

#### 구조체의 전역선언

구조체를 특정 함수 안에서 선언하면 그 함수 내부에서밖에 사용이 불가능하므로, 일반 전역변수와는 다르게 일반적으로 구조체는 함수 밖에 전역으로 선언한다.

```c
#include <stdio.h>

// 일반적으로 자료형은 밖에 선언
typedef struct EMPLOYEE
{
	char name[20];
	int salary;
	float height;
	char comAddr[60];
} EMP;

int main(void) {
    EMP emp = { "angnyang", 20000, 189, "SEOULSI"}; // 초기화
    
    return 0;
}
```



#### typedef와 구조체 변수의 선언

키워드 typedef는 이미 존재하는 자료형에 새로운 이름을 붙여 간단한 자료형 이름으로 사용하고자 할 때 사용된다.

```c
// 새로운 자료형명 EMP로 재정의
struct EMPLOYEE {
		char name[20];
		int salary;
		float height;
		char comAddr[60];    
};

typedef struct EMPLOYEE EMP;

// 새로운 자료형명으로 구조체 변수 선언
EMP emp1;
```

구조체를 선언할 때(구조체 변수 선언 X) typedef를 붙여 구조체 자료형을 재정의 할 수 있다.

- 단 typedef를 붙여 구조체를 선언할 때, 구조체 선언문 바로 뒤의 단어는 구조체 변수 선언이 아니라 새로운 구조체 자료형명이다.

```c
typedef struct EMPLOYEE {
		char name[20];
		int salary;
		float height;
		char comAddr[60];    
} EMP;// 구조체 자료형명 EMP, 구조체 변수 아님!
```

- typedef가 붙어 있으면 struct 뒤의 자료형명은 생략이 가능하다.
  - **단 이때, 구조체 재정의를 위한 자료형명은 반드시 필요하다!!!**

```c
typedef struct { // 자료형명 생략 가능
		char name[20];
		int salary;
		float height;
		char comAddr[60];    
} EMP;// 얘는 반드시 필요!
```



### 3. 구조체 복사(대입)

- 구조체 변수는, 멤버들이 복잡한 구조를 갖더라도 변수로 취급된다.

  즉, 배열과는 달리 통째로 복사할 수 있다.

- 일반 변수처럼 바로 대입이 가능하다.

```c
#include <stdio.h>
#include <string.h>
int main(void) {

	typedef struct EMPLOYEE // EMPLOYEE: 구조체 자료형 => typedef 사용 시 생략 가능
	{
		char name[20]; // 멤버(Member)
		int salary;
		float height;
		char comAddr[60];
	} EMP;  // 세미콜론 필요

	struct EMPLOYEE emp = { "홍길동", 4500000, 175, "서울시 강남구" }; // 구조체 변수: emp
	EMP tmp;
	
	printf("%s, %d, %.2f, %s \n",
		emp.name, emp.salary, emp.height, emp.comAddr);
	
    tmp = emp; // 구조체 변수는 자료가 아니라 값이기 때문에, 대입이 가능하다.
    
    printf("%s, %d, %.2f, %s \n",
		tmp.name, tmp.salary, tmp.height, tmp.comAddr);
	return 0;
}
```



## II. 구조체를 함수에 전달 및 반환

구조체는 함수에 전달 및 반환될 수 있다.

구조체 변수를 반환값으로 쓰는 이유는, 반환값은 하나여야 하는데, 구조체 내부에 여러 개의 값을 넣어 전달할 수 있기 때문이다.

함수의 매개변수로 구조체 변수를 표기할 때

- `struct 자료형명 변수명`
- `재정의된자료형명 변수명`

함수의 반환형으로 구조체 변수를 표기할 때

- `struct 자료형명 함수명() {}`
- `재정의된자료형명 함수명 () {}`

```c
#include <stdio.h>
#include <string.h>


typedef struct EMPLOYEE
{
	char name[20];
	int salary;
	float height;
	char comAddr[60];
} EMP;

void funcA(struct EMPLOYEE emp);

struct EMPLOYEE funcB();

int main(void) {

	struct EMPLOYEE emp = { "홍길동", 4500000, 175, "서울시 강남구" };
	struct EMPLOYEE my;
	funcA(emp);
	my = funcB();
	return 0;
}

// 1. 구조체를 인자로 받는 함수
void funcA(struct EMPLOYEE emp) // void funcA(EMP emp)
{
	printf("%s, %d, %.2f, %s \n",
		emp.name, emp.salary, emp.height, emp.comAddr);

	return 0;
}

// 2. 구조체를 반환하는 함수
struct EMPLOYEE funcB() // EMP funcB()
{
	struct EMPLOYEE tmp;
	
	tmp.salary = 3700000, strcpy(tmp.name, "진달래"), tmp.height = 170, strcpy(tmp.comAddr, "경기도 양주시");
	// 한글은 2byte이므로, char에 넣을 수 없고 문자열로 넣어야 한다. 주의!

	printf("%s, %d, %.2f, %s \n",
		tmp.name, tmp.salary, tmp.height, tmp.comAddr);

	printf("%s, %d, %.2f, %s \n",
		tmp.name, tmp.salary, tmp.height, tmp.comAddr);
	
	return tmp;
}

```



