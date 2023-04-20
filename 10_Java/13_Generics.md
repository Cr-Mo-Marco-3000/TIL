# Generics

컬렉션에 저장되는 Data 타입을 제한하는 방법

일반적으로, 컬렉션에도 같은 타입만 저장하는 것이 더 일반적임

저장할 때 이 타입을 제한하는 방법 => 저장을 잘못하면 컴파일 에러 발생

- 형식
  - `ClassName<DataType> variableName = new Classname<[DataType]>()`

- 장점
  - 잘못된 데이터 저장을 실행시점이 아닌 컴파일 시점에 알 수 있음
  - 가져올 때 형변환이 불필요하다.

```java
package p03;

import java.util.HashSet;
import java.util.Set;

public class GenericsTest {

	public static void main(String[] args) {
		
		
		// 1. 제네릭스 미사용 => 문자열 중에 숫자 포함시
		Set set = new HashSet<>();
		
		set.add("홍길동");
		set.add("홍길동2");
		set.add("홍길동3");
		set.add(4);		
		
		// 반드시 형변환 필요 => 없으면 런타임 에러 발생
		for (Object x: set) {
			System.out.println(((String)x).length());
		}
		
		/*
		 * 장점
		 * 1) 제네릭스를 사용하면 잘못된 데이터를 컴파일 시점에 알 수 있다.
		 * 2) 형변환이 빌요없다
		*/
		
		// 2. 제네릭 사용
		Set<String> set2 = new HashSet<>();
		set2.add("홍길동");
		set2.add("홍길동2");
		set2.add("홍길동3");
		// set2.add(4); => 컴파일에러 발생
		for (String x: set2) {
			System.out.println(x.length());
		}
	}

}

```



