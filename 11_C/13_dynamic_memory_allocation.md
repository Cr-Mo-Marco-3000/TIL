# 동적 메모리 할당

메모리는 4개의 세그먼트로 이루어지는데, 각각의 특징은 다음과 같다.

1. 스택 세그먼트의 변수

- 함수 호출시 할당 / 함수 종료시 소멸

- 여기 선언된 배열은 고정 크기 배열



2. 데이터 세그먼트의 변수

- 프로그램 실행시 할당, 프로그램 종료시 소멸

- 즉, 프로그램의 처음부터 끝까지 남아있다.

- 여기 선언된 배열도 고정크기 배열이다.
- => 원칙적으로, 실행문이 오기 전에 선언문이 와야 하며, 이 규칙은 C99버전 이전에는 에러였다.



3. 그리고, 개발자가 직접 메모리 할당과 반납을 할 수 있는 힙 세그먼트이다.

- 예상보다 적은 크기의 데이터가 메모리에 들어가는 경우, 고정된 배열 크기만큼 할당받는 것은 낭비이므로, 동적 할당이 필요하다.



## 1. 힙 세그먼트

힙 세그먼트의 메모리 할당은 메모리 할당이 컴파일 타임이 아닌 런타임에서 이루어진다.

해당 세그먼트에는 **포인터 변수**를 통해서만 접근 가능하며, 헤더파일 <stdlib.h>에 선언된 함수들을 가지고 조작 및 접근 한다.

- 함수를 통해 메모리 할당 요청을 하고, 사용하지 않을 때는 반납할 수 있다.
- 메모리 사용하다 공간이 부족하거나 남을 때는 더 큰, 더 작은 크기로 재할당도 가능(원본 데이터 유지)

연결 리스트와 큐, 스택, 이진 트리 등 자료구조를 체계적이고 논리적으로 구현하는 알고리즘에서 일반적으로 사용되는 영역이다.

힙 세그먼트는 스택과 마찬가지로 재활용 영역이다. 즉, 처음 할당받으면 쓰레기 값이 있다.



### 참고: 객체지향 프로그래밍에서의 힙 세그먼트

객체지향 프로그래밍에서는, 객체는 힙 영역에, 객체 변수는 스택 영역에 만들어져서, 객체 변수를 사용할 때 힙 영역음 참조하게 됨;



## 2. 동적 할당 함수의 종류

총 4가지의 함수를 사용한다.

1. malloc
2. calloc
3. realloc
4. free

각 함수는 모두 void형 포인터를 반환하는 제너릭 함수이므로, 선언 및 정의할 때 포인터 형변환이 필수이다!

### 1. malloc()

- 함수 원형(size_t는 unsigned int를 뜻함)
  - `void *malloc(size_t size)`

- 예시
  - `ptr = (int *)malloc(100);`
- 설명
  - 인수로 크기(byte단위)를 넘겨주면 운영체제에서는 비어 있는 영역을 할당해 그 **시작 주소를 반환**
  - 만약 함수가 메모리를 할당받을 수 없는 상태라면 NULL 값을 반환

### 2. calloc()

- 함수 원형
  - `void *malloc(size_t num_elements, size_t element_size);`
- 예시
  - `ptr = (int *)calloc(10, sizeof(int));`
- 설명
  - **size_t num_elements * size_t element_size 만큼의 크기를 할당**하면서, **할당된 공간을 자동으로 0으로 초기화**
  - 사용 전 할당받은 메모리에 값을 저장하는 프로그램이라면 굳이 쓸 필요 없음

### 3. realloc()

- 함수 원형
  - `void *realloc(void *ptr, size_t size);`
- 예시
  - `ptr = (int *)calloc(ptr, 200);`
- 설명
  - 이미 할당되어 있는 영역을 다시 size만큼 재할당하며 새로운 영역의 시작 주소를 반환함
  - 만약 뒤쪽의 공간이 부족하다면, 새로운 넉넉한 공간을 찾아 할당한 뒤 기존 메모리의 내용 복사, 기존 메모리 반납
  - **즉, 메모리의 기존 데이터를 보장함**

### 4. free()

- 함수 원형
  - `void free(void *ptr);`
- 예시
  - `free(ptr);`
