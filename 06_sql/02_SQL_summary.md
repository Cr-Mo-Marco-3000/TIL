# Database

[toc]

## 1. SQL 개념

> SQL(StructuredQueryLanguage)는 관계형 데이터베이스 관리시스템(RDBMS)의데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.



**SQL 문법의 세가지 종류**

- **DDL - 데이터 정의 언어**
  - CREATE
  - DROP
  - ALTER
- **DML - 데이터 조작 언어**
  - INSERT
  - UPDATE
  - DELETE
  - SELECT
- DCL - 데이터 제어 언어
  - GRANT
  - REVOKE
  - COMMIT
  - ROLLBACK



## 2. Database 생성

> 해당하는 데이터베이스 파일이 있으면 해당DB를 콘솔로 연다. 
>
> 만약 해당하는 파일이 없으면 새로 생성하고, 해당 DB를 콘솔로 연다.

```sqlite
$ sqlite3 database

ex)
$ sqlite3 tutorial.sqlite3    -- 1. 콘솔로 DB를 열고,
sqlite> .databases            -- 2.데이터베이스 목록을 확인한다.
```



**CSV 파일 불러오는 명령어**

> 주의사항)
>
> `.`으로 시작하는 모든 명령어는 SQLite에서 데이터베이스를 조금 더 편리하게 다루기 위해 제공하는 명령어이며, SQL 문법에 속하지 않는다.

```sqlite
sqlite> .mode csv
sqlite> .import 파일명.csv 테이블명

ex)
sqlite> .import users.csv users_user -- users.csv 파일을 users_user 테이블에 전부 집어 넣겠다.
```



## 3. 테이블 생성 및 삭제 

> 데이터 타입의 종류는 INTEGER, TEXT, REAL, NUMERIC, BLOB 등이 존재한다.
>
> 자세한 내용은 [SQLite3 공식문서](https://sqlite.org/datatype3.html)를 참조한다.



**테이블 생성 (CREATE)**

- 주의사항: PRIMARY KEY 설정을 할 때는, 스키마에 반드시 INTEGER라고 해야 함!
  - INT라고 하면 안됨!!!

```sql
CREATE TABLE table (
  column1 datatype PRIMARY KEY,
  column2 datatype,
  ...
);
```



**테이블 생성 with NOT NULL 조건 예시**

- 데이터베이스에서는 기본적으로, 빈 값은 허용하지 않는 게 원칙!

  - 빈 문자열이라도 들어가야 함!

  - 스키마에 NOT NULL 속성 활용

- SQLite는 기본적으로 key값을 재사용한다.

  - 예를 들어 pk가 5번까지 있는 table에서, 5번 record를 삭제한 후, 하나를 추가하면 pk가 5인 값이 생성되는 식이다.

  - 이를 방지하기 위해서는, PRIMARY KEY에 AUTOINCREMENT Option을 추가해야 한다.
  - AUTOINCREMENT Option은 지워진 데이터의 재사용 여부를 지정한다.

- Django에서는, AUTOINCREMENT 옵션이 기본값이다.

```sql
CREATE TABLE table (
  id INTEGER PRIMARY KEY, -- AUTOINCREMENT Option은 지워진 데이터의 재사용 여부, 이전에 삭제된 값의 pk를 다시 사용하지 않는다.
  name TEXT NOT NULL,
  age INT NOT NULL,
  ...
);
```

 

**테이블 및 스키마 조회 명령어** **(!= SQL 명령어 아님)**

```sqlite
sqlite> .tables          -- 테이블 목록 조회
sqlite> .schema table    -- 특정 테이블 스키마 조회
```



**테이블 제거 (DROP)**

```sql
sqlite> DROP TABLE classmates;
sqlite> .tables -- 테이블 제거 확인
```



## 4. 데이터 추가, 읽기, 수정 및 삭제

**추가 (INSERT)**

```sql
INSERT INTO table (column1, column2, ...)
VALUES(value1, value2);

-- 모든 열에 데이터가 있는 경우 column을 명시하지 않아도 됨!
INSERT INTO table VALUES(value1, value2 ...);

-- SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK옵션을 가진 rowid column을 정의!
-- 지정 없이 만들어보고 아래와 같이 해보면 나옴!
SELECT rowid, * FROM table;

-- id값을 직접 지정했을 경우, 차후 INSERT를 할 때, VALUES 뒤에 id를 포함한 모든 value를 작성하거나, 각 value에 맞는 column들을 명시적으로 작성해 주어야 한다.
```



**조회 (SELECT)**

> 참고)
>
> SQL은 세미콜론(;)을 만나기 전까지 절대 실행되지 않습니다.
>
> 따라서 아래 LIMIT 예시와 같이 들여쓰기를 비교적 자유롭게 할 수 있습니다.

```sql
-- 모든 컬럼 가져오기 --
SELECT * FROM table;

-- 특정 컬럼 가져오기 --
SELECT column1, column2 FROM table;

-- LIMIT: 원하는 개수(num)만큼 가져오기 -- 
SELECT column1, column2
FROM table
LIMIT num;

-- OFFSET: 특정 위치에서부터 가져올 때 --
-- (맨 위부터 num만큼 떨어진 값부터 가져온다는 의미)
SELECT column1, column2
FROM table
LIMIT num OFFSET num;

-- WHERE: 조건을 통해 값 가져오기 --
SELECT column1, column2
FROM table
WHERE column=value;

-- DISTINCT: 중복없이 가져오기 --
-- 어떤 컬럼에 값의 종류가 몇 개 있는지 알아볼 때 쓰인다.
SELECT DISTINCT column FROM table;
```



**삭제 (DELETE)**

