# 포인터 심화

## 1. 배열 이름 포인터로서 쓰기

- 포인터의 이름은, 배열의 첫 번째 원소를 가리키는 포인터로 사용될 수 있다.
  - 즉, `matrix[r][c]`에서 matrix는 matrix[0]을 가리키는 포인터(즉 `&matrix[0]`와 같다.)이고, `matrix[0]`는 `matrix[0][0]`을 가리키는 포인터이다.
  - **단, 두 가지의 경우는 배열의 첫 번째 원소가 아니라 해당 배열을 가리킨다.**
    1. **sizeof() 연산자와 함께 쓰이는 경우, 해당 배열 자체의 size를 반환.**
    2. **&연산자와 같이 쓰이는 경우, 해당 배열 자체를 의미**
  - 여기서 원소란, 가장 작은 단위의 원소가 아닌 한 차원 아래의 원소, 이를테면 2차원 행렬에서의 행을 말한다.

```c
#include <stdio.h>

int main() {

	char arr[3][3];

	printf("3x3 배열의 시작위치: %p\n",arr);
	printf("배열의 이름 - 첫 번째 원소(행)에 + 1: %p\n", arr + 1);
	printf("배열 전체의 크기만큼 더하기: %p", &arr + 1);

	return 0;
}
```

- **즉, `a[i] => *(a+i)`이고, 실제로 컴파일러 내부에서 해당 변환을 수행한다.** 

```c
// 첨자 변환 실험

#include <stdio.h>

int main() {
	int array[3][4];

	// *(array+2) ==  &*(*(array+2) + 0)
	printf("%d", array[2] == &array[2][0]);

	// **(array+2) == *(*(array+2)+0)
	printf("%d", *array[2] == array[2][0]);
}
```

- 배열의 이름을 포인터로 쓰는 것처럼, 포인터에 첨자를 붙여 사용할 수도 있다.

```c
int array[5] = {1, 2, 3, 4, 5};
int *ptr;
ptr = array;
printf("%d", ptr[2]); // == *(ptr+2) == 3
```

### 포인터와 배열명

앞에서, 배열의 이름은 해당 배열 원소의 첫 번째를 가리키는 포인터로 사용될 수 있다고 하였다. 이 말은, 이를테면 2차원 배열에서 배열명은 첫 번째 행을 가리키고, 배열명[행]은 첫 번째 열 - (1,1)을 가리킨다는 것을 의미한다.

이는 다음과 같이 증명할 수 있다.

```c
int *ptr;
p = &arr[i][j]; // i행 j열을 가리키는 포인터
// p = &*(arr[i]+j)
// j에 0을 대입
// &*(arr[i])
// &과 *는 서로 상쇄됨
p = arr[i]
```

또, 앞에서 말했듯이 &를 붙이면 첫 번째 원소가 아닌 배열 자체를 가리키게 된다.



## 2. 배열 포인터 변수

다차원 배열 포인터 변수란, 다차원 배열에서 특정 단위 - 이를테면 면 혹은 행에 접근할 때 사용하는 포인터 변수를 말한다.

- 포인터 자체의 크기는 4byte 혹은 8byte이다.
- 이를테면, 2차원 배열의 행에 접근하고 싶을 때, 해당 포인터가 몇 byte씩 건너뛰어야 각 행에 접근할 수 있는지 컴퓨터는 파악이 가능하다.
  - 예를들어 char 4 X 4 배열은 메모리에 일직선으로 저장되므로, 각 행에 접근하기 위해서는 4씩 건너뛰어 접근해야 한다.
- 따라서 2차원 배열 포인터에는 열이 들어가야 하고, 3차원 배열 포인터에는 행과 열이 들어가야 한다.

```c
#include <stdio.h>

int main() {
	int array[4][4][4];
	
	int *ptr; // 1차원 배열 포인터
	int (*ptr2)[4]; // 2차원
	int (*ptr3)[4][4]; // 3차원
	
	printf("%d, %d, %d, %d, %d, %d", 
		sizeof(ptr), sizeof(ptr2), sizeof(ptr3), sizeof(*ptr), sizeof(*ptr2), sizeof(*ptr3)); // 4, 4, 4, 4, 16, 64
}
```

