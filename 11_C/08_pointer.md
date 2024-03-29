# 포인터

현대 컴퓨터에서 메모리는 바이트 단위로 나누어지고, 각 바이트마다 고유의 주소를 가지고 있다.

변수 선언되면 각각 최소 1바이트 이상을 메모리상에서 차지하고 있다.

이때, 변수가 차지하는 **첫 번째 바이트의 주소**를 변수의 주소라고 부른다.

이때 이 주소는 정수가 아니기 때문에 **일반적인 정수형 변수에 보관이 불가능**하고 **포인터 변수**에 저장해야만 한다.

- 예를 들어, 출력시에도 특정 변수의 포인터(주소값)이나  포인터 변수를 출력할때는 `%p`형태변환자를 사용한다.

i 변수의 주소를 포인터 편수 p에 저장한다면, p는 i를 가리킨다라고 표현한다.

**즉, 포인터란 주소이고, 포인터 변수는 주소를 저장하는 변수이다.**

- 포인터
  - 실행중인 프로세스의 임의의 주소



## 1. 포인터의 선언

- 포인터 이름 앞에 별표를 붙여 선언한다.
- `int *p;`
  - p가 int형을 갖는 **개체**를 가리키는 포인터 변수라는 의미
  - p가 변수가 아닌 메모리 공간을 가리킬 수 있기 때문에 개체라고 표현
- 포인터 변수는 다른 변수들과 함께 선언문에 등장이 가능하다.
  - `int i, j, a[10], b[10], *p1, *p2;`
- **포인터 변수는 선언 시 자료형과 관계없이 동일한 크기를 할당받는다.**
  - 각 운영체제 별 최대 지정가능한 메모리 주소가 다른데, 주소는 항상 최대로 찍어야 하기 때문이다.
  - **sizeof()** 연산자로 포인터 변수를 찍어보면 알 수 있다(포인터 상수 X)
  - 32비트 운영체제
    - 4바이트

  - 64비트 운영체제
    - 8바이트
- 포인터는 다른 포인터를 가리킬 수도 있다.
- 포인터 변수의 자료형은 자신이 참조할 데이터의 자료형과 같아야 한다.
  - **왜냐하면, 포인터 변수가 가리키는 번지로 가서 데이터를 읽어올 때, 해당 자료형이 가지는 바이트만큼 읽어오기 때문이다.**
    - 예를 들어 32비트 운영체제에서 `int *p`면, 해당 메모리 주소로 가서 **4바이트**를 읽어오라는 것이다.
  - 각각 정수형, 부동소수점형, 문자형을 가리킴
    - `int *p;`
    - `double *q;`
    - `char *r;`
- visual studio에서는, 가독성을 위해 포인터 변수를 선언할 때 *의 위치를 앞으로 바꾼다.
  - `int* p;`

## 2. 주소 및 참조 연산자

### 1. 주소 연산자 &

포인터 변수에 특정 변수의 주소를 할당할 때, 그 **할당할 주소를 반환**하는 연산자 &를 사용한다.

- `&`
  - 변수의 주소를 찾기 위해 사용한다.
  - `&myVar`
    - myVar의 메모리주소
- 포인터 변수는 사용하기 전에 반드시 값을 할당해야 한다.

```c
#include <stdio.h>

int main() {
	int myVar;
	
	int* myPointer;

	// 어떤 주소를 포인터 변수에 할당
	myPointer = &myVar;

	// 이렇게도 가능
	int myVar2;
	int* myPointer2 = &myVar2;

	// 아래 방식도 가능하다.
	int myVar3, * myPointer3 = &myVar3;

	return 0;
}
```

### 2. 참조 연산자 *

- `*`
  - 간접 참조(indirection) 연산자
    - 변수명으로 참조하는 건 직접참조
  - 포인터가 특정 개체를 가리키고 있을 때, 참조 연산자를 통해 **가리키는 개체에 접근 가능**
  - **`*` 연산자를 사용하면 해당 포인터의 자료형을 참고하여 해당 자료형만큼의 byte를 읽어온다.**

```c
	int myVar = 3;
	int* myPointer;
	myPointer = &myVar;

	// 해당 포인터 변수가 가리키는 주소의 값을 출력
	printf("%d", *myPointer);
```

- *는 &의 수학적인 역이다.

```c
	// &는 *의 역이라고 생각하면 된다.
	// &로 해당 변수의 포인터(주소)를 추출 => *로 해당 포인터가 가리키는 참조값을 추출
	int j;
	int i = 3;

	// j = i와 동일하다
	j = *&i;
	printf("%d", j);
```

- **포인터 변수 p가 i를 가리킨다면, *p는 i에 대한 가명(alias)이다.**
  - 즉 `p* == i`이다
    - 실제 출력도 참으로 나온다.
  - *p는 i와 같은 값을 가진다.
  - *p의 값을 변경하면 i의 값도 변경된다.

```c
#include <stdio.h>

int main() {
	int* p;
	int i = 3;
	p = &i;

	printf("%d \n", *p);// 3

	*p = 5;
	printf("%d \n", i); // 5

	return 0;
}
```

