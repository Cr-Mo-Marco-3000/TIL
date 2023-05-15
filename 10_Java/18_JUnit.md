# Junit

## I. 개요

- Java에서 테스트 주도 개발에 사용되는 라이브러리
- 테스트 코드를 작성하는 목적
  - 코드의 안정성을 높일 수 있음
  - 기능 추가와 변경 과정에서 side-effect를 줄일 수 있음
  - 해당 코드가 작성된 목적을 명확하게 표현 가능
    - 코드에 불필요한 내용이 들어가는 것을 비교적 줄일 수 있음

### 1. JUnit이란?

- Java 진영의 대표적인 Test Framework
- 단위 테스트를 위한 도구를 제공
  - 단위 테스트란?
    - 코드의 특정 모듈이 의도된 대로 동작하는지 테스트 하는 절차를 의미
    - 모든 함수와 메소드에 대한 각각의 테스트 케이스(Test Case)를 작성하는것
  - 어노테이션(Annotation)을 기반으로 테스트를 지원
  - 단정문(Assert)로 테스트 케이스의 기대값에 대해 수행 결과를 확인할 수 있음
- JUnit 5는 크게 Jupiter, Platform, Vintage 모듈로 구성됨



### 2. JUnit 모듈 설명

#### 1. JUnit Jupiter

TestEngine API 구현체로 JUnit 5를 구현하고 있음

테스트의 실제 구현체는 별도 모듈 역할을 수행하는데, 그 모듈 중 하나가 Jupiter-Engine임

이 모듈은 Jupiter-API를 사용하여 작성한 테스트 코드를 발견하고 실행하는 역할을 수행

**개발자가 테스트 코드를 작성할 때 사용됨**

#### 2. JUnit Platform

Test를 실행하기 위한 뼈대

Test를 발견하고 테스트 계획을 생성하는 TestEngine 인터페이스를 가지고 있음

TestEngine을 통해 Test를 발견하고, 수행 및 결과를 보고함

그리고 각종 IDE 연동을 보조하는 역할을 수행(콘솔 출력 등)

(Platform = TestEngine API + Console Launcher + JUnit 4 Based Runner 등)

#### 3. JUnit Vintage

TestEngine API 구현체로 JUnit 3, 4를 구현하고 있음

기존 JUnit 3, 4버전으로 작성된 테스트 코드를 실행할 때 사용됨

Vintage-Engine 모듈을 포함



## II. Annotations

### 3. JUnit LifeCycle Annotation

JUnit 5는 아래와 같은 테스트 라이프 사이클을 가지고 있음

1. @Test
   - 테스트용 메소드를 표현하는 어노테이션
2. @BeforEach
   - 각 테스트 메소드가 시작되기 전에 실행되어야 하는 메소드를 표현
3. @AfterEach
   - 각 테스트 메소드가 시작된 후 실행되어야 하는 메소드를 표현
4. @BeforeAll
   - 테스트 시작 전에 실행되어야 하는 메소드를 표현(static 처리 필요)
5. @AfterAll
   - 테스트 종료 후에 실행되어야 하는 메소드를 표현(static 처리 필요)



### 4. JUnit Main Annotation

1. @SpringBootTest
   - 통합 테스트 용도로 사용됨
   - @SpringBootApplication을 찾아가 하위의 모든 Bean을 스캔하여 로드함
   - 그 후 Test용 Application Context를 만들어 Bean을 추가하고, MockBean을 찾아 교체

2. @ExtendWith
   - JUnit4에서 @RunWith로 사용되던 어노테이션이 ExtendWith로 변경됨
   - @ExtendWith는 메인으로 실행될 Class를 지정할 수 있음
   - @SpringBootTest는 기본적으로 @ExtendWith가 추가되어 있음



## III. 주의점

- 테스트 메서드와 라이프사이클 메서드는 다음과 같은 형태이면 **안된다**.
  - 추상 메서드
  - return값을 가진 메서드
    - 단, `@TestFactory`를 단 메서드는 제외
  - private으로 지정된 메서드
