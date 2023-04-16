# Array

## I. 배열

데이터가 많을 경우, 배열로 만들어서 관리

데이터 저장하는 3가지 방법

1. 변수

2. 배열

   - 같은 형식의 데이터만 저장 가능

   - 크기 변경 불가
     - 추가, 삽입, 삭제 불가

3. 컬렉션

   - 서로 다른 데이터를 저장 가능
   - 크기 변경 가능
     - 추가, 삽입, 삭제 가능

### 1. 배열의 특징

- 원시형, 참조형 등 **모든 데이터**를 배열로 저장 가능
- 같은 데이터 형만 배열로 저장 가능(C와 동일)
- 배열 원소로의 접근은 첨자 사용
- 배열의 크기는 `.length`를 사용해서 구함
- **사용시 선언 및 생성 필요**
  - 선언만 해서는 사용할 수 없음
- 생성은 3가지 방법으로 가능
  - `new` 키워드
  - 리터럴 사용
  - `new` 키워드와 리터럴 혼합

- 배열이 생성되면 기본적으로 데이터형에 맞춰서 초기화됨
  - 임의의 값은 변수 문서 참고

### 2. 배열 사용법

1. 변수 선언
   - `데이터형 [] 배열명`
     - 주로 사용
   - `데이터형 배열명 []`
2. 생성 및 할당
   - 배열명 = new 객체명[배열크기]
   - 변수에 저장된 데이터는 주소값
     - 즉 변수의 자료형은 `데이터형`이 아니라 `데이터형[]`
3. 선언과 생성 및 할당 동시에 가능
   - `int[] numbers = new int[30];`
   - 배열 자체는 클래스의 인스턴스이므로 **힙 영역에 생성**되고, 스택 영역에 생성된 numbers변수로 사용가능

```
package p02;

public class Array {

	public static void main(String[] args) {
		int[] myArray = new int[30]; // 선언, 생성, 할당
		
		System.out.println(myArray.length); // 길이는 30
		
		System.out.println(myArray); // 주소값 출력
		
		System.out.println(new int[30]); // 생성만 하고 할당 안하기 => 힙역역의 주소값 출력
	}

}

```



### 3. for - each 반복문

- 배열의 크기를 넘는 인덱스를 사용할 경우 `ArrayIndexOutOfBoundsException` 에러 발생
- 이를 방지하기 위한 특이한 방식의 반복문
- 배열의 원소를 가져와서 i에 저장한 후, 이후 문을 실행
  - **변수에 저장해 주는 것이기 때문에, 원본은 변경할 수 없다!**
  - 즉, 출력이나 별도 연산에서만 가능

```
package p02;

public class Array {

	public static void main(String[] args) {
		int[] myArray = new int[30]; // 선언, 생성, 할당
		
		
		for (int i=0; i < myArray.length; i++) {
			myArray[i] = i;
		}
		
		// for - each 반복문 => for of 반복문과 유사
		for (int i: myArray) {
			System.out.println(i);
		}	
	}
}

```



### 4. 리터럴을 이용한 배열 초기화

- **C와 마찬가지로 초기화 때만 이렇게 할당 가능**

- `int[] myArr = {1, 2, 3};`

- 단, 리터럴을 이용해 초기화 할 때는, 선언 후 따로 할당을 할 수 없다.

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		int[] myArr = {1, 2, 3};

		for (int i : myArr) {
			System.out.println(i);
		}
		
	}

}

```



### 5. new와 리터럴 혼합

- 혼합 사용시는 new 생성자 내부에 배열 크기를 넣어주면 안됨

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		int[] myArr;
		myArr = new int[] {1, 2, 3};
		
		// 위 두 라인을 한 번에
		// int[] myArr = new int[] {1, 2, 3};
		
		for (int i : myArr) {
			System.out.println(i);
		}
	}
}
```



### 6. 파라미터로 배열 전송

메서드의 파라미터로 배열을 전달할 경우, 배열도 객체이기 때문에 원본 배열의 위치값이 넘겨진다.

**따라서 해당 배열을 수정하면 원본 배열도 수정된다.**

- **call by reference**

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		int[] numbers = {1, 2, 3 ,4, 5};
		
		for (int i: numbers) {
			System.out.println(i);
		} // 1, 2, 3, 4, 5
		
		change(numbers);
		
		for (int i: numbers) {
			System.out.println(i);
		} // 2, 3, 4, 5, 6
	}
	
	public static void change(int[] args) {	
		for (int i=0; i < args.length; i++) {
			args[i]++;
		}
	}
}

```



### 7.  배열 복사

- System.arraycopy를 사용한 배열 복사
- `System.arraycopy(Object source, int sourceStartIndex, Object dest, int destStartIndex, int length)`
  - source배열의 sourceStartIndex인덱스부터 length만큼의 원소를 dest 배열의 destStartIndex부터 복사
  - target 배열의 크기가 더 작으면 에러

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		int[] source = {1, 2, 3, 4, 5};
		
		for(int i : source) {
			System.out.println(i);
		}
		
		int[] target = new int[5] ;
		
		
		System.arraycopy(source, 0, target, 0, source.length);
		
		System.arraycopy(source, 0, target, 0, source.length);
		for(int j : target) 
			System.out.println(j);
		
	}
}

```

