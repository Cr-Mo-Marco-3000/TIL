# 조건문과 반복문

## 1. 조건문

> 많은 부분이 C계열의 언어와 유사함으로, 기억해 둘 만한 부분만 서술한다.
>
> 제어문: 조건제어, 반복제어, 기타제어
> 조건제어: if, switch
> 반복제어: for, while, do-while
> 기타제어: break, continue, goto

### 1. if 조건문과 논리 연산자

```c
#include <stdio.h>

// 제어문: 조건제어, 반복제어, 기타제어
// 조건제어: if, switch
// 반복제어: for, while, do-while
// 기타제어: break, continue, goto

int main() {
	int num;
	
	printf("input number?");
	scanf("%d", &num);

	if (num >= 0) printf("%d, Positive \n", num); // 각 절에 명령이 하나씩일때는 {} 없이 이렇게도 실행 가능
	else printf("End. \n"); 

	if (num >= 0) { // 코드 블럭 {}을 만들고 나면, 그 블럭은 하나의 단위로 처리된다
		printf("%d, Positive. \n", num);
	}
	else {
		printf("End. \n");
	}

	return 0;
}


```

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
	
	int a;
	// 조건문에서의 논리 연산자 사용
	scanf("%d", &a);

	if (a > 100 || a < 0) {
		printf("점수가 너무 큽니다!");
		exit(1); // 프로그램 강제종료 => exit(0);는 프로그램 정상종료 == main함수의 return 0; stdlib.h로부터 인클루드
		printf("앙냥냥!");
	}

	if (a >= 10 && a <= 15) { // 논리곱
		printf("%d", a);
	}
	else {
		putchar(a);
		
	}	


	// 단축 평가 지원 => a가 15 이상이면 앞까지만 확인
	if (a >= 15 || a <= 10) {
		printf("bigger or smaller: %d", a);
	}
	else {
		printf("%d", a);
	}
	
	return 0;
}
```

### 2. switch문

- 일치하는지 여부만 판단하는 조건문
- 정수형 상수, 문자형 상수만 판단가능

```c
#include <stdio.h>

int main() {

    int input;

    printf("1 or 2 or 3 \n");

    scanf("%d", &input);

    switch (input) {
    case 1:
        printf("1");
        break;
    case 2:
        printf("2");
        break;
    case 3:
        printf("3");
        break;
    default: // if 문에서의 else와 같다.
        printf("이도 저도 아니네요")
        break;
    }

    return 0;
}


// 중간에 break가 없으면, 해당 case 아래부터 계속 실행된다
// 2를 입력했을 경우 2, 3 출력
int main() {

    int input;

    printf("1 or 2 or 3 \n");

    scanf("%d", &input);

    switch (input) {
    case 1:
        printf("1");
        break;
    case 2:
        printf("2");
    case 3:
        printf("3");
        break;
    }

    return 0;
}
```



## 2. 반복문

- 사용법은 아래와 같다
  - do-while문만 주의할것

- `{}` 블록으로 묶어주지 않으면 한 줄만 반복 가능하다.
- C99부터는 반복문 안에 변수 선언을 할 수가 있지만, C에서는 모든 변수를 블록 앞에 선언하도록 권장하므로 좋은 방법은 아니다.

```c
#include <stdio.h>

int main() {
	// for 문
	// js와는 다른 부분이, for 문에서도 i를 정의해 주어야 한다.
	// break;, continue; 사용 가능
	int i;
    // for (let i = 0; i < 5; i++) {  <= 이 방식도 가능하지만 권장하지 않음
	for (i = 0; i < 5; i++) {
		printf("%d \n", i);
	}

	// for 무한 반복
	// for (;;) {
	//	printf("%d \n", i);
	// }
    
    // 이렇게 한 쪽을 비워도 가능 => 위에 i가 선언되어 있기 때문
    for (;i <= 10;) {
        printf("%d \n", i);
    }

	printf("이제부터 와일이다! \n");

	// while문
	while (i <= 100) {
		printf("%d \n", i);
		i++;
	}
    
	// while문 무한루프
	//while (1) {
	//	printf("앙냥냥");
	//}

}
```

- do-while
  - 입력된 값을 검증할 때 많이 쓰임
  - 검사해서 맞으면 while문을 벗어나서 내려감


```c
	// do-while문
	// do-while은 처음 while 문을 검사하지 않고 do 안의 문을 실행한 후, while 조건에 따라 실행한다.
	// 주의할 점은, 다른 루프문과는 다르게 do-while문은 맨 뒤에 ;가 들어간다는 것이다.
	do {
		printf("지금부터 두와일 시작!");
		i--;

	} while (i >= 0);

```

- for문에서의 특수한 반복조건

```c
#include <stdio.h>

int main() {
	char msg[100];
	int number = 0, alpha = 0, special = 0, i;

	printf("문자열 입력? ");
	
	gets(msg); // C program is Fun !!!, Book Price: 25000[enter]

	for (i = 0; msg[i] != '\0'; i++) { // 비교 연산자가 아닌 반복조건
		if (msg[i] >= 48 && msg[i] <= 57) {
			number++;
		}
		else if (msg[i] >= 65 && msg[i] <= 90 || msg[i] >= 97 && msg[i] <= 122) {
			alpha++;
		}
		else {
			special++;
		}
	}
	printf("숫자: %d, 알파벳: %d, 특수문자 : %d \n", number, alpha, special);
	
	return 0;
}
```



## 3. 기타 제어문

### 1. goto

- 무조건 분기 명령
- goto 문을 만나면 프로그램의 실행 위치는 goto문에서 지정하는 레이블이 있는 곳으로 무조건 이동
- **goto문에서 사용한 label은 프로그램 함수의 어딘가에 반드시 존재해야 한다**
- 남용하지 말것!
  - 잦은 사용은 절차적 흐름을 방해한다.
- **다른 함수로는 goto는 이동될 수 없다!**
- 예시

```c
int main() {
	char ch;

	for (int i = 0; i <= 3; i++) {
		for (ch = 65; ch <= 90; ch++) {
			printf("%c ", ch);
			if (ch == 'H') {
				goto theEnd; // 레이블명Move 
			}
		}
	}
theEnd:
	printf("종료 \n");
	return 0;
}ㅇ
```



### 2. break, continue

- 다른 곳에서의 그것과 비슷하다.