- 배열 포인터 변수에 포인터 넣기
  - 배열 포인터 변수에 포인터를 넣을 때는, 포인터 형식을 맞춰 주어야 한다.
  - 이는 단순히 int형 같은 의미일 뿐 아니라, 해당 포인터에 배열의 열 크기를 정확히 맞춰서 넣어 주어야 한다는 것을 의미한다.


```c
#include <stdio.h>

int main() {
	int array[3][4][5] = { 0 };
	
	// 1차원 배열 포인터 변수
	int *ptr1;
	// 1차원 배열 포인터에 저장 => 배열변수는 해당 배열의 첫 번쨰 원소를 의미 => 배열의 첫 번째 원소 즉 3면 4행 1열의 주소를 저장
	ptr1 = array[2][3];
	// 아니면 & 연산자를 붙여 직접 넣어주기 가능 => 3면 4행 1열의 주소를 저장
	ptr1 = &array[2][3][0];

	// 2차원 배열 포인터 변수
	int (*ptr2)[5];
	ptr2 = array[2]; // 2차원 배열 포인터에 저장 => 배열의 첫 번째 원소 즉 3면 1행을 가리킴
	ptr2 = &array[2][0]; // & 연산자를 통해 2차원 배열 포인터에 저장 => 배열의 첫 번째 원소 즉 3면 1행을 가리킴


	puts("===============================================================");

	int array2[3][4] = { 0 }; // 2차원 배열 선언

	int(*ptr3)[3];
	int(*ptr4)[4];

	ptr3 = array2; // 컴파일 에러 => array2는 열크기가 4인데 ptr3는 3임

	// 아래 두 방법과 같이 할당이 정확함
	ptr4 = array2;
	ptr4 = &array2[3];
}
```

- 아래는 전혀 문제가 없다.

```c
#include <stdio.h>

int main() {
	int array[3][4] = { 0 };

	int (*ptr)[4]; // 행을 가리키는 포인터

	ptr = array; // array == &array[0] 이므로
}
```



## 3. 이중 포인터를 이용한 배열 원소 접근

- **다차원 배열 포인터 변수에 *를 붙이면, 해당 포인터 내부의 첫 번째 원소를 가리키는 포인터로 전환된다.**
  - **포인터이므로, 포인터 연산이 가능하다**.
  - 즉, **이차원 배열 포인터 변수**에서 첫번째 행, 첫 번째 열의 값에 접근하려면, `**`를 붙이면 된다.
- 이차원 배열의 첨자를 포인터 연산식으로 변형하면 다음과 같다.
  - `ptr[i][j] == *(*(ptr+i)+j)`
- 증명은 다음과 같다.

```c
#include <stdio.h>

int main() {
    int count[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };

    int(*ptr)[4]; // 2차원 배열

    int i, j;

    // 증명
    ptr = count;
    // ptr == count ==  &count[0]
    // *ptr == *(&count[0]) == count[0] == &count[0][0] // 첫 번째 행, 첫 번째 열의 포인터

    // 따라서, 아래와 같은 식이 성립된다.
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            //아래 두 식은 같다.
            printf("%p, %d == ", ptr[0] + j, ptr[0][j]);
            printf("%p, %d\t", *ptr +j, *(*ptr + j));
        }
        ptr++; // 행을 하나씩 증가
        puts("");
    }

}
```



## 4. 포인터 배열

- 포인터 배열은, 포인터를 담고 있는 배열이다.
- 배열의 각 원소 크기는, 포인터를 담고 있으므로 4 or 8이다
- 예를 들어, 문자열 포인터 배열이 있다.
  - 문자열의 시작 주소를 담고 있는 배열이다
  - 문자열 리터럴은 첫 번째 원소를 가리키는 포인터를 반환한다.
    - 일반 문자 배열을 할당할 때 처럼이다.



## 5. 이중 포인터

- 이중 포인터는, 특정 자료형을 가리키는 포인터를 가리키는 포인터를 말한다.

