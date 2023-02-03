# Data Manipulation Language - DML

## 1. 정의

DML은 데이터 조작 언어(Data Manipulation Language)의 약자로, DB 내부의 데이터를 조작하기 위해 사용하는 명령어를 의미한다.

DML에는 대표적으로 다음 3가지 명령이 속한다.

>일부 문서에서는 SELECT 명령도 DML로 분류하고 있지만, SELECT 명령은 DM에 직접 변화를 일으키는 명령이 아니므로 DML이 아니다.

1. INSERT
2. UPDATE
3. DELETE





### I. COMMIT과 ROLLBACK 

- `COMMIT`
- `ROLLBACK` 

DML 명령은 자동으로 영구 저장되지 않는다. 

COMMIT 명령을 통해 DB에 영구히 반영하거나, ROLLBACK을 통해 바로 직전에 COMMIT된 버전으로 복구할 수 있다.

최근의 많은 RDBMS에서는 AUTO COMMIT 기능을 제공하지만, 이는 매우 위험하므로 AUTO COMMIT 기능을 꺼 놓고 COMMIT 명령을 이용하자.



## 2. 종류

### 1) INSERT

- `INSERT INTO 테이블명 (column1, column2, ...) VALUES(value1, value2, ...); `
- `INSERT INTO 테이블명 VALUES(value1, value2 ...);`
  - 모든 컬럼에 넣을 value가 있을 경우 column을 명시하지 않아도 된다.

