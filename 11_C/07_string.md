# 문자열

- 1차원 배열의 대표
- C 내부에는 문자열 자료형이 **없음**
- **1차원 문자 배열**을 사용하여 문자열을 지원

- 문자열 상수는 **컴파일러에 의해 자동으로 NULL(`\0` == `0`)로 종료**된다.
  - null과 공백은 printf로 찍어보면 보이지 않는다.

- **즉, 문자열은 NULL 종료 문자배열(Null-terminated Character Array)이라고 정의할 수 있다.**



## 1. 문자 배열

- 1차원 문자배열을 이용하여 문자열 저장
- 문자배열 초기화 방법
  - **아래 str2와 str3에서, 작성하지 않은 배열의 인덱스 4부터는 `\0`으로 채워진다.**
  - 만약 할당하는 문자열 끝에 \n가 있으면 그 부분까지만 **문자열**로 인식한다.

```c
char str1[10]; // 문자배열, 10바이트로 10문자 저장 가능

char str2[10] = {'k', 'i', 'l', 'l'}; // 문자배열에 문자 상수 초기화

char str3[10] = "kill"; // 문자배열에 문자열 초기화
```

- 'a'와 "a"는 의미가 다르다
  - 'a'
    - 1바이트 할당
    - 문자상수
  - "a"
    - 문자열 상수
    - 2바이트('a' + \0) 할당
- **언사이즈드 배열로 문자배열을 선언할 수 있다.**
  - 단, 이 때는 {} 내부에 글자를 적어주는 식으로 초기화해주면 안 된다.
    - {}로 초기화하면 끝에 `\0`을 자동으로 붙여주지 않기 때문에 무조건 에러가 발생한다.
  - 문자배열을 초기화 할 때는 언사이즈드를 쓰지 말고 크기를 명확히, 또는 넉넉하게 해 주거나, 언사이즈드를 쓸거면 초기화시 큰따옴표를 이용합시다. 
    - 언사이즈드배열 사용시 할당된 메모리의 크기는 글자의 수 + 1이 된다(끝에 자동으로`\0` 추가)

```c
#include <stdio.h>

int main() {
	// 언사이즈드 배열로 문자열을 초기화할 때는 주의하세요!

	// 일반적으로 고정된 크기의 문자배열을 초기화할 때 문자열을 넣으면 뒤를 다 \0로 채워주기 때문에 두 방식이 동일하다고 생각하기 쉽습니다.
	// 근데 아니야 C 뻐큐머겅
 
	// 언사이즈드 + 큰따옴표로 초기화할 경우 끝에 \0을 자동으로 붙여주지만 
	// 언사이즈드 + {}로 초기화하면 끝에 \0가 붙지 않습니다!
	
	// 문자배열을 초기화 할 때는 언사이즈드를 쓰지 말고 크기를 명확히, 또는 넉넉하게 해 주거나, 
	// 언사이즈드를 쓸거면 초기화시 큰따옴표를 이용합시다. 

	// 얘는 4바이트 배열에 'k', 'i', 'l', 'l' 저장 => 출력시 \0가 자동으로 붙지 않아서 에러가 뜸

	char str2[] = { 'k', 'i', 'l', 'l' }; 
	printf("오류야 떠라!: %s, %d \n", str2, sizeof(str2)); // 오류, 4

	char str3[] = "kill"; // 얘는 뒤에 자동으로 \0를 붙여줘서 5바이트를 먹음
	printf("정상출력: %s, %d", str3, sizeof(str3)); // 정상출력, 5

	return 0;
}
```



## 2. 문자열 입력 함수

### 1. gets(문자배열)

- <stdio.h> 헤더파일 필요
- 문자열을 입력받아 문자배열에 저장
  - 인덱스 표시 없이 문자배열의 이름으로 함수 호출
  - 해당 배열의 시작주소부터 문자열이 할당
- 형식
  - `gets(문자배열명)`

```c
#include <stdio.h>

int main() {
    char name[20];
    char telno[15];
    char comAddr[50];
    
    printf("배열의 시작주소: %p, %p, %p \n", &name, &telno, &comAddr);
    
    printf("이름은? \n");
    gets(name);
    
    printf("전화번호는? \n");
    gets(telno);
    
    printf("주소는? \n");
    gets(comAddr);
    
    printf("너의 개인정보: %s, %s, %s \n", name, telno, comAddr);
    
	return 0;
}

```