- 설명
  - free 함수의 인수는, 위의 세 함수의 호출에서 반환 받은 값, 즉 메모리 주소여아 함!
  - 이 함수는 할당 받은 영역을 해제하고, 이렇게 해제된 영역은 다른 동적 할당시 사용 가능
  - **할당된 공간 중 일부만 해제 불가능**

### 주의할 점

1. 힙 영역을 free()함수를 통해 해제하지 않으면, 프로세스가 끝나기 전까지 **할당된 상태로 남아있는다.**
   - 누군가가 해당 주소를 알고 있으면 사용이 가능하지만 만약 적절이 처리하지 않아 해당 주소를 잃어버리면, 해제가 힘들다.
     - **메모리 누수 발생**
2. 해제한 힙 영역의 주소를 free()로 다시 해제시도했을 경우, 프로세스가 죽어버린다.
   - 또한, 해제된 메모리에 함부로 접근했을 때는 오류가 발생할 수 있다.
3. 해제 후 할당되었던 포인터에 NULL포인터를 할당해서 오류를 방지하자
   - `ptr = NULL;`

#### 이중 구조체 포인터를 통한 접근

- 이중 구조체 포인터로 접근할 때, *p->member가 아니라, `(*p)->member`를 사용해야 한다.
  - 우선순위가 ->가 먼저이기 때문이다

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
	
	// malloc 성공하면 시작주소, 실패하면 NULL 포인터 반환
	char *ptr;

	while (1) {
		ptr = (char *)malloc(100); // 포인터와 같은 타입으로 캐스팅

		if (ptr == NULL) {
			perror("Error ");
			exit(1);
		}

		printf("input string ?\n");
		gets(ptr);

		if (!strcmp(ptr, "end")) {
			break;
		}

		printf("ptr: %p, %s\n", ptr, ptr);
		free(ptr);	// 해제한 힙 영역은, 재할당 가능 => 해제하지 않으면 함수가 끝나도 free를 만나기 전까지 남아있음
					// 누군가가 해당 주소를 알고 있다면, 계속 사용 가능 
					// => 그런데, 적절히 처리하지 않아 주소를 잃어버리면, 힙에는 남아 있더라도 해제가 힘들어, 메모리 누수가 발생!
	}					

	free(ptr);	// 괄호 안의 => 힙 영역의 주소를 해제 => ptr 자체는 함수가 끝낼때 해제
	ptr = NULL; // 안전하게, 해제한 주소를 처리
	// free(ptr);						// => 해제된 메모리를 적절하게 처리하지 않고 다시 해제하면 죽음
	// printf("ptr: %p, %s", ptr, ptr); // => 해제된 메모리에는 접근하면 안된다!
	
	
	return 0;
}
```

## 3. 메모리 누수

- 메모리 누수 현상은 컴퓨터 프로그램이 필요하지 않은 메모리를 계속 점유하고 있는 현상으로 할당된 메모리를 사용한 다음 반환하지 않는 것이다.
- 메모리 누수는 프로그램이 메모리를 할당 후, 해제하지 않음으로 시스템의 메모리를 고갈시키는 소프트웨어 오류로, 당장 프로그램이 비정상적으로 종료되지 않으나 메모리 누수가 누적되면 결국 메모리 부족으로 인한 프로그램의 비정상적인 종료를 유발한다.
- 동적 메모리 할당은, 반드시 확인 후 진행하는 것이 좋다.

### 참고: 여러 언어에서의 동적 할당

- C
  - 구조적인 programming
  - malloc으로 힙 영역 할당
- C++
  - 객체 지향 프로그래밍
  - new로 힙 영역 할당, delete로 삭제
    - 원래는 수동으로 해주어야함
    - 메모리를 수동으로 관리해주면, 성능상의 이점이 있으나 메모리 누수 발생 가능
  - 메모리 관리를 수월하게 하기 위한 라이브러리 존재
    - VLD
- JAVA, C#
  - 객체 지향 프로그래밍
  - delete를 대신 해 주는 가비지 콜렉터 내장
    - 메모리 누수가 발생하지 않는 대신, 즉시 지워지지 않는다.

### VLD를 이용한 메모리 누수 관리

- 한글이 있으면, 메모리 누수가 발생하는 위치를 줄로 찝어주지 못하는 오류가 발생하므로 주의

```c
#include <vld.h>
#include <stdio.h>
#include <stdlib.h>

