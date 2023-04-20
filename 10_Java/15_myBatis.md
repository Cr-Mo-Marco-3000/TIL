# MyBatis

기본적으로 두 가지 라이브러리를 import해야 한다.

DB Driver

MyBatis

여러 개의 xml을 사용한다.

1) 환경설정 xml 파일  => `.properties` 인식

​								=> 2) sql 설정 xml 인식(테이블 당 한개씩 만든다.)

Naming Convention

1. 환경설정 xml: `configuration.xml`

2. sql설정 xml: `tableNameMapper.xml`



1번 xml 파일을 ServiceImpl에서 resource에 넣어 사용한다.



## 1. 

`mybatis.org`

myBatis의 장점

compile unchecked로 바꾸어서, try - catch 처리를 안 해줘도 된다.



## 2. 파일 설정

따라서, "."은 Java 클래스와 관련된 경로를 표시할 때 사용되고, "/"는 XML 문서와 관련된 경로를 표시할 때 사용됩니다. 이 두 가지 경로 표시 방법은 서로 호환되지 않으므로, 올바른 경로를 사용해야 합니다.