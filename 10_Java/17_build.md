# 빌드 툴(Build Tool)

### 개발 과정

1. 소스 파일 작성

2. jar 다운로드 + build path

3. 컴파일

2. 소스파일 검증(특정 기능 검증) - 단위 테스트(junit 라이브러리: 소스파일 동작 확인)

3. 패키징(압축: jar, war)

4. 배포

   - 로컬

   - 원격

1 ~ 4까지를 해주는 툴을 빌드 툴이라고 하며, 이는 자동화를 의미한다.

대표적인 자동화 툴에는 maven과 gradle이 있다.



## 1. maven

프로젝트를 생성 시 maven project로 생성

1. create a simple project
2. groupId
   - 패키지
3. ArtifectId
   - 프로젝트명



### 1. 폴더 구조 설명

1. src/main/java
   - 소스 파일 저장
2. src/main/resources
   - `.java`가 아닌 파일들 저장(xml 등)
3. src/test/java
   - 단위 테스트용



### 2. pom.xml

pom.xml에 사용할 jdk버전을 넣은 후, 프로젝트 우클릭, maven update project

```java
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.app</groupId>
  <artifactId>MavenTest</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  
  <build>
 	<plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.5.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
    </plugins>
 </build>
 
</project>
```



### 3. jar 관리

pom.xml에 필요한 jar 정보만 지정하면 자동으로 다운 및 build path 해줌

`<dependencies>` 태그에 넣어준다.

- dependency 정보
  - `mvnrepository.com`
- 

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.app</groupId>
  <artifactId>MavenTest</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  
  <dependencies>
	  
	<dependency>
	    <groupId>org.mybatis</groupId>
	    <artifactId>mybatis</artifactId>
	    <version>3.5.13</version>
	</dependency>
	
	<dependency>
	    <groupId>org.junit.jupiter</groupId>
	    <artifactId>junit-jupiter-engine</artifactId>
	    <version>5.8.2</version>
	    <scope>test</scope>
	</dependency>

	<dependency>
	    <groupId>org.projectlombok</groupId>
	    <artifactId>lombok</artifactId>
	    <version>1.18.26</version>
	    <scope>provided</scope>
	</dependency>

	<dependency>
		    <groupId>com.jslsolucoes</groupId>
		    <artifactId>ojdbc6</artifactId>
		    <version>11.2.0.1.0</version>
	</dependency>

  </dependencies>
  
  
  <build>
 	<plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.5.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
    </plugins>
 </build>
</project>
```



### 4. run

runs as maven build... 에서 goal에 넣거나(아래 명령어에서 mvn을 뗀다), cmd에서 실행시키기

1. 컴파일
   - `mvn compile`
   - compile
2. 단위 테스트
   - `mvn test`
   - test

3. 패키징
   - `mvn package`
   - `mvn clean`
     - target 폴더에 파일 삭제
   - `C:\Users\bizyoung93\.m2\repository\com\app\MavenTest\0.0.1-SNAPSHOT`

4. 배포
   - `mvn install`
   - install
   - maven의 로컬저장소
     - `C:\Users\bizyoung93\.m2\repository\com\app\MavenTest\0.0.1-SNAPSHOT` 에 있다.



- 빌드 중 테스트 생략하는 방법
  - 명령어 뒤에 `-DskipTests` 추가