- 이중 포인터, 삼중 포인터는, 선언할 때 만큼 `*`를 붙이면 값에 접근한다고 생각하면 된다.
  - `int **ptr;`은, 값에 접근하려면 `**ptr`

- 문자열 포인터 배열에 접근할 때는, 이중 포인터를 사용한다.

```c
// 이중 포인터
#include <stdio.h>

void funcA(char **ptr);


int main() {
	char *ptr[] = { "kingdom test", "Advance C programming", // 해당 배열의 원소는, 리터럴의 첫 번째 글자를 가리키는 포인터
	"C++ Programming", "one two three", "multi compus",
	"seoul 서울시 강남구 양재동 100번지",
	"busan 부산시 해운대구 해운대동 바다 2번지", NULL }; // 마지막에 NULL 포인터

	funcA(ptr); // 포인터 배열을 인자로 전달할 때, 매개변수는 반드시 이중포인터로 받아야 한다.
				// kingdom test를 가리키는 포인터


	return 0;
}


// ptr의 문자열을 출력
// 단일 포인터를 주면, 1바이트씩 늘어난다. => 해당 포인터를 가리키는 포인터로 사이즈를 주어야 4바이트씩 늘어난다.
// strlen 사용하지 말고 직접 conunt해서 뒤에 숫자 표시

void funcA(char **ptr) {
	/*
		// ptr은 kingdom test를 가리키는 포인터
		// *를 달면 k를 가리키는 포인터
		// **를 달면 k 값을 출력
	*/
	char *ptr2;
	int cnt = 0;

	while (*ptr) {
		printf("%p: ", *ptr);
		ptr2 = *ptr;
		while (*ptr2) {
			cnt++;
			ptr2++;
		}
		printf("%u, %u: %s, 길이: %d \n", ptr, *ptr, *ptr, cnt);
		ptr++;
		cnt = 0;
	}
}


```



## 6. 제네릭 함수 : void형 포인터

### 1. 포인터 형변환

일반 변수도 cast연산자를 통해 형변환을 하듯이, 포인터도 마찬가지로 cast연산자로 형변환을 할 수 있다.

- `(자료형 *) 포인터`

단, 포인터 형변환을 해도 포인터의 크기는 그냥 4 or 8이다.

- 그냥 포인터를 담고 있기 때문이다.
- 여기서 값을 뽑아내야 가리키는 변수의 변한 크기가 나온다.

```c
// 포인터 형변환
#include <stdio.h>
int main()
{
	char ch='A';
	int num=10;
	double dnum=3.5;
	char *ptr=&ch;

	printf("&ch: %p, ptr: %p \n", &ch, ptr);
	printf("sizeof(ch): %d, sizeof(ptr): %d \n", 
										sizeof(ch), sizeof(ptr));
	printf("sizeof(&ch): %d, sizeof(*ptr): %d \n",
										sizeof(&ch), sizeof(*ptr));

	printf("\nsizeof(ptr): %d \n", sizeof(ptr) );
	printf("sizeof((int *)ptr): %d \n", sizeof((int *)ptr) ); // 포인터 형변환 문법
	printf("sizeof((double *)ptr): %d \n", sizeof((double *)ptr) ); // 포인터를 형변환해도, 포인터는 주소이기 때문에 4byte

	printf("\nsizeof(*ptr): %d \n", sizeof(*ptr) );
	printf("sizeof(*(int *)ptr): %d \n", sizeof(*(int *)ptr) );
	printf("sizeof(*(double *)ptr): %d \n", sizeof(*(double *)ptr) ); // 해당 포인터로 값을 뽑아내면 해당 크기만큼 뽑아냄
	return 0 ;
}


```



### 2. void형 포인터

- C언어 표준에서는 NULL 포인터는 아무것도 가리키지 않는 포인터를 의미한다.
- 이는, 어떤 것이든 가리킬 수 있는 포인터, 참조할 대상체가 정해져 있지 않은 포인터이다.
- void 포인터 변수를 사용하여 값을 참조할 때는 **캐스트 연산자를 사용하여 포인터 자료형을 명시한 후** 참조해야 한다.
  - **즉, void형 포인터가 나오면, 포인터 형변환이 들어간다고 생각하면 된다**