int* funcA(int _numSz)
{
	//
	int *nPtr, i;

	nPtr = (int*)malloc(_numSz * sizeof(int));

	if (nPtr == NULL)
	{
		perror("funcA() Error : ");
		exit(1);
	}

	for (i = 0; i < _numSz; i++)
		*(nPtr + i) = 100 + i;

	return nPtr;
}

void funcB(char* msg)
{
	printf("msg : %s \n", msg);
}

int main()
{
	int numSz, * Ptr, i;

	printf("input Array Size ? ");
	scanf("%d", &numSz);

	Ptr = funcA(numSz);

	printf("\n동적할당 데이터\n");
	for (i = 0; i < numSz; i++)
		printf("%d, ", *(Ptr + i));

	printf("\n");

	funcB("다우기술");

	// free(Ptr); 해당 주석을 풀지 않으면 메모리 누수가 발생한다.

	return 0;
}

```





## 3. 구조체 포인터 동적 할당

- 힙 세그먼트는 포인터를 통해 조작할 수 밖에 없기 때문에, 구조체를 힙 세그먼트에서 이용하기 위해서는 구조체 포인터를 이용해야 한다.
  - 구조체 포인터 연산자 `->`이용

```c
// 구조체 포인터 empPtr 이용

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct EMP {
	char name[20];
	int salary;
	float height;
	char comAddr[50];
};