### 8. main메서드에서의 배열 사용

- 프로그램의 시작점(starting point)역할을 하는 main 메서드 표현식은 다음과 같으며 파라미터로  String 배열이 사용된다.
- cmd에서 실행할 때, 띄어쓰기로 구분해서 입력하거나, run configuration의 arguments에서 설정할 수 있다.
  - `${string_prompt}`를 넣어 주면 프로그램을 실행할 때 입력창이 뜬다.

- 단, 숫자을 입력해도 문자열로 처리하기 때문에 Integer.parseInt() 등을 통해 변환해 주어야 한다.

```java
package p02;

public class Args {

	public static void main(String[] args) {
		for(String i : args) {
			System.out.println(Integer.parseInt(i));
		}
		
	}

}

```



## II. 이차원 배열

- 배열 생성 및 할당
- 이차원 배열은 나란히 메모리 공간을 차지하는 게 아니라, 주소를 담고 있는 행 배열이 있고, 그 주소들은 각각 다른 위치에 할당된 배열들을 가리킴

- 비정방형 이차원 배열은, 행에 NULL(주소값이므로)이 선언되어 있음

- r행 c열의 2차원 배열 n에서, 행의 길이에 접근할때는 `n.length`, 열의 길이에 접근할때는 `n[0].length`

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		// 여러 가지 이차원 배열 생성 방법
		
		// 1. new 키워드 할당
		// 정방형 배열
		int[][] myArr = new int[3][5];
		
		// 비정방형 배열
		int[][] myArr2 = new int[3][];
		
		System.out.println(myArr[0]);
		System.out.println(myArr[1]);
		System.out.println(myArr[2]);
		
		// 에러 2가지
		// int[][] myArr3 = new int[][];		
		// int[][] myArr3 = new int[][5];		
		
		// 비정방형 배열의 원소를 각각 할당
		// myArr의 [0], [1], [2]에는 처음에는 NULL값이 할당
		myArr2[0] = new int[] {1, 2, 3};
		
		myArr2[1] = new int[4];
		for(int x: myArr[1]) {
			x = 4;
		}

		// 불가능 => 이미 초기화됨
		// myArr2[2] = { 1, 2, 3, 4, 5 }; 
		
		
		// 참
		System.out.println(myArr2 instanceof int[][]);

		
		// 2. 리터럴 사용 할당
		int [][] myArr3 = { {1, 2}, {3, 4, 5} };
	
		
		// 3. 혼합 사용 할당
		int[][] myArr4 = new int[][] {{1, 2}, {3, 4, 5}};
		
	}
}

```

- 비정방형 배열 반복 돌리기

```java
package p02;

public class Array {

	public static void main(String[] args) {
		
		String[][] myString = {{"햄릿", "맥베스"}, {"아메리칸 푸라푸치노", "앙카와 푸카", "패스츄리 로맨스"}};
		
		for (int i=0; i < myString.length; i++) {
			for (int j=0; j < myString[i].length; j++) {
				System.out.println();
			}	
		}
	}
}

```



## III. java.util.Arrays 클래스

배열 사용시 도움을 받을 수 있는 클래스

```java
package counter;

import java.util.Arrays;

import java.util.List;

public class UtilString {

	public static void main(String[] args) {
		
		// 1. 배열값 출력(문자열로 출력)
		int[] n = {10, 20, 30};
		String[] s = {"A", "B", "C"};
		System.out.println(Arrays.toString(n)); 		// [10, 20, 30]
		System.out.println(Arrays.toString(s)); 		// [A, B, C]
		
		// 2. 모든 배열값이 변경
		String[] s2 = {"A", "B", "C"};
		Arrays.fill(s2, "X");
		System.out.println(Arrays.toString(s2));
		
		// 3. 값 변경: 일부분 배열값이 변경
		String[] s3 = {"A", "B", "C", "D", "E", "F", };
		Arrays.fill(s3, 0, 4, "X");						// 0 ~ 3까지 변경
		System.out.println(Arrays.toString(s3));
		
		// 4. 값 비교
		int [] x = { 1, 2, 3 };
		int [] x2 = { 1, 2, 3 };
		System.out.println(Arrays.equals(x, x2));
		
		// 5. 정렬
		int [] x3 = {4, 2, 3, 98, 43, 24, 65};
		Arrays.sort(x3);
		System.out.println(Arrays.toString(x3));
		
		// 6. 이진탐색 => 위치찾기 => 정렬 필수
		int [] k2 = {2, 4, 6, 29, 31, 42, 51};
		System.out.println(Arrays.binarySearch(k2, 6));
		
		// 7. 배열 길이 변경
		int [] y = {1, 2, 3};
		int [] y2 = Arrays.copyOf(y, 5);
		System.out.println(Arrays.toString(y));
		System.out.println(Arrays.toString(y2));
		
		// 8. 개별적인 값들을 컬렉션 API로 생성
		
		List<String> list = Arrays.asList("A", "B", "C");
		System.out.println(list);
		
		List<Integer> list2 = Arrays.asList(1, 2, 3);
		System.out.println(list2);
	}			

}

```