- 사용
  - `void *ptr;`

- 사용처
  - 런타임 중(실행 중) 주소 타입이 다양한 주소가 들어올 때(int형, char 형 등) 

```c
#include <stdio.h>

int main() {
	char ch = 'A';
	int num = 100;
	double dnum = 5.6;
	
    // void형 포인터 => 함수의 매개변수로 설정하면, 타입에 구애받지 않는다 => fwrite, fread에서 이렇게 사용;
	void *ptr; 

	printf("ptr: sizeof : %d \n", sizeof(ptr));

	ptr = &ch;

	printf("inside:  %c", *(char*)ptr); // char * 연산자를 사용하여 포인터 자료형(char *)을 명시

	return 0;
}
```

### 3. 제네릭 함수

- 일반화 프로그래밍(generic programming)은 자료형을 일반화 하는 것을 의미한다.
- 즉 데이터 형식에 의존하지 않고, 하나의 로직에서 여러 다른 데이터 타입들을 처리하는 기술에 중점을 두어 재사용성을 높일 수 있는 프로그래밍 방식이다.
- **이때 자료형에 대한 제약없이 사용할 수 있는 함수를 제네릭 함수라고 부른다.**
  - C++의 핵심!
- 변경 전

```c
// dataSwap.c

#include <stdio.h>

void swap(void *source, void *target, int size);

int main() {
	short int x = 100, y = 200;

	int n1 = 500, n2 = 900;
	
	double d1 = 1.1, d2 = 5.9;
    
	char names[2][20] = { "kim ??", "lee ??" };
	
    // 자료형마다 함수를 만들어 주어야 하는 불편함
	swap(&x, &y, sizeof(x));
	// swap(&n1, &n2, sizeof(int));
	// swap(&d1, &d2, sizeof(double));
	// swap(names[0], names[1], sizeof(names[0]));


	printf("x: %hd, y: %hd \n", x, y);
	printf("n1: %d, n2: %d \n", n1, n2);
	printf("d1: %lf, d2: %lf \n", d1, d2);
	printf("%s, %s\n", names[0], names[1]);


	return 0;
}

void swap(int *a, int*b) {
	int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
};
```

- 제네릭 함수로 변경 후

```c
// dataSwap.c

#include <stdio.h>

void swap(void *source, void *target, int size);

int main() {
	short int x = 100, y = 200;

	int n1 = 500, n2 = 900;
	
	double d1 = 1.1, d2 = 5.9;
	char names[2][20] = { "kim ??", "lee ??" };
	
	swap(&x, &y, sizeof(x));
	swap(&n1, &n2, sizeof(int));
	swap(&d1, &d2, sizeof(double));
	swap(names[0], names[1], sizeof(names[0]));


	printf("x: %hd, y: %hd \n", x, y);
	printf("n1: %d, n2: %d \n", n1, n2);
	printf("d1: %lf, d2: %lf \n", d1, d2);
	printf("%s, %s\n", names[0], names[1]);


	return 0;
}

// Generic Function(자료형에 구애받지 않고 하나의 로직으로 여러 데이터를 처리하는 함수)
void swap(void *source, void *target, int size) { // 객체지향에서는, 함수 중복정의 가능 => 매개변수까지 같아야 같은 함수라고 판단.
	
	char tmp, i;

	//void형 포인터는 ++이 안 된다
	for (i = 0; i < size; i++) {
		tmp = *((char *)source+i);
		*((char *)source+i) = *((char *)target+i);
		*((char *)target+i) = tmp;
	}

};
```



## 7. 함수 포인터

함수 포인터 변수란 포인터 변수가 함수의 주소를 저장하여, 포인터 변수를 통해 함수를 호출하게 하는 것이다.

함수명은 원래 포인터가 아니지만, 문맥에 따라 pointer로 converted(decay)되며 함수가 저장된 메모리 주소를 나타내게 된다.