- 포인터 실험

```c
#include <stdio.h>

int main() {
	int i = 3;
	int* p;
	int* q;

	// 포인터 실험
	p = &i;
	q = &p;

	// 아래 두 출력은 동일하다
	// 다만 &i를 십진수로 찍어서 오류가 있긴 하다
	// *q == p의 값 == i의 주소
	printf("%d \n", &i);// 
	printf("%d \n", *q);// 

	return 0;
}
```

### 3. 주의점

1. **초기화하지 않은 포인터 변수에 참조 연산자를 사용해서 값을 참조하거나, 값을 할당하는 것은 위험하다.**

```c
int* p;
printf("%d", *p); // 프로그램이 멈추거나 쓰레기 값 반환

int* p;
*p = 1; // 만약 p가 유효한 메모리 주소를 갖고 있다면 해당 주소의 자료가 망가진다.

// 따라서, 아래와 같이 NULL로 초기화하고, 조건문을 줘서 변수를 가리키거나 할당하자.
int *ptr = NULL, num;

if (ptr == NULL) {
    ptr = &num;
} else {
    ptr = 100;
}
```

2. 포인터 변수의 자료형을 자신이 참조할 변수와 같은 자료형으로 선언하라
3. 일반 변수는 간접참조 할 수 없다
4. 포인터 연산은 정수형 연산식을 사용한다.

## 3. 포인터 할당

c는 형만 같다면 할당 연산자가 포인터를 복사하는 것을 허용한다.

어떤 개체는 무한개의 포인터 변수가 동시에 가리킬 수 있다.

```c
int i, j;
int *p, *q;

// 포인터 할당 == 주소 할당
p = &i;

// 또 다른 포인터 할당 => i의 주소를 p에서 q로 복사
q = p;
```

p나 q에 새로운 값을 할당하면 i의 값도 달라진다.

```c
// q나 p에 새로운 값을 할당하면 i의 값도 달라진다.
*p = 1;
printf("%d \n", i); // 1

*q = 2;
printf("%d \n", i); // 2
```

아래는 포인터 할당이 아니므로 주의

```c
// 이것은 포인터 할당이 아니라 값을 넣는 것이므로 주의.
*p = *q;
```



## 4. 포인터 연산

`+`, `-`, `++`, `--`



## 5. 인자로서의 포인터

포인터는 여러 가지 용도에 사용되는데, 대표적으로 함수 인자로서 사용된다.

함수의 인자로 값을 전달하는 것을 값에 의한 호출(Call by value)라고 부르고, 함수로 주소를 전달하는 것을 참조에 의한 호출(Call by Reference)라고 부른다.

함수의 인자로 값이 전달된다면 함수 안에서 매개변수의 값이 변경되어도 원본 인자의 값은 변경되지 않지만 포인터가 전달된다면 이를 변경할 수 있다. 

- 포인터 매개변수

함수 매개변수로 포인터를 지정하는 방법은 여러 가지가 있다.

`myFunc(int *param)`

`myFunc(int param[])`

`myFunc(int param[10])`

위 세가지 방법은 **인자로 포인터를 전달한다는 정확히 동일한 의미**이고, 차이점은 가독성의 차이밖에 없다.



## 6. 포인터 상수화

- 어떤 함수 안에서, 포인터의 **값**을 변경하는 것을 막고 싶을때, parameter에 const를 붙여 포인터를 상수화한다.
  - 단, 값을 바꾸는 것을 막는 것이기 때문에, pointer를 바꾸는 것과 참조하는 것은 허용된다.

```c
#include <stdio.h>

void showMsg1(char* ptr);
void showMsg2(const char* ptr);

int main(void) 
{
	char c1[6] = "hello";

	c1[0] = 'H';

	printf("c1: %s \n", c1);

	char* c2 = "hello";

	//*(c2 + 0) = 'H'; // 문자열 상수 => 데이터 세그먼트에 있어서 수정 불가

	printf("c2: %s \n", c2);

	puts("=====================================================");

	char msg[20] = "kingdom";

	showMsg1(msg);
	printf("msg: %s \n", msg);

	showMsg2(msg);
	printf("msg: %s \n", msg);

	return 0;
}

void showMsg1(char* ptr) 
{
	*ptr = 'K';
}

void showMsg2(const char* ptr) // 포인터 상수화 
// 해당 함수 안에서는 const가 붙은 포인터를 사용하여 포인터가 참조하는 데이터 수정 불가능
{	
	char a = 'a';
	printf("%c \n", *ptr);
	//*ptr = 'k'; // 에러뜸
	ptr = &a; // 주소는 바꿀 수 있다 => 값을 못 바꾸는것
	printf("%c \n", a);
}
```



### 배열변수는 포인터 상수이지만 sizeof 연산자에서 길이를 반환

포인터 상수이든 포인터 변수이든, 원칙적으로 sizeof를 찍어보았을 때는 포인터 자체의 크기를 반환하는 것이 맞다.