### 2. 문자열 입출력함수 정리

- 형식지정자 `%s`

  - 입 출력시 **주소를 받는다.**
    - 단, 문자 배열은 변수명을 쓸 때 첫 메모리 주소를 반환하기 때문에 그냥 써도 된다.
  - 출력시
    - **메모리 주소를 받으면 해당 메모리 주소부터 \0을 만날때까지 문자열을 출력**
    - 즉, 문자 배열 변수명(== 문자열의 첫 메모리 주소)을 받으면 출력

  - 입력시(scanf 등)
    - **메모리 주소를 받으면 해당 메모리 주소부터 \0을 만날때까지 문자열을 입력**

#### 1. 입력

- **아래 두 함수는 배열의 경계를 검사하지 않는다.**
  - 따라서 문자배열은 저장된 문자열의 크기보다 1 큰 메모리를 할당받아야 한다.
- `gets(stringArray);`
  - 문자열을 읽어 배열 stringArray에 저장
  - **인자로 문자 배열 메모리 주소를 받는다**
    - 주소로 넣어 주어도 상관없다.
  - **enter만 null로 바뀌어서 문자열을 구분하여 저장된다.**
    - 즉, 공백, tab은 그대로 문자열로 취급된다.

- `scanf("%s", stringArray);`
  - **두 번째 인자로 문자 배열 메모리주소를 받는다**
    - stringArray는 그 자체로 메모리 주소이기 때문에 앞에 &를 붙여줄 필요가 없다.
      - `stringArray == &stringArray == &stringArray[0]`
  - **공백문자를 포함할 수 없으며** 공백, 탭, Enter로 문자열을 구분하여 저장한다.
    - **공백, tab, enter가 null로 바뀌어** 문자열을 구분하여 저장된다.
    - 뒤에 `%*c`를 잊지 말자
- gets에서 enter 입력시 null로 바뀌는 예시

```c
#include <stdio.h>

int main() {
	char msg[100];
	int number = 0, alpha = 0, special = 0, i;

	printf("문자열 입력? ");
	
	gets(msg); // C program is Fun !!!, Book Price: 25000[enter]
	
    // 아래쪽에 숫자가 아닌 문자로 비교해도 된다.
	for (i = 0; msg[i]; i++) {
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

#### 2. 출력

- `puts(stringArray);`

  - 자동개행을 보장한다.

- `printf("%s", stringArray);`

   

### 3. scanf_s(), gets_s()

- 안전한 메모리 관리를 위해 
- 표준 C 라이브러리에는 포함되지 않고 있다.
- 형식

```c
#include <stdio.h>

int main() {
    char name[20];
    char tel_no[20];
    
    printf("성명 ?");
    scanf_s("%s", name, 20);
    printf("%s \n", name);

}
```



## 3. C 문자열 처리함수

- C에서의 문자열은 배열의 일종이기에 많은 제약사항이 있다.
- 예를 들어, `=` 연산자를 통해 문자열을 복사하는 것은 불가능하다
  - **대입 연산자를 통해 배열 복사 불가능**

```c
char a[] = "abc";
char b[4];

b = a; // 불가능
```

- 배열 변수를 통한 값 비교는 값이 아닌 주소를 비교하기 때문에 배열 내용이 같다고 이를 비교할 수 없다.

```c
#include <stdio.h>

int main() {
	char a[] = "kill";
	char b[] = "kill";
	if (a == b) {
		printf("같습니다.");
	} else 
 		printf("다릅니다."); // 얘 출력
	
    return 0;
}

```

- c 라이브러리는 문자열을 처리하기 위한 기본적인 함수를 제공한다.
  - **해당 함수들은 문자배열이 아닌 다른 데이터 타입의 배열은 처리할 수 없다.**

### 0. <string.h>

- 문자열 처리를 위한 함수들의 원형을 담은 헤더파일

- `#include <string.h>`
- 해당 라이브러리의 함수들은 인자로 하나 이상의 문자열을 요구한다.
- **함수원형을 살펴보면 매개변수는 char* 형으로 선언되어 있으므로 매개변수로 문자형 배열, char*형 변수, 혹은 분자형 리터럴 등 문자열이 될 수 있는 모든 것을 받을 수 있다.**
- 다만, 함수원형에 const로 선언되지 않은 문자열 매개변수는, 함수호출시 값이 변경될 수 있기 때문에 주의하자.