int main() {

	struct EMP *empPtr; // 구조체 포인터

	while (1) {
		empPtr = (struct EMP*)malloc(sizeof(struct EMP));

		if (empPtr == NULL) {
			perror("Error");
			exit(1);
		}

		// 데이터입력
		printf("이름? (입력 종료:end)\n");
		gets(empPtr->name);

		if (!strcmp(empPtr->name, "end")) { // 주소이므로 그대로 입력 가능
			break;
		}

		printf("연봉?\n");
		scanf("%d", &empPtr->salary);

		printf("키?\n");
		scanf("%f%*c", &empPtr->height);
		
		printf("주소?\n");
		gets(empPtr->comAddr);

		// 데이터 출력
		printf("이름: %s\n", empPtr->name);
		printf("연봉: %d\n", empPtr->salary);
		printf("키: %f\n", empPtr->height);
		printf("주소: %s\n", &empPtr->comAddr);
	}

	// 메모리해제
	free(empPtr);
	empPtr = NULL;
	return 0;
}
```



### 구조체 포인터 배열와 재할당

- 숫자를 받아, 해당 숫자만큼 포인터 배열에 저장한 후, 그 포인터 배열에 문자열을 할당한다.
- 문자열 추가시 숫자를 받아서, 해당 숫자만큼 realloc 한 뒤 저장

```c
// double_pointer1.c
#include <stdio.h>
#include <string.h>
int main()
{
	char **ptr, tmp[100];
	
	int x, y, i;
	
	printf("\n문자열의 수 ? ");
	scanf("%d%*c", &x); //3
	
	// 힙 세그먼트 어딘가에 12바이트를 할당한 뒤 
	ptr = (char **)malloc(x * sizeof(char *)); 
	if (ptr == NULL) {
		perror("Error");
		exit(1);
	}

	for (i = 0; i < x; i++)
	{
		printf("%d,input string ? ", i + 1);
		gets(tmp);
		*(ptr + i) = (char *)malloc(strlen(tmp) + 1); // (char *)malloc(strlen(tmp) + 1) : char * 형 포인터를 반환
		strcpy(*(ptr + i), tmp);
	}

	printf("\n문자열 출력\n");
	
	for (i = 0; i < x; i++)
		printf("%p, %s \n", *(ptr + i), *(ptr + i));
	
	puts("");
	puts("============================ 문자열 추가 ============================");
	puts("");

	printf("\n추가할 문자열의 수 ? ");
	scanf("%d%*c", &y); // 2

	ptr = (char **)realloc(ptr, (x + y) * sizeof(char *));
	if (ptr == NULL) {
		perror("Error");
		exit(1);
	}

	for (i = x; i < x + y ; i++)
	{
		printf("%d,input string ? ", i + 1);
		gets(tmp);
		*(ptr + i) = (char *)malloc(strlen(tmp) + 1); // (char *)malloc(strlen(tmp) + 1) : char 배열을 가리키는 포인터를 반환
		strcpy(*(ptr + i), tmp);
	}

	printf("\n문자열 출력\n");

	for (i = 0; i < x; i++)
		printf("%p, %s \n", *(ptr + i), *(ptr + i));

	puts("");


	for (i = 0; i < x + y; i++)
		free(ptr[i]);

	free(ptr);
	ptr = NULL;
	return 0;
}
```





## 4. 연결 리스트(Linked List)

자기참조 구조체를 사용해서 연결 리스트를 만든다.

**구조체를 사용해서 연결 리스트를 생성할 때는, 구조체 네임태그가 반드시 필요하다!**

- 네임태그가 구조체 내부 멤버 전에 작성되기 때문에, 이를 참조할 수 있는 것



### 1. 단일 연결 리스트

- 단방향으로만 순환 가능한 연결 리스트
- 일반적으로 연결 리스트의 노드에는 head(시작), tail(끝) 용어를 사용한다.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vld.h>

struct EMP {
	char name[20];
	int salary;
	float height;
	char comAddr[50];
	struct EMP *next; // 구조체 내부에 다음 노드의 포인터를 저장
};

int main() {
	struct EMP *head, *tail; // 연결 리스트의 시작, 끝을 저장할 포인터 변수
	struct EMP *empPtr, *x;  // 연결 리스트를 만들 때 활용할 포인터, 메모리 해제할 때 사용할 포인터.
	head = tail = NULL;      // 첫 번째 노드 생성 전에는 head와 tail이 모두 비어있으므로, 
							 // 이를 표시하기 위함 => 사실 head에만 붙여도 됨

	while (1) {

		// 노드 EMP의 크기만큼 동적 할당을 받은 후 구조체 포인터 반환
		// 노드마다 사이즈는 같지만 동적 할당된 메모리상의 위치는 제각각이다
		empPtr = (struct EMP *)malloc(sizeof(struct EMP));
		
		// 할당 실패시 에러 처리
		if (empPtr == NULL) {
			perror("Error");
			exit(1);
		}
		// 각 정보 입력받기 => 연봉과 신장의 경우에는 & 필요
		printf("이름 입력? - 종료: end\n");
		gets(empPtr->name);

		// 종료조건 만족시
		if (!strcmp(empPtr->name, "end")) {
			break;
		}

		printf("연봉 입력?\n");
		scanf("%d", &empPtr->salary);
		printf("신장 입력?\n");
		scanf("%f%*c", &empPtr->height);
		printf("주소 입력?\n");
		gets(empPtr->comAddr);

		// 새로운 노드를 만들기 전에는 지금 만든 노드(empPtr)가 마지막 노드이므로
		// 다음 노드가 없다는 의미로 NULL 포인터를 넣어 처리
		empPtr->next = NULL;

		if (head == NULL) {			// 기존에 시작 노드가 없으면
			head = tail = empPtr;	// 지금 만든 노드가 처음이자 끝 노드
		} else {
			tail->next = empPtr;	// 기존 최종 노드의 next에 새로 만든 노드를 저장 후
			tail = empPtr;			// 새로 만든 노드를 마지막 노드로 설정
		}
	}

	free(empPtr);					// 연결 리스트에 속하지 못한 불완전한 노드 해제

	/*
	출력
	*/
	puts("");
	printf("출력을 실행합니다.\n");
	puts("");
	empPtr = head;					// 리스트에 시작 노드를 넣는다.
	while (empPtr) {				// 마지막 노드까지 반복
		printf("이름: %s, 연봉: %d, 키: %.2f, 주소: %s\n",
			empPtr->name, empPtr->salary, empPtr->height, empPtr->comAddr);
		empPtr = empPtr->next;
	}

	/*
	해제
	*/
	puts("");
	printf("해제를 실행합니다.\n");
	puts("");
	empPtr = head;						// 리스트에 시작 노드를 넣는다.
	while (empPtr) {					// 마지막 노드까지 반복
		x = empPtr->next;
		free(empPtr);
		empPtr = x;
	}

	/*
	교수님 코드
	
	while (empPtr) {
		x = empPtr;
		empPtr = empPtr->next;
		free(x);
	}
	*/

	empPtr = NULL; // 눈 먼 free() 방지용

	
	return 0;
}
```



