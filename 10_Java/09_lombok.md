# Lombok

생성자, getter/setter, toString을 자동으로 제공하는 라이브러리



## 1. 설치

c 드라이브로 설치 파일을 옮긴다.

`java -jar lombok.jar`

이클립스를 찾아서 설치



## 2. maven에 dependency 작성

- pom.xml에 롬복 추가
- restart, rebuild하기
  - 이클립스 종료후 재실행
  - project - project clean후 빌드

## 3. 코드 작성

- 클래스 위에 다음 어노테이션들을 달아준다.
  - 해당 어노테이션이 생성자 등을 대체한다.

```java
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
```

