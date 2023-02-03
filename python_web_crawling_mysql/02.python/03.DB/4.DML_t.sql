-- 8.DML.sql
/* 
- DML : Data Mainpulation Language
            데이터 조작 언어
	   (select/insert/update/delete 모두 다 DML)
		- 이미 존재하는 table에 데이터 저장, 수정, 삭제, 검색
	   
- *** : commit : 영구저장, rollback : 복원 문장 필수
- *** : tip - app 개발시 db에 insert한 데이터는 반드시 commit 필수 

- 영구 저장 조건
	1. insert/update/delete 문장에만 영향을 줌
	2. sql문장을 실행시킨 프로그램상에서만 영향을 줌(DML 작업한 sw상에서만 commit / rollback 유효)
	3. 가급적 sql문장 backup시 insert 문장이 있을 경우 습관적으로 마지막에 commit; 필수(*)
	4. 저장시 : commit
	   복원시 : rollback
	
- 참고 : sql 작업을 편리하게 지원하는 tool들은 auto commit 기능 내포

- CRUD : create/read/update/delete
		insert/select/update/delete

*** 용어 정리 ***
	1. select : 검색 = query = 질의
	2. insert/update/delete = dml
	1+2 = sql				
	
1. insert sql문법
	1-1. 모든 칼럼에 데이터 저장시 
		-table 구조상의 컬럼 순서에 맞게 모든 데이터 저장시 사용하는 
		-
		insert into table명 values(데이터값1, ...)

	1-2.  특정 칼럼에만 데이터 저장시,
		명확하게 칼럼명 기술해야 할 경우 
		insert into table명 (칼럼명1,...) values(칼럼과매핑될데이터1...)

	1-3. 하나의 sql문장으로 다수의 table에 데이터 입력 방법
		insert all 
			into table명 [(칼럼명,...)] values(데이터,,,)		
		select 검색칼럼 from....;

2. update 
	2-1. 모든 table(다수의 row)의 데이터 한번에 수정
		- where조건문 없는 문장
		- update table명 set 칼럼명=수정데이타;

	2-2. 특정 row값만 수정하는 방법
		- where조건문으로 처리하는 문장
		- update table명 set 칼럼명=수정데이타 where 조건sql;
*/


-- *** insert ****
-- 1. 칼럼명 기술없이 데이터 입력



-- 2. 칼럼명 기술후 데이터 입력 
-- 선언된 컬럼 순서에 맞게 데이터 저장 가능



-- 3. 다중 table에 한번에 데이터 insert하기 
-- 이미 존재하는 table의 데이터를 기반으로 다수의 table에 insert하기



-- 4. ? 부서 번호가 10인 데이터는 emp01에 저장, 
-- 부서 번호가 20 or 30인 데이터는 emp02에 저장
-- 조건 표현 : when~then
-- 데이터만 삭제 - rollback으로 복구 불가능한 데이터 삭제 명령어



-- ? 주변 분 정보 emp02/ 내 정보는 emp01



-- *** update ***
-- 1. 테이블의 모든 행 변경



-- 30이전의 데이터로 복원



-- 2. emp01 table의 모든 사원의 급여를 10%(sal*1.1) 인상하기




-- ? emp table로 부터 empno, sal, hiredate, ename 순으로 table 생성




-- 3. emp01의 모든 사원의 입사일을 오늘로 바꿔주세요



-- 4. 급여가 3000이상인 사원의 급여만 10%인상



-- 5.? emp01 table 사원의 급여가 1000이상인 사원들의 급여만 500원씩 삭감 



-- 6. emp01 table에 DALLAS(dept의 loc)에 위치한 부서의 소속 사원들의 급여를 1000인상



-- 7. emp01 table의 SMITH 사원의 부서 번호를 30으로, 직급은 MANAGER 수정



-- *** delete ***
-- 8. 하나의 table의 모든 데이터 삭제



-- 9. 특정 row 삭제(where 조건식 기준)
-- emp01 에서 10번만 삭제



-- 10. emp01 table에서 comm 존재 자체가 없는(null) 사원 모두 삭제



-- 11. emp01 table에서 comm이 null이 아닌 사원 모두 삭제



-- 12. emp01 table에서 부서명이 RESEARCH 부서에 소속된 사원 삭제 



-- 13. table내용 삭제