### 2. 이중 연결 리스트

- 아래 코드에서는 head, tail 대신 start, end를 쓰겠다.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vld.h>

struct EMP {
	char name[20];
	int salary;
	float height;
	char comAddr[50];
	struct EMP *next;	// 구조체 내부에 다음 노드의 포인터를 저장
	struct EMP *before;	// 구조체 내부에 이전 노드의 포인터를 저장
};

int main() {
	struct EMP *start, *end; // 연결 리스트의 시작, 끝을 저장할 포인터 변수
	struct EMP *empPtr, *x;  // 연결 리스트를 만들 때 활용할 포인터, 메모리 해제할 때 사용할 포인터.
	start = end = NULL;      // 첫 번째 노드 생성 전에는 start와 end가 모두 비어있으므로, 
							 // 이를 표시하기 위함 => 사실 start에만 붙여도 됨

	while (1) {

		// 노드 EMP의 크기만큼 동적 할당을 받은 후 구조체 포인터 반환
		// 노드마다 사이즈는 같지만 동적 할당된 메모리상의 위치는 제각각이다
		empPtr = (struct EMP *)malloc(sizeof(struct EMP));
		
		// 할당 실패시 에러 처리
		if (empPtr == NULL) {
			perror("Error");
			exit(1);
		}
		// 각 정보 입력받기 => 연봉과 신장의 경우에는 & 필요
		printf("이름 입력? - 종료: end\n");
		gets(empPtr->name);

		// 종료조건 만족시
		if (!strcmp(empPtr->name, "end")) {
			break;
		}

		printf("연봉 입력?\n");
		scanf("%d", &empPtr->salary);
		printf("신장 입력?\n");
		scanf("%f%*c", &empPtr->height);
		printf("주소 입력?\n");
		gets(empPtr->comAddr);

		// 새로운 노드를 만들기 전에는 지금 만든 노드(empPtr)가 마지막 노드이므로
		// 다음 노드가 없다는 의미로 NULL 포인터를 넣어 처리

		empPtr->next = NULL;
		empPtr->before = end;			// 위쪽에서 end에 NULL을 초기화시켜 주었으므로 시작노드에서는 NULL 할당
										// empPtr->before = NULL; => 교수님 코드
							
		if (start == NULL) {			// 기존에 시작 노드가 없으면
			start = end = empPtr;		// 지금 만든 노드가 처음이자 끝 노드
		} else {
			// empPtr->before = end;	//교수님 코드
			end->next = empPtr;			// 기존 최종 노드의 next에 새로 만든 노드를 저장 후
			end = empPtr;				// 새로 만든 노드를 마지막 노드로 설정
		}
	}

	free(empPtr);					// 연결 리스트에 속하지 못한 불완전한 노드 해제

	/*
	출력 (end => start)
	*/
	puts("");
	printf("출력을 실행합니다.\n");
	puts("");
	empPtr = end;					// 리스트에 마지막 노드를 넣는다.
	while (empPtr) {				// 시작 노드까지 반복
		printf("이름: %s, 연봉: %d, 키: %.2f, 주소: %s\n",
			empPtr->name, empPtr->salary, empPtr->height, empPtr->comAddr);
		empPtr = empPtr->before;
	}

	/*
	출력 (start => end)
	*/
	puts("");
	printf("출력을 실행합니다.\n");
	puts("");
	empPtr = start;					// 리스트에 마지막 노드를 넣는다.
	while (empPtr) {				// 시작 노드까지 반복
		printf("이름: %s, 연봉: %d, 키: %.2f, 주소: %s\n",
			empPtr->name, empPtr->salary, empPtr->height, empPtr->comAddr);
		empPtr = empPtr->next;
	}


	/*
	해제
	*/
	puts("");
	printf("해제를 실행합니다.\n");
	puts("");
	empPtr = start;						// 리스트에 시작 노드를 넣는다.
	while (empPtr) {					// 마지막 노드까지 반복
		x = empPtr->next;
		free(empPtr);
		empPtr = x;
	}

	/*
	교수님 코드
	
	while (empPtr) {
		x = empPtr;
		empPtr = empPtr->next;
		free(x);
	}
	*/

	empPtr = NULL; // 눈 먼 free() 방지용

	
	return 0;
}
```

### 3. 연결 리스트 노드 내부 문제점과 개선

- 노드 내부에 문자열이 있을 경우, 해당 영역이 길어졌을 때 이후 메모리 영역을 침범하는 일이 발생할 수 있다.
- 이럴 때를 대비해서 두 가지 방법이 있다.
  1. 버퍼를 만들어서 입력 크기를 제한하는 일반적인 방법
  2. 주소 같이 크기가 큰 문자열은, 자체적으로 힙 세그먼트에 할당한 후 구조체에는 그 포인터만 저장하는 방법
- 위 두 개를 같이 쓸 수도 있다.

```c
// 위의 단일 연결 리스트 코드와 같이 보자
// 주석이 달린 부분이 변화된 부분이다.

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vld.h>

