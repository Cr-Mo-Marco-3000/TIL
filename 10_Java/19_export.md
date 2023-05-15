# Export

## I. Eclipse를 활용한 Export

### 1. 실행 가능한 .jar export

File - Export - Runnable .jar Export 선택

Launch configuration에서 main 메서드를 선택한다.

- Library handling 설정
  1. Extract required libraries into generated JAR
     - 파일 내부에 필요한 라이브러리들을 .class, 즉 실행 가능한 형태로 모두 포함시킨다.
     - 실행 가능한 .jar 파일 이동이 자유롭지만, 용량이 커진다.
  2. Package required libraries into generated JAR
     - .jar 파일 내부에 필요한 라이브러리들을 .jar 형태로 저장한다.
     - .jar 파일 내부에 .jar 파일은 원래는 실행이 불가능하지만, 이클립스에서는 이것이 가능하다.
  3. Copy required libraries into a sub-folder next to the generated JAR
     - 필요한 라이브러리들을 .jar 파일이 저장되는 디렉터리의 하위 폴더에 저장한다.
     - .jar 파일을  실행하기 위해서는 해당 폴더도 같이 가지고 가야 한다.

## II. Maven을 활용한 build

> 자세한 내용은 17_build.md를 참조

maven의 build 중 package를 통해 .jar 파일을 만들 수 있다.

다만, 필요한 라이브러리를 모두 포함하기 위해서는 dependency를 잘 설정해야 한다.



## III. 실행

- 터미널에 다음 명령어를 입력한다.
  - `java -jar jarFileName.jar` 