```sql
-- 조건을 통해 특정 레코드 삭제
-- 하나의 레코드만 삭제하고 싶을 때, 고유값인 pk 많이 이용
DELETE FROM table
WHERE condition;

ex)	
DELETE FROM classmates
WHERE name='김싸피';
```



**수정 (UPDATE)**

- 얘도 주로 where 뒤에 pk값을 넣고는 한다(고유값이기 때문).

```sql
UPDATE table
SET column1=value1, column2=value2, ...
WHERE condition;

ex)
-- 김싸피의 이름을 김삼성으로 바꾼다고 하면... --
UPDATE classmates
SET name='김싸피', address='대한민국'
WHERE name='김삼성';
```



**예시와 함께하는 WHERE문 심화 (READ)**

```sql
-- Q.users에서 age가 30이상인 사람만 가져온다면? --

SELECT * FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상인 사람의 이름만 가져온다면? --

SELECT first_name FROM users
WHERE age >= 30;
```

```sql
-- Q.users에서 age가 30이상이고 성이 김인 사람의 성과 나이만 가져온다면? --
SELECT age, last_name FROM users
WHERE age >= 30 and last_name='김';
```



## 5. 심화 SQL문

### Aggregate Function

- 집계 함수
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결괏값을 반환하는 함수
- SELECT 구문에서만 사용됨

#### Expressions

- COUNT (레코드 값들의 개수 반환)

  ```sql
  SELECT COUNT(*) FROM users;
  ```

- 아래 함수들은 기본적으로 해당 컬럼이 숫자(INTEGER)일 때만 사용 가능

  - AVG (레코드 값들의 평균값 반환)

    ```sql
    SELECT AVG(age)
    FROM users
    WHERE age >= 30;
    ```

  - MAX (레코드 값들의 최대값 반환)
  - MIN (레코드 값들의 최소값 반환)
  - SUM (레코드 값들의 합 반환)




### LIKE

- query data based on pattern matching
- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards를 제공



> Wildcard Character

- 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
  - *, ? 등
- 주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임
- 텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자로, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자
- 지정된 패턴 일치를 기반으로 데이터를 수집하는 데도 도움이 될 수 있음



> LIKE는 두 가지 와일드 카드(언더스코어 그리고 퍼센트 기호)와 함께 동작한다.

- `-` (반드시 이 자리에 한 개의 문자가 존재해야 한다는 뜻)

  ```sql
  -- 20대인 사람들만 가져올 때 --
  SELECT *
  FROM users
  WHERE age LIKE '2_';
  ```

- `%` (이 자리에 문자열이 있을 수도, 없을 수도 있다. 0개 이상이라는 뜻)

  ```sql
  -- 지역번호가 02인 사람만 가져올 때 --
  SELECT *
  FROM users
  WHERE phone LIKE '02-%';
  ```

- 두 개를 조합해서 사용할 수도 있다.

  ```sql
  -- 핸드폰 중간 번호가 반드시 4자리면서 511로 시작되는 사람들 --
  
  SELECT * FROM users
  WHERE phone LIKE '%-511_-%';
  ```



**정렬 (ORDER BY)**

```sql
SELECT columns FROM table
ORDER BY column1, column2 ASC / DESC;

-- ASC: 오름차순 / DESC: 내림차순 --
```

```sql
-- 나이 내림차순, 성 순서로 오름차순 정렬하여 상위 10개만 뽑아보면? --
SELECT * 
FROM users
ORDER BY age DESC, last_name ASC -- 2개 이상의 정렬 기준을 갖는 경우 ,로 분리 가능하며 ASC는 기본값이기 때문에 생략 가능합니다.
LIMIT 10;
```



**GROUP BY**

- 행 집합에서 요약 행 집합을 만듦
- SELECT문의 optional 절

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 문장에 WHERE 절이 포함된 경우, 반드시 WHERE 절 뒤에 작성해야 함



> 지정된 기준에 따라 행 세트를 그룹으로 결합한다.
>
> 데이터를 요약하는 상황에서 주로 사용한다.

```sql
SELECT column1, aggregate_function(column_2)
FROM table
GROUP BY column1, column2;
```

```sql
-- 성(last_name)씨가 몇 명인지 조회할 때 --
-- AS 구문을 통해 요약되는 컬럼의 이름을 변경할 수 있습니다.
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
```



**ALTER**

- 총 4 가지 기능
  1. table 이름 변경
  2. 테이블에 새로운 column 추가
  3. column 이름 수정(3.25버전부터)
  4. column 삭제(3.35버전부터)

- 테이블명 변경

  ```sql
  ALTER TABLE 기존테이블명
  RENAME TO 새로운테이블명;
  ```

- 새로운 컬럼 추가

  ```sql
  ALTER TABLE 테이블명
  ADD COLUMN 컬럼명 datatype;
  
  -- ALTER TABLE articles ADD COLUMN created_at TEXT NOT NULL;
  -- 하면 실패!
  
  -- 왜냐하면 기존에 있는 레코드들에는 새로 추가할 필드에 대한 정보가 없음! 따라서 NOT NULL형태의 컬럼은 추가 불가!
  -- 해결방법 
  -- 1. NOT NULL 설정 없이 추가 
  -- 2. 기본값(DEFAULT) 설정
  
  -- ALTER TABLE articles ADD COLUMN created_at TEXT NOT NULL DEFAULT '생성날짜'
  -- 기본값이 설정 됨!
  ```
  
- 컬럼 이름 변경

  ```sql
  ALTER TABLE 테이블명
  RENAME COLUMN 컬럼명 TO 새로운테이블명;
  ```

- 컬럼 삭제

  ```sql
  ALTER TABLE 테이블명
  DROP COLUMN 컬럼명;
  ```

  