struct EMP {
	char name[20];
	int salary;
	float height;
	char *comAddr;
	struct EMP *next;	
};

int main() {
	struct EMP *head, *tail; 
	struct EMP *empPtr, *x;  
	head = tail = NULL;     
							
	char tmp[250];			 // 문자열 처리를 위한 임시 문자배열

	while (1) {

		empPtr = (struct EMP *)malloc(sizeof(struct EMP));
		
		// 할당 실패시 에러 처리
		if (empPtr == NULL) {
			perror("Error");
			exit(1);
		}

		do {
			printf("이름 입력? : 최대 19자: 종료: end\n");
			gets(tmp);
		} while (strlen(tmp) >= sizeof(empPtr->name)); // 같아도 안된다. => 끝에 \0

		strcpy(empPtr->name, tmp);	// 조건 통과시 이름 저장

		// 종료조건 만족시 종료 
		// => 불완전한 구조체 메모리는 아래서 할당해제하므로 괜찮다.
		if (!strcmp(empPtr->name, "end")) {
			break;
		}

		printf("연봉 입력?\n");
		scanf("%d", &empPtr->salary);
		printf("신장 입력?\n");
		scanf("%f%*c", &empPtr->height);
		printf("주소 입력?\n");

		// address는 길이가 가변적이므로, 
		// 임시 배열에 저장해준 후 힙 영역에 동적할당한다
		gets(tmp);
		empPtr->comAddr = (char *)malloc(strlen(tmp) + 1);
		strcpy(empPtr->comAddr, tmp);

		empPtr->next = NULL;
							
		if (head == NULL) {			
			head = tail = empPtr;
		} else {
			tail->next = empPtr;		
			tail = empPtr;	
		}
	}

	free(empPtr);					

	puts("");
	printf("출력을 실행합니다.\n");
	puts("");
	empPtr = head;					// 리스트에 마지막 노드를 넣는다.
	while (empPtr) {				// 시작 노드까지 반복
		printf("이름: %s, 연봉: %d, 키: %.2f, 주소: %s\n",
			empPtr->name, empPtr->salary, empPtr->height, empPtr->comAddr);
		empPtr = empPtr->next;
	}


	/*
	해제
	*/
	puts("");
	printf("해제를 실행합니다.\n");
	puts("");

	empPtr = head;
	
	while (empPtr) {
		free(empPtr->comAddr);
		x = empPtr->next;
		free(empPtr);
		empPtr = x;

		/* 교수님 코드
		x = empPtr;
		empPtr = empPtr->next;
		free(x->comAddr);
		free(x);
		*/
	}

	empPtr = NULL; // 눈 먼 free() 방지용

	
	return 0;
}
```

### 4. 정렬된 연결 리스트

```c
#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

int node_insert();
void node_output();
void node_free();

typedef struct S {
	int value;
	struct S *next;
} node;

node *head; // head는 전역변수 => 나중에 출력이나 해제할 때, 처음 노드부터 쫘르륵 할 것이기 때문에 저장해 주어야 해요

int main()
{
	char ch;
	int stop = 0;

	head = NULL;

	do {
		printf("\n1) 레코드 입력 \n");
		printf("2) 레코드 출력 \n");
		printf("3) 종료 \n");
		printf("\n 선택하세요... ");
		ch = getchar();
		getchar();

		switch (ch)
		{
		case '1':node_insert();
			break;
		case '2': node_output();
			break;
		case '3': node_free();
			stop = 1;
		}
	} while (!stop);

	return 0;
}

