"""
1. python - DB 연결
외부 라이브러리 필요 => pymysql
"""

import pymysql

"""
2. sql 실행 절차

1) Python - MySQL 연결(host, user, password, db)
2) Cursor 생성
3) 작업 수행: select + DML => commit
4) 연결 해제: close
"""

"""
1) Python - MySQL 연결(host, user, password, db)
"""

# localhost는 나 자신을 의미한다.
conn = pymysql.connect(
    host="localhost", user="root", password="root1234", db="scott", charset="utf8"
)


"""
2) Cursor 생성
"""

cur = conn.cursor()


"""
3) 작업 수행: e.g. deptno = 10인 사원들의 모든 정보 출력
"""

"""
3-1) SELECT
"""

q = "SELECT * FROM emp WHERE deptno = 10"
cur.execute(q)

# cur 객체는 iterable하다
# null값은 None으로 출력된다.
for record in cur:
    print(record[0], record[1])


"""
3-2) INSERT: 50, PROGRAMMING, SUJI
"""

# 문자열로 들어가는 부분은 문자열 처리('')를 해야 함에 주의! =>
# q = "INSERT INTO dept(deptno, dname, loc) VALUES(50, 'PROGRAMMING', 'SUJI')"
# cur.execute(q)

# pymysql에서는 숫자와 문자열 모두 %s로 받는다! =>
q = "INSERT INTO dept(deptno, dname, loc) VALUES(%s, %s, %s)"
new_values = (60, "DEV", "SEOUL")
cur.execute(q, new_values)

conn.commit()


"""
4) 연결 해제
"""

conn.close()
