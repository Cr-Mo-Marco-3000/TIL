# Collections & Map

- 용도
  - 여러 개의 Data 저장

- 특징

  - 참조형 Data값만 저장 가능
    - 기본형 Data는 Wrapper로 저장 가능
  - 저장되는 데이터의 종류 무관

  - 크기변경 가능(삭제, 추가, 삽입)

  - Data 사용여부에 따라서 저장하는 자료구조가 달라짐

- 종류
  - Collection 계열
    - List 계열
      - 순서 존재, 중복 가능
    - Set 계열
      - 순서 미존재, 중복 불가
  - Map 계열
    - 순서 미존재, Key & Value를 저장
    - key를 이용해 값을 관리

- 계층구조
  - Collection(Interface)
    - Set (Interface)
      - HashSet
      - ...
    - List (Interface)
      - ArrayList
      - ...
  - Map(독자적인 Interface: Collection 계열이 아님!)
    - HashMap



## I. set



```java
package p03;

import java.util.HashSet;
import java.util.Iterator;

public class SetTest {

	public static void main(String[] args) {
		
		// 다형성
		// Set set = new HashSet<>();
		HashSet set = new HashSet<>();
		
		set.add("홍길동");
		set.add(24);
		set.add(3.14);
		set.add("홍길동");
		
		// 출력1 => toString 출력
		System.out.println(set);
		
		// 출력2 => for - each 문 이용
		for (Object obj : set) {
			System.out.println(obj);
		}
		
		// 출력3 => Iterator Interface 이용
		// hasNext()
		// next()
		Iterator ite = set.iterator();
		
		while (ite.hasNext()) {
			System.out.println(ite.next());
		}
		
		// 추가 메서드
		
		/*
		 * 배열크기: 	배열명.length
		 * 문자열길이:	s.length()
		 * 컬렉션크기:	변수명.size()
		 * 
		 */
		
		System.out.println("크기: " + set.size());
		System.out.println("비어있냐: " + set.isEmpty());
		System.out.println("비어있냐: " + set.contains(24));
		
		// 삭제
		set.remove("홍길동");
		
		// 전체삭제
		set.clear();
	}

}

```



## II. List