int node_insert()
{
	node *temp, *prev, *newNode;
	int in_value; // 받는 값
					
	while (1)											 // 새로 입력될 값이 있으면 몇 번째 노드에 위치하는지 비교를 해야 합니다
	{
		temp = head;									 // 비교는 가장 작은 값을 담은 노드(head)부터 해야죠
		prev = NULL;									 // head는 가장 작은 노드(시작노드)니까 전 노드가 없어요

		printf("\ninput value ? (입력종료:-99999) ");
		scanf("%d%*c", &in_value);						 // 5, 10, 15, 3, 7 
		if (in_value == -99999)
			break;


		// 아래 반복문은, 새로 받은 값과 비교해서 1) 바로 작은 값을 갖는 노드의 주소와, 2) 바로 큰 값을 가진 다음 노드를 찾는 과정입니다.


		while (temp != NULL && temp->value < in_value)   // temp != NULL : temp가 NULL이면 첫 번째 입력받은 노드이므로 반복문을 돌릴 필요가 없어요
														 // 매 루프마다, 가장 작은 값이 들어간 상태인 head부터 temp에 넣고 비교합니다.
														 // temp->value < in_value : 새로 입력받은 값(in_value) 보다 temp값이 작으면
		{
			prev = temp;								 // 현재 temp는 prev에 넣고 => 즉, 현재 값보다 작은 값을 포함한 노드를 prev에 넣음
			temp = temp->next;							 // 한 단계 큰 노드로 확인하러 이동
		}


		// 위 반복이 끝나면 1) prev에는 현재 입력받은 값보다 한 단계 작은 값을 가진 node의 주소가 들어 있고, 2) temp에는 한 단계 큰 노드가 들어 있어요
		// 즉 ... -> prev -> 새로 입력받은 값(in_value에 저장) -> temp -> ... 순서로 논리상 정렬되어 있지만, 
		// 새로 입력받은 값은 아직 힙 세그먼트에 구조체가 만들어지지 않았고, 위 정보가 기존 구조체에도 바르게 저장되지 않은 상태예요


		newNode = (node *)malloc(sizeof(node));			 // 새로 입력받은 값을 넣을 공간을 할당받음
		if (newNode == NULL)							 // 정상 생성 확인용
			return false;

		newNode->value = in_value;						 // 새로 만든 노드에 값은 새로 받은 값을 집어넣고
		newNode->next = temp;							 // 한 단계 큰 노드(temp)를 새로운 노드의 다음 포인터 변수(next)에 넣어줌(만약 새 노드가 head라도 기존 head가 temp에 담겨 있어 괜찮다)
										
		if (prev == NULL)								 // 만약 노드가 지금까지 값들 중 가장 작은 값인 경우(위 루프를 돌았는데 prev(더 직전 작은 값을 가진 주소) 가 없네?)
			head = newNode;								 // 새로 생성된 노드를 머리(가장 작은 값 == 시작점)로 만듬
		else
			prev->next = newNode;						 // 이외의 경우(새로운 값이 중간에 들어가거나, 마지막인 경우) prev 노드의 다음 노드에 새로 생성된 노드를 집어넣음

	} //while (1) end

	return true;
}

void node_output()
{
	node *temp;
	int cn = 1;

	temp = head;

	while (temp)
	{
		printf("%d, value : %d \n", cn++, temp->value);
		temp = temp->next;
	}
}

void node_free()
{
	node *temp, *x;

	temp = head;

	while (temp)
	{
		x = temp;
		temp = temp->next;
		free(x);
	}
}
```

연결 리스트의 장단점

- 메모리를 미리 할당할 필요 없이
- 필요한 만큼 할당하고, 필요없을때 반납하면 된다.

단점

- 느리다(자료 5만개 => malloc 5만번)

## 5. 동적배열

동적배열의 장단점

- 장점

메모리 연속 할당으로 인해 pointer로 계속 레퍼런스 할 필요 없다.

malloc 횟수가 적어진다.

- 단점

일정 메모리를 미리 확보해야 한다.

최대크기 - 현재 차지하는 크기(줄어들지라도 최대크기만큼 할당)만큼의 메모리 낭비가 발생한다.