### 1. strcpy

- 문자열 복사 함수
- 함수 원형
  - `char* strcpy(char* destination, const char* source);`
    - source가 가리키는 문자열을 destination이 가리키는 배열에 복사해준다.
- 반환값
  - **destination의 포인터**
- 예시

```c
#include <stdio.h>

int main() {
	char str1[10];
	char str2[10];
	
    // 문자열 리터럴 복사
    printf("%s", strcpy(str2, "abcd"));
    
    // 배열을 복사
    printf("%s", strcpy(str1, str2));
    
    // 반환값을 사용하여 배열을 여러 번 복사
    printf("%s", strcpy(str1, strcpy(str2, "dcba")));
    
    return 0;
}

```



### 2. strlen

- 문자열 길이 반환 함수

- 예시

  1. 메모리 주의하며 문자 받아와서 합치기	

     ```c
     #include <stdio.h>
     // 헤더파일이 없다고 라이브러리를 못 부르는 건 아니다 => 링커가 붙여준다. + 현재는 문제가 없다(문자열 함수는 기본적으로 포인터 주소(숫자)도 입력받기 때문)
     
     #include <string.h>
     
     
     int main(void) {
     	// 문자열을 s1에 받아와서 s2에 합치려고 함
         char s1[20], s2[20];
     
     	do {
     		printf("input s1 ?");
     		gets(s1); // dom[enter]
     	} while (strlen(s1) + strlen(s1) >= sizeof(s2)); // 메모리 할당 크기는 상수로 주는 것이 아니다 => 위험하다.
         
         strcat(s2, s1);
     	return 0;
     }
     ```

  2. 메모리 주의하며 입력 문자열 크기 제한

     ```c
     #include <stdio.h>
     #include <string.h>
     
     int main(void) {
     
     	// strlen, strcpy를 이용한 입력 문자열 크기 제한
     	char tmp[200];
     	char str[10];
     	
     	do {
     		printf("9자 이하로 입력해주세요 \n");
     		gets(tmp);
     	} while (sizeof(str) <= strlen(tmp));
     
     	strcpy(str, tmp);
     
     	printf("%s \n", str);
     
     	return 0;
     }
     ```



### 3. strcat

- string concat

- 문자열 연결 함수

- 함수 원형
  - `char* strcat(char* destination, const char* source);`
    - source의 내용을 destination 끝에 이어붙여준다.
- 반환값
  - destination의 포인터

- 예시

```c
strcpy(str1, "abc");
strcpy(str1, "def");
```



### 4. strcmp

- string compare
- 함수 원형
  - `int strcmp(const char* str1, const char* str2);`
- **문자열** str1과 str2를 비교하여 값을 반환한다.
  - 반환값
    - 1
      - 앞이 크다
    - 0
      - 크기가 같다
    - -1
      - 뒤가 크다
- **ASCII를 이용해서 사전식 순서로 비교를 한다**
  - A에서 Z, a에서 z, 0에서 9라는 연속된 문자들은 마찬가지로 연속된 코드를 갖는다.
  - 모든 대문자는 소문자보다 작다. (ASCII에서 65에서 90까지의 코드들이 대문자이며; 97과 122까지의 코드가 소문자다.)
  - 숫자는 문자보다 작다. (48에서 57까지가 숫자다.)
  - 띄어쓰기는 모든 출력 가능한 문자보다 작다. (띄어쓰기는 ASCII에서 32라는 값을 갖는다.)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
	char str[20] = "apple";
    char str1[10] = "apple";
    char str2[20] = "Apple";
    
    printf("같으면 0, 앞이 크면 1, 뒤가 크면 -1: %d \n", strcmp(str, str1)); // 0	
    printf("같으면 0, 앞이 크면 1, 뒤가 크면 -1: %d \n", strcmp(str1, str2)); // 1 => 사전식 비교
    
    return 0;
}
```

### 