- **함수 포인터 변수는 스택 영역에 저장**되며, 코드 영역의 함수 주소를 저장한다.

**해당 포인터 변수의 형식은, 할당될 함수에게 맞춰 주어야 한다**

### 참고

> (*변수명)이 오면 둘 중에 하나이다
>
> 1. 뒤에 ()가 오면 함수 포인터 변수
>    - int (*ptr)[3]
>
> 2. 뒤에 []가 오면 배열 포인터 변수
>    - int (*ptr)(int a);

- 형식
  - `자료형 (*변수명)(인자리스트);`

```c
#include <stdio.h>

void myFunc(int *ptr);

int main() {
    void (*funcPtr)(char *); // 함수 포인터 변수
    
    funcPtr = myFunc;
    
    (*funcPtr)("multi campus");		// 함수호출 => 원래는 얘만 됐었음 => 더 바람직함
	funcPtr("Advanced C Programming");	// 나중에 얘도 되게 됨 
	
    return 0;
}

void myFunc(int *ptr) {

	printf("myFunc() : %p, %s \n", ptr, ptr);

}
```

- 응용

```c
#include <stdio.h>

int add(int x, int y);
int sub(int x, int y);
int mul(int x, int y);
int div(int x, int y);

int main()
{
	 int (*ptrArr[4])(int x, int y) = { add, sub, mul, div };
	// int (*ptrArr[4])(int , int ); // 함수 포인터 배열
	int menu_no, num1, num2, result;
	char op[4] = { '+', '-', '*', '/' };
	char tmp[10];

//	ptrArr[0] = add;

   while(1)
	{
	    printf("\n1. add\n");
   		printf("2. subtract\n");
   		printf("3. multiply\n");
   		printf("4. divide\n");
   		printf("5. end\n");
		do {
   			printf("\nSelect(1-5) --> ");
   			scanf("%d",&menu_no); //1, 3, abc
        } while(menu_no< 0 || menu_no>5);

		   if(menu_no==5)
				break;

   		printf("Input the two numbers --> ");
   		scanf("%d %d%*c",&num1, &num2); //100 30[enter]

		result = ptrArr[menu_no-1](num1, num2);
   		printf(" %d %c %d = %d \n", num1, op[menu_no-1], num2, result);
    }

	return 0;
}

int add(int x, int y)
{
	return x+y;
}

int sub(int x, int y)
{
	return x-y;
}

int mul(int x, int y)
{
	return x*y;
}

int div(int x, int y)
{
	if(y==0)
	{
		printf("can not divide by 0\n");
		return -1;
	}
	return x/y;
}

```



## 8. Enum Pointer

```c
//enumPointerEx.c
#include <stdio.h>
#include <string.h>

typedef enum Season // enum은 정수형 상수의 집합 => datatype 5.c
{
    SPRING,
    SUMMER,
    FALL,
    WINTER,
} SEASON;

char *GetSeason(enum Season season) // 문자열 리터럴(첫 번째 문자를 가리키는 포인터)를 반환하므로
{
    if (season == SPRING) {
        return "봄"; // 문자열 상수는, 데이터 세그먼트의 read only 영역에 들어간다 => 따라서, 너무 많이 쓰면 공간이 부족해질 수 있다.
    }
    else if (season == SUMMER) {
        return "여름";
    }
    else if (season == 2) {
        return "가을";
    }
    else if (season == 3) {
        return "겨울";
    }
}

/* => 교수님 방식
char *GetSeason(enum Season season) // 문자열 리터럴(첫 번째 문자를 가리키는 포인터)를 반환하므로
{
    static char ret[100];

    if (season == SPRING) {
        strcpy(ret, "봄");
    }
    else if (season == SUMMER) {
        strcpy(ret, "여름");
    }
    else if (season == 2) {
        strcpy(ret, "가을");
    }
    else if (season == 3) {
        strcpy(ret, "겨울");
    }

    return ret;
}
*/

int main()
{
    char *ptr;
    enum Season season = SUMMER;
    ptr = GetSeason(season);


    printf("선택한 계절: %s \n", ptr);
    return 0;
}
```

