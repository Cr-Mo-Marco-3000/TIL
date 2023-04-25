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

### 참고: Iterator

for보다 빠른 반복을 위한 객체

- 생성
  - `Iterator<E> ite = list.iterator();`
  - `Iterator<E> ite2 = map.iterator();`
- 메서드
  - `hasNext()`
    - 가져올 객체가 있으면 true, 아니면 false
    - return
      - boolean
  - `next()`
    - return
      - E
  - remove()
    - next()로 가져온 객체를 제거\

- 예시

```java
List<Integer> myList = ArrayList<Integer>();
Iterator<Integer> ite = myList.iterator();

while(ite.hasNext()) {
    System.out.println(ite.next());
}
```



## I. Set

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

- ArrayList를 선언하는 세가지 방법

```java
// 제네릭으로 저장되는 객체 설정
List<E> list = new ArrayList<E>();
List<E> list2 = new ArrayList<>();
// 설정 안함
List list3 = new ArrayList();
```

- 예시

```java
package p04;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;

public class ListTest {

	public static void main(String[] args) {
		
		ArrayList<String> list = new ArrayList<>();
		
		// 저장 => 중복 가능
		list.add("Hello");
		list.add("World");
		list.add("Idiots");
		
		// 출력1 - toString()
		System.out.println(list);
		
		// 출력2 - foreach 생략
		
		// 출력3 - Iterator
		Iterator<String> ite = list.iterator();
		
		while(ite.hasNext()) {
			System.out.println(ite.next());
		}

		// 출력 4 - get(idx)
		String x = list.get(0);
		String x2 = list.get(1);
		System.out.println(x + x2);
		
		System.out.println("길이: " + list.size());
		System.out.println("길이: " + list.isEmpty());
		System.out.println("길이: " + list.contains(10));
		System.out.println("길이: " + list.contains(40));
		System.out.println("길이: " + list.indexOf(10));
		
		// 배열로 반환

		Object [] obj = list.toArray();		// 동적바인딩을 통해 Array에 list의 내용물을 담음
		System.out.println("배열로 변환: " + Arrays.toString(obj));
		
		// 부분 리스트
//		List<Integer> subList = list.subList(0, 2);
//		System.out.println(subList);
		
	}

}

```

- 예시 2
  - 아래 예시에서 사용되는, Arrays.asList()로 생성되는 ArrayList는, List 다형성에 담기기는 한다.
    - java.util.ArrayList의 ArrayList가 아니다!
    - 따라서, 원소 추가 등 조작이 불가능하다.


```java
package p04;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Cat {
	String name;
	int age;
	String gender;
	
	public Cat() {
		
	}

	public Cat(String name, int age, String gender) {
		this.name = name;
		this.age = age;
		this.gender = gender;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	@Override
	public String toString() {
		return "Cat [name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
	
}

public class ListTest2 {

	public static void main(String[] args) {
		
		// 1. 배열 이용 => 추가, 삽입, 삭제 불가능, 출력만 가능
		Cat [] catArr = {
				new Cat("야옹이", 2, "암컷"),
				new Cat("나비", 1, "수컷")
		};
	
		// 2. List 이용 (다형성)
		List<Cat> list = new ArrayList<Cat>();
		list.add(new Cat("야옹이", 2, "암컷"));
		list.add(new Cat("나비", 1, "수컷"));
		
		// 2-2. 많이 사용되는 패턴 ==> 추가 작업 불가능
		List<Cat> list2 = Arrays.asList(
				new Cat("야옹이", 2, "암컷"), 
				new Cat("나비", 1, "수컷"));
		
		// 추가
		list.add(new Cat("망치", 3, "수컷"));
		// 삽입
		list.add(0, new Cat("망치", 3, "수컷"));
		// 수정
		list.set(0, new Cat("블랙", 1, "수컷"));
		
		// 출력
		System.out.println(list);
		
		// 삭제
		// by index
		list.remove(0);
		// by value
		list.remove(new Cat("망치", 3, "수컷"));
		
	}

}

```



## III. Map

```java
package p04;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapTest {

	public static void main(String[] args) {
		
		// 1. HashMap
		// <key, value>
		// 다형성으로 작성이 일반적
		Map <String, String> map = new HashMap<>();
		
		// 데이터 저장
		map.put("p01", "홍길동1");
		map.put("p02", "홍길동2");
		map.put("p03", "홍길동3");
		
		// 출력 1 - get(key) => 키가 없으면 null 반환
		String n = map.get("p01");
		System.out.println(n);
		System.out.println(map.get("p02"));
		System.out.println(map.get("p100")); // null 반환
		
		// 출력 2 - key값을 우선 얻고(Set 반환) - value 출력
		Set<String> keys = map.keySet();
		
		System.out.println(keys);
		
		for (String key: keys) {
			System.out.println(map.get(key));
		}
		
		// 출력 3 - toString
		System.out.println(map);
		
		
	}
}

```



```java
package p04;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapTest2 {

	public static void main(String[] args) {
		
		// 1. HashMap
		// <key, value>
		// 다형성으로 작성이 일반적
		Map <String, String> map = new HashMap<>();
		
		// 데이터 저장
		map.put("p01", "홍길동1");
		map.put("p02", "홍길동2");
		map.put("p03", "홍길동3");
		
		// 확인
		System.out.println(map.size());
		System.out.println(map.containsKey("p01"));
		System.out.println(map.containsValue("홍길동1"));
		System.out.println(map.isEmpty());		
		
		// 삭제 by key
		map.remove("po3");
		
		// 치환 by key
		map.replace("p01", "이순신");
		System.out.println(map);
		
		// 전체삭제
		map.clear();
		
		System.out.println(map);
		
		
		
	}
}

```

