

# StreamAPI

- 스트림 API(Strean API)
- jdk 1.8 ~ 사용가능
- 기존에는 해당 값들을 반복하기 위해 for문 혹은 Iterator 사용
- Java 8부터 또 다른 방법으로 **컬렉션 및 배열**의 요소를 반복 처리하기 위해 Stream 사용 가능
- **컬렉션 또는 배열에 `stream()` 메서드로 Stream 객체를 얻고**, forEach() 메서드로 요소를 어떻게 처리할지 람다식으로 제공
- 장점
  1. 내부 반복자이므로 처리 속도가 빠르고 병렬 처리에 효율적
  2. 람다식으로 다양한 요소 처리를 정의 가능
  3. 중간 처리와 최종 처리를 수행하도록 파이프라인 형성 가능

- `배열, 컬렉션, 파일 + Stream`
  - 기능처리(메서드의 파라미터로 대부분이 함수형 인터페이스로 되어있다.)
    - 중간처리
      - 정렬, 필터링, 연산, 중복처리(`.distinct()`) 등
    - 최종처리
      - 집계
      - 변환
      - 반복출력

- 사용순서
  1. stream 얻기
  2. 중간처리
  3. 최종처리

- 가장 기본적인 예시

```java
package stream_api;

import java.util.HashSet;
import java.util.Set;
import java.util.stream.Stream;


public class StreamTest1 {

	public static void main(String[] args) {
		
		// 1. Set 컬렉션 생성
		Set<String> set = new HashSet<>();
		set.add("홍길동");
		set.add("신용권");
		set.add("가가가");
		
		Stream<String> stream = set.stream();				// 스트림 얻기 => 컬렉션이나 배열에 .stream을 붙여서 얻음
		stream.forEach(name -> System.out.println(name));	// 람다식을 통해 각각의 요소를 처리
	}

}

```



## 1. 내부 반복자

for문과 iterator는 컬렉션의 요소를 컬렉션 바깥쪽으로 반복해서 가져와 처리(외부 반복자)

스트림은 요소 처리 방법(람다식)을 컬렉션 내부로 주입시켜서 요소를 반복 처리(내부 반복자)

내부 반복자는 멀티코어 CPU를 최대한 활용하기 위해 요소들을 분배시켜 병렬 작업을 할 수 있다.

하나씩 처리하는 순차적 되부 반복자보다, **효율적으로 요소를 반복**시킬 수 있는 장점이 있다.

```java
package stream_api;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class ParallelStreamExample {

	public static void main(String[] args) {
		// List 컬렉션 생성
		List<String> list = new ArrayList<String>();
		
		list.add("홍길동");
		list.add("김삿갓");
		list.add("박용택");
		list.add("박용근");
		list.add("김아야");
		
		Stream<String> stream = list.parallelStream();	// 병렬 스트림 얻기
		stream.forEach(name-> {
			System.out.println(name + ": " + Thread.currentThread().getName());	// 람다식 -> 요소 처리 방법
		})
	}
}

```



## 2. 중간 처리와 최종 처리

스트림은 하나 이상 연결될 수 있다.

스트림이 연결되는 것을 스트림 파이프라인이라고 한다.

오리지널 스트림과 집계 처리 사이의 중간 스트림들은 최종 처리를 위해 요소를 걸러내거나(필터링), 요소를 변환시키거나(매핑), 정렬하는 작업을 수행한다.

최종 처리는 중간 처리에서 정제된 요소들을 반복하거나, 집계(카운팅, 총합, 평균) 작업을 수행한다.

파이프라인으로 구성할 때 주의할 점은, 파이프라인의 맨 끝에는 반드시 최종 처리 부분이 있어야 한다는 것이다.

최종 처리가 없다면 오리지널 및 중간 처리 스트림은 동작하지 않는다.

즉 아래 코드에서 average() 이하를 생략하면 stream(), mapToInt()는 동작하지 않는다.

```java
// Student 스트림
Stream<Student> studentStream = list.stream();

// Score 스트림
IntStream scoreStream = studentStream.mapToInt(student -> student.getScore());	// Student 객체를 getScore() 메소드의 리턴값으로 매핑

// 평균 계산
double avg = scoreStream.average().getAsDouble();

// 메소드 체이닝 패턴을 통해 더 간단하게 작성
double avg = list.stream().mapToInt(student -> student.getScore()).average().getAsDouble();
```

