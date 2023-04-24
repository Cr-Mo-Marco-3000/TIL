# map

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

