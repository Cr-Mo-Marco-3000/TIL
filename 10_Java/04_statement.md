# 조건문

문장

- 실행문
  - 순차문 - main method의 첫라인부터 해당 블록의 끝까지 => ;로 끝남
  - 제어문
    - 조건문
    - 반복문
- 비실행문
  - 주석문

## 1. if문

- 조건문 후 실행한 문장이 하나일 경우, 코드블록 생략 가능(c와 동일)



## 2. switch문

- c에서의 switch문과 동일

- break가 없으면 걸리는 조건부터 이후까지 다 실행
- C와 다른 점
  - 조건에 byte, short, int, char, String, enum 가능

```java
package p02;

public class typecast {

	public static void main(String[] args) {
        // 문자열
		String season = "여름";
		char a = 'a';
		switch (season) {
		case "봄":
			System.out.println("spring");
			break;
		case "여름":
			System.out.println("summer");
			break;
		default:
			System.out.println("사계절이 아닙니다");
		}	
		
        // 문자
		switch (a) {
		case 'a':
			System.out.println("spring");
			break;
		case 'b':
			System.out.println("summer");
			break;
		default:
			System.out.println("사계절이 아닙니다");
		}
        
        //enum
        
	}

}

```



## 3. 반복문

- 우리가 아는 그 반복문
  - 단, for를 쓸 때 조건문에 int를 써 주어도 된다.

- for
- while
- do-while
- break
- continue

### 1. 반복문에 별칭 사용

- 반복문에 Label을 붙임으로써 continue나 break를 유동적으로 사용 가능

```java
package loop;

public class breakAndContinue {

	public static void main(String[] args) {
		BigLoop:
			for (int i=2; i<10; i++) {
				SmallLoop :
					for (int j=2; j<10; j++) {
						if (i == 3) {
							break BigLoop; // 바깥쪽의 반복문을 종료시키기 때문에, 3단은 출력되지 않는다.
						}
						System.out.print(i * j + " ");
					}
				System.out.println();
			}
	}

}

```