**하지만 배열변수의 경우 포인터 상수임에도 불구하고, sizeof를 찍었을 때 컴파일러는 해당 배열의 전체 크기를 반환한다!** 

[참고](https://www.quora.com/What-is-the-difference-between-a-constant-pointer-and-an-array-name-in-C)

```c
int arr[10] = {0,1,2,3,4,5,6,7,8,9}; 
 
//let us find the size of the array - 
printf("Size: %d\n", sizeof(arr)); //this prints 40; assuming size of int is 4 
 
//let me create a constant pointer now 
int* const ptr = arr; //has to be initialized during declaration 
 
printf("Size: %d\n", sizeof(ptr)); //this prints 4; assuming size of int is 4 
```



## 참고: 포인터 상수 vs 상수 포인터

> 배열 변수 다루다가 두 개념이 헷갈려서 정리
>
> 인터넷 상에서는 상수 포인터, 포인터 상수, 상수를 가리키는 포인터라는 말이 마구 섞여서 사용되고 있으니 영어로 보시는 것이 정확합니다.
>
> 용어의 기준은 http://www.tcpschool.com/c/c_pointerArray_relation 요기로 했습니다.
>
> 오개념이 있으면 수정 바랍니다.

1. 포인터 상수

   - **constant pointer**

     - **배열변수는 포인터 상수(교과서 389p) 할때의 그 포인터 상수**

     - 상수인 포인터 == 상수인 주소 == 변하지 않는 주소

     - 요런 형태

       - `int * const CPointer = &a;`

       - `int myArray[10] = {0};`

     - **포인터(주소)는 변하게 하지 못하지만 값은 바꿀 수 있음**
       - 즉, 포인터 상수는 포인터 연산이 불가능함
     

```c
#include <stdio.h>

int main(void)
{
    int var1 = 0, var2 = 0;

    int* const ptr = &var1; // 포인터 상수 선언

    *ptr = 1; // 포인터가 가리키는 변수의 값은 잘 바뀜
    printf("%d \n", *ptr);

    // ptr = &var2; // 여기서 에러 발생 => 포인터는 바꾸지 못한다
    printf("%p \n", ptr);

    puts("==============================================");

    int myArray[10] = { 0 }; // 배열변수 선언

    myArray[0] = 1; // 배열 내부의 값은 잘 바뀜
    printf("%d", myArray[0]);

    // myArray++; // 여기서 에러 발생 => 포인터는 바꾸지 못함
    printf("%p \n", myArray);
    return 0;
}
```



2. 상수 포인터
   - **Pointer to Constant**
     - 포인터는 포인터인데 가리키는 놈이 상수, 즉 변하지 못함
     - 상수만 가리킨다는 의미가 아님, 해당 포인터를 통해 **값을** 변경시키지 못한다는 뜻
       - **내가 상수만 바라보니 내가 바라보는 동안 너는 변하지 않는 상수여야 한다.**
   - **우리가 함수 인자로 포인터를 넘길 때, 해당 값을 변경하지 못하게 할 때 쓰는 바로 그 포인터**(교과서 403p)
   - 요런 형태
     - `const int *myPointer = 10;` 
   - 교수님께서 설명해 주셨듯이, 그런데 포인터 자체는 옮길 수 있지만 해당 포인터를 통해 **값을** 변경하는 것을 방지하려고 쓴다

```c
#include <stdio.h>

int main(void)
{
    int a = 10, b = 20; // 변수 선언

    const int* myPointer; // 상수 포인터 선언

    myPointer = &a; // 포인터는 자유롭게 변경 가능

    printf("변수 a의 값: %d == 메모리 주소 %p의 값: %d \n", a, myPointer, *myPointer);

    myPointer = &b; // 포인터는 자유롭게 변경 가능
    printf("변수 b의 값: %d == 메모리 주소 %p의 값: %d \n", b, myPointer, *myPointer);

    //*myPointer = 100; // 에러 => 해당 포인터를 통해 값 변경 불가능

    b = 30; // 해당 변수 자체는 상수화된 변수가 아니므로 값 변경 

    printf("변수 b의 값: %d == 메모리 주소 %p의 값: %d \n", b, myPointer, *myPointer);

    return 0;
}
```



3. 상수 포인터 상수는 너무 변태같으니 제외



## 한글 포인터 접근 시 주의점

- 일반적으로 한글은 아스키 코드가 아니기 때문에 2 byte를 차지한다.

- `*` 연산자를 사용하면 해당 포인터의 자료형을 참고하여 해당 자료형만큼의 byte를 읽어온다.
- **여기서 문제가 생기는데, 문자 배열은 char로 선언하기 때문에, 포인터로 접근할 때 각 원소가 차지하는 메모리 단위를 1Byte로 읽는다.**
- **즉, 한글 문자열은 포인터 단위로 수정, 접근하는 것이 힘들다**

```c
char s3[20] = "앙냥냥";

printf("%s", s3); // 정상 출력

printf("%c", s3[0]); // 문자 배열에서 각 인덱스는 1바이트씩을 의미하기에 쓰레기 값이 찍힌다
```

