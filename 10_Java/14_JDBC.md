# JDBC

> Java Database Connectivity

1. JAVA와 DBMS(오라클, mysql...) 연동기술(Web 포함)
2. JAVA에서 인터페이스를 만들어 일관된 방법으로 DB에 접속할 수 있게 함
3. 자바에서 제공해준 인터페이스를 implements 받아서 각 벤더에서, 자사의 DB를 연동시킬 수 있는 드라이버를 만듦
4. 드라이버(`.jar`)를 사용하도록 build path를 해야 된다.

인터넷에서 각 DB별 버전에 맞는 드라이버를 찾아 설치요

## 1. 오라클

오라클 같은 경우에는, 오라클을 설치할 때 드라이버를 포함하고 있다.

`C:\oraclexe\app\oracle\product\11.2.0\server\jdbc`

`.jar` 파일 중 하나를 선택해서 쓰면 된다.



## 2. 연동

### 1. build path

프로젝트 우클릭 후 build path - configure build path - library - add external library



### 2. 4가지 정보 기입

`String driver =  "oracle.jdbc.driver.OracleDriver";`

`String url = "jdbc:oracle:thin:@localhost:1521:serviceName";`

- @뒤에는 ip address와 포트번호 필요 & 방화벽 해제 필요

`String id = "SCOTT";`

`String ps = "TIGER";`

- 전처리
  - 오라클에서 예시로 제공해주는 SCOTT 계정과 테이블을 저장해서 사용한다.

`C:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin\scott.sql`

```sql
-- 외부파일 읽어서 실행하기
@C:\oraclexe\app\oracle\product\11.2.0\server\rdbms\admin\scott.sql
```



### 3. 드라이버 로딩

`Class.forName(driver);`

**자체적으로 throw를 하는 클래스이므로, 예외처리가 필수이다.**

