# 컴파일 과정





## 헤더파일

- `.h`확장자를 가진다.
- 헤더파일 내부에는 1. 다른 헤더파일의 include문(`#include <stdio.h>`) 2. 매크로 상수 선언문(`#define NAME VALUE`)등 **전처리기 지시문**과 3. 라이브러리 함수, 프로젝트 내부 여러 함수의 선언문(`int myFunc(int parameter1, ...);`)이 포함되어 있다.
  - 소스코드마다 공통되는 부분을 담고, 이를 include해서 사용한다.

- 헤더파일을 include하는 두 구문은 다음과 같다.
  1. `#include <stdio.h>`
     - 시스템 헤더파일
     - 헤더파일을 읽을 때 **시스템에서 제공하는 시스템 디렉토리 파일을 찾아 삽입시킨다.**
  2. `#include "myHeaderFile.h"`
     - 사용자 헤더파일
     - 응용프로그램의 작업대상 디렉토리에서 파일을 찾아 삽입시키라는 의미이다.
     - 만약 작업대상 디렉토리에 파일을 찾지 못할 경우 자동적으로 시스템 디렉토리를 검색한다.

- 헤더파일은 **소스파일마다 각자 삽입되어야 한다.**
  - 전처리 과정은 소스파일마다 각각 실행되기 때문이다.



- 전처리 과정 중, 헤더 파일이 삽입되고, 매크로 치환 및 적용된다.
  - 전처리기는 `#include` 구문을 만나면 해당하는 헤더파일을 찾아서 그 파일의 내용을 순차적으로 삽입한다.
- **현재 사용되지 않는 함수라도 쓸 가능성이 있다면 각 파일에 선언하거나 헤더파일에 넣어주는 것이 바람직하다**

- 사용예시

```c
/*
헤더파일 file.h
*/ 

// 전처리문(타 헤더파일 include문) 사용
#include <stdio.h>

// 매크로 상수 선언
#define AGE 25
#define SUDANG 300000

// 함수 선언 => 함수의 원형을 표시
void myName(void);
void myAge(void);

/*
file1.c
*/

#include "file.h" // 현재 작업대상 디렉토리 헤더파일 삽입 + 찾지 못할 경우 시스템 디렉토리를 검색

int salary = 45000000;

int main() {

	myName();
	myAge();
	mySal(); 

	return 0;
}

void myName(void) {
	printf("성명: %s \n", "홍길동");
}


void myAge(void) {
	printf("나이: %d \n", AGE);
}

/*
file2.c
*/

#include "file.h"

extern int salary;

char mySal() {
	printf("수당: %d \n", SUDANG);
	salary += SUDANG;
}
```