[참고](https://docs.oracle.com/javase/8/docs/api/)

OracleDriver 클래스를 객체 생성(드라이버 로딩) 필요

그런데 해당 클래스는 문자열로 되어 있다.



### 4. 연결(make connection)

Connection은 인터페이스이기때문에 new를 사용하면 안된다.

java.sql에서 필요한 클래스 import

`Connection con = DriverManager.getConnection(url, id, pw);`



### 5. SQL 작성

일반 SQL과 동일하게 작성

단, `;` 제외

`String sql = "SELECT * FROM Dept";`

또 where 절을 쓸 때는,  값이 들어가는 부분을 ?로 치환한 후, setInt나 setString을 통해 넣어주어야 한다.

?의 위치는 1부터 시작한다.

`where id = ?`

`pstmt.setInt(위치, 값);`

### 6. SQL을 전송하기 위한 클래스

PreparedStatement: 인터페이스

`PreparedStatement pstmt = con.prepareStatement(sql);`

여러 쿼리를 날릴 때 서로 다른 메서드를 쓴다.

- `pstmt.execute();` 
  - CREATE

- `ResultSet rs = pstmt.executeQuery();`
  - SELECT

- `int n = pstmt.executeUpdate();`
  - INSERT, DELETE, UPDATE
  - 리턴되는 n값은 실제 적용된 행의 개수

- rs에서 값을 읽어들이는 방법

  - 포인터를 이용해, 각 행은 `.next()`를 사용해서 가리킨다.
    - 값이 있으면 true, 없으면 false()를 반환
  - `rs.getInt("컬럼헤더");`

  - `rs.getString("컬럼헤더");`
  - 단, 여기서 컬럼헤더는, DB상의 컬럼명이 아니라, 내 SELECT에서 뽑혀져나온 컬럼명이다.
  - 컬럼헤더 대신 숫자(1, 2, 3, ...)이 들어갈수도 있다.

```java
package p01;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class SelectTest {

	public static void main(String[] args) {
		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String id = "SCOTT";
		String pw = "TIGER";
		
		
		// 각 클래스가 반환하는 예외에 맞추어 예외처리 필요
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		
		// finally에서 해제하기 위해 초기화를 여기서
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DriverManager.getConnection(url, id, pw);			
			String sql = "SELECT * FROM Dept";	// ; 제외
			pstmt = con.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				System.out.println(rs.getInt("deptno"));
				System.out.println(rs.getString(2));
				System.out.println(rs.getString("loc"));
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				// 역순으로 close()
				if (rs!=null) rs.close();
				if (pstmt!=null) pstmt.close();
				if (con!=null) con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		
	}

}

```



### 7. 사용했던 자원 역순으로 close()



### 8. INSERT

위의 1부터의 과정을 그대로 하되, 약간의 차이가 있다.

INSERT를 할 때, 값이 있는 부분은 ?로 처리한 후, 

setInt등을 통해 값을 넣어주어야 한다.

위치는 1부터 시작한다.

`pstmt.setInt(위치, 값);`

`pstmt.setString(위치, 값);`

마지막으로

`int n = executeUpdate();`

**자바는 autocommit이다.**



```java
package p01;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class InsertTest {

	public static void main(String[] args) {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String id = "SCOTT";
		String pw = "TIGER";
		
		
		// 각 클래스가 반환하는 예외에 맞추어 예외처리 필요
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		
		// finally에서 해제하기 위해 초기화를 여기서
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DriverManager.getConnection(url, id, pw);			
			String sql = "INSERT INTO dept ( deptno, dname, loc ) "
					+ "values ( ?, ?, ? )";	// ; 제외
			pstmt = con.prepareStatement(sql);
			
			pstmt.setInt(1, 50);
			pstmt.setString(2, "개발");
			pstmt.setString(3, "서울");
			
			int n = pstmt.executeUpdate();
			System.out.println(n + "개가 저장되었습니다");
			
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				// 역순으로 close()
				if (rs!=null) rs.close();
				if (pstmt!=null) pstmt.close();
				if (con!=null) con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}

	}

}

```

### 9. UPDATE

```java
package p01;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class InsertTest {

	public static void main(String[] args) {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String id = "SCOTT";
		String pw = "TIGER";
		
		
		// 각 클래스가 반환하는 예외에 맞추어 예외처리 필요
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		
		// finally에서 해제하기 위해 초기화를 여기서
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DriverManager.getConnection(url, id, pw);			
			String sql = "UPDATE Dept "
					+ " set dname =?, loc=? "
					+ " where deptno=? ";
			
			pstmt = con.prepareStatement(sql);
			
			pstmt.setString(1, "인사");
			pstmt.setString(2, "제주");
			pstmt.setInt(3, 50);
			
			int n = pstmt.executeUpdate();
			
			System.out.println(n + "개가 수정되었습니다");
			
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				// 역순으로 close()
				if (rs!=null) rs.close();
				if (pstmt!=null) pstmt.close();
				if (con!=null) con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}

	}

}

```

### 10. DELETE

```java
package p01;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DeleteTest {

	public static void main(String[] args) {
		

		String driver = "oracle.jdbc.driver.OracleDriver";
		String url = "jdbc:oracle:thin:@localhost:1521:xe";
		String id = "SCOTT";
		String pw = "TIGER";
		
		
		// 각 클래스가 반환하는 예외에 맞추어 예외처리 필요
		try {
			Class.forName(driver);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		
		// finally에서 해제하기 위해 초기화를 여기서
		Connection con = null;	
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DriverManager.getConnection(url, id, pw);			
			String sql = "DELETE FROM Dept WHERE Deptno=?";
	
			pstmt = con.prepareStatement(sql);
			
			pstmt.setInt(1, 50);
			
			int n = pstmt.executeUpdate();
			
			System.out.println(n + "개가 삭제되었습니다");
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			try {
				// 역순으로 close()
				if (rs!=null) rs.close();
				if (pstmt!=null) pstmt.close();
				if (con!=null) con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
}

```



## 3. 클래스 분리

DTO(data transfer object) 패턴 

DTO 객체에 하나의 행을 넣어서 DB를 처리하는 방식.



## 클래스 구조

![dto_pattern](C:\Users\bizyoung93\Desktop\TIL\10_Java\14_JDBC.assets\dto_pattern.png)