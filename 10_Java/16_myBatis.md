# MyBatis

`mybatis.org`

JDBC대신 DB 입출력을 편리하게 하기 위해서 사용하는 xml기반 라이브러리

- 장점
  - compile unchecked로 바꾸어서, try - catch 처리를 안 해줘도 된다.

**사용하려면 프로젝트에 두 가지 라이브러리를 import해야 한다.**

1. DB Driver(각 DB마다 제공해준다.)

2. MyBatis



### 주의점

- myBatis는 jdbc와는 달리, 명시적인 commit()이 반드시 필요하다.



## 1. 기본 사용

- 기본적으로 여러 개의 xml을 사용한다.

1) 환경설정 xml 파일  => 환경 변수(`.properties`) 인식
   - 이 xml 파일을 ServiceImpl에서 resource에 넣어 사용한다.
2) sql 설정 xml 인식(테이블 당 한개씩 만든다.)

- Naming Convention

  1. 환경설정 xml: `configuration.xml`


  2. sql설정 xml: `tableNameMapper.xml`

- 경로 표시 주의사항
  - "."은 Java 클래스와 관련된 경로를 표시할 때 사용되고, "/"는 XML 문서와 관련된 경로를 표시할 때 사용됩니다. 
  - 이 두 가지 경로 표시 방법은 서로 호환되지 않으므로, 올바른 경로를 사용해야 합니다.

### 1. 설정 패키지

- jdbc.properties
  - db에서 쓸 환경 변수를 저장한다.

```properties
# comment
# key=value 
jdbc.driver=oracle.jdbc.driver.OracleDriver
jdbc.url=jdbc:oracle:thin:@localhost:1521:xe
jdbc.userid=SCOTT
jdbc.passwd=TIGER


```

- Configuration.xml
  - 위에서 저장한 환경 변수를 등록

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
	
  <!-- jdbc.properties 파일 등록 -->	
  <properties resource="com/mybatis/jdbc.properties"></properties>
  
  <environments default="development">
    <environment id="development">
      <transactionManager type="JDBC"/>
      
      <!-- 각 환경변수들을 property tag에 추가한다. -->
      <dataSource type="POOLED">
        <property name="driver" value="${jdbc.driver}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.userid}"/>
        <property name="password" value="${jdbc.passwd}"/>
      </dataSource>
      
    </environment>
  </environments>
  <!-- 아래에는, 매퍼들을 추가한다. -->
  <!-- 각 매퍼들에는, 한 테이블의 쿼리들이 들어간다. -->
  <mappers>
    <mapper resource="com/mybatis/DeptMapper.xml"/>
    <mapper resource="com/mybatis/DeptMapper2.xml"/>
  </mappers>
</configuration>
```

- DeptMapper.xml
  - 각 쿼리를 지정해주는 태그들이 존재한다.
  - parameterType과 resultType을 지정해준다.
  - 해당 매퍼를 특정 패키지화 하고싶다면, namescape에 적어준 후, DAO에서 이를 명시하여 사용한다.
  - DTO에 getters와 setters가 필수적인 이유가, 여기서 써서 그렇다.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!-- namescape는 mapper를 지정하는 패키지 역할 -->  
<mapper namespace="com.dept.DeptMapper">
  
  <!-- mapper tage 사이에, 각 쿼리 태그들이 들어간다.-->
  <!-- 즉, dao에서 했던 것들이 들어간다. -->
  <!-- ;도, "도 없음에 주의-->
  <!-- resultType은 거의 select에서만 쓴다 -->
  <!-- 즉, 정보가 제대로 처리됐는지 알려주는 n은 myBatis가 알아서 처리해준다. -->
  <select id="findAll" resultType="com.dto.DeptDTO">	<!-- id에는 해당 쿼리를 소환할 이름 ,resultType에는 해당 쿼리의 반환 형식을 지정한다.-->		
    select deptno, dname, loc 							<!-- 해당 객체의 setter 메서드와 일치시켜주어야 한다. => * 도 일치하기만 하면 됨 -->
    from Dept											<!-- 즉, getter와 setter는 필수! -->
  </select>
  
  <select id="findAllDesc" resultType="com.dto.DeptDTO">
    select * 
    from Dept
    order by deptno desc
  </select>
  
  <select id="findByDeptno" parameterType="int" resultType="com.dto.DeptDTO">
    select *
    from Dept
    where deptno = #{deptno}
  </select>
  
  <!-- 저장 -->
  <!-- DeptDTO에 있는 getter 메서드명을 가져와서 #{변수명}에 치환 -->
  <!-- parameter는 DeptDTO, HashMap 등 하나에 뭉쳐서 전달해야 한다.-->
  <insert id="insert" parameterType="com.dto.DeptDTO">
	INSERT INTO dept ( deptno, dname, loc )
	values ( #{deptno}, #{dname}, #{loc} )
  </insert>
  
  <!-- update -->
  <update id="update" parameterType="com.dto.DeptDTO">
	update dept
	set dname=#{dname}, loc=#{loc}
	where deptno=#{deptno}
  </update>
  
  <!-- 삭제
  	자바코드에서 전달한 int deptno에 값을 가져와서 #{deptno}에 치환하고
  	전달 타입을 parameterType에 지정한다.
   -->
  <delete id="delete" parameterType="int">
	DELETE FROM dept
	where deptno=#{deptno}
  </delete>
  
</mapper>
```

- DeptMapper2.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!-- namescape는 mapper를 지정하는 패키지 역할 -->  
<mapper namespace="com.dept.DeptMapper2">
  
  <!-- mapper tag 사이에, 각 쿼리 태그들이 들어간다.-->
  <!-- 즉, dao에서 했던 것들이 들어간다. -->
  <!-- ;도, "도 없음에 주의-->
  <!-- resultType은 거의 select에서만 쓴다 -->
  <!-- 즉, 정보가 제대로 처리됐는지 알려주는 n은 myBatis가 알아서 처리해준다. -->
  <select id="findAll" resultType="com.dto.DeptDTO">	<!-- id에는 해당 쿼리를 소환할 이름 ,resultType에는 해당 쿼리의 반환 형식을 지정한다.-->		
    select deptno, dname, loc 							<!-- 해당 객체의 setter 메서드와 일치시켜주어야 한다. => * 도 일치하기만 하면 됨 -->
    from Dept											<!-- 즉, getter와 setter는 필수! -->
  	order by deptno desc
  </select>
  <!-- <if test="조건"> 조건이 참이면 여기가 실행 </if> --> 

</mapper>
```



### 2. DTO 패키지

- 하나의 부서정보를 담은 객체를 나타낸다.
- 테이블당 하나가 생성되겠지?

```java
package com.dto;

public class DeptDTO {

	// 관례적으로 table의 컬럼명을 변수명으로 둔다.
	int deptno;
	String dname;
	String loc;
	
	//constructor
	public DeptDTO() {}

	public DeptDTO(int deptno, String dname, String loc) {
		this.deptno = deptno;
		this.dname = dname;
		this.loc = loc;
	}
	
	// getters & setters
	public int getDeptno() {
		return deptno;
	}

	public void setDeptno(int deptno) {
		this.deptno = deptno;
	}

	public String getDname() {
		return dname;
	}

	public void setDname(String dname) {
		this.dname = dname;
	}

	public String getLoc() {
		return loc;
	}

	public void setLoc(String loc) {
		this.loc = loc;
	}
	
	// toString
	@Override
	public String toString() {
		return "DeptDTO [deptno=" + deptno + ", dname=" + dname + ", loc=" + loc + "]";
	}
}

```



### 3. Main 패키지

- DeptMain.java
  - service - Dao를 통해 DB와 소통하되, DTO를 주고받으며 이를 출력하거나, 사용한다.

```java
import java.util.List;
import java.util.Scanner;

import com.dto.DeptDTO;
import com.service.DeptService;
import com.service.DeptServiceImpl;

import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;


public class DeptMain {

	public static void main(String[] args) {
		
		while (true) {
			Scanner scan = new Scanner(System.in);
			System.out.println("1. 전체목록");
			System.out.println("2. 부서저장");
			System.out.println("3. 부서수정");
			System.out.println("4. 부서삭제");
			System.out.println("0. 종료");
			System.out.println("---------------------");
			String num = scan.nextLine();
			if ("1".equals(num)) {
				DeptService service = new DeptServiceImpl();
				
				List<DeptDTO> list = service.findAll();
				
				System.out.println("부서번호 \t 부서명 \t 부서위치");
				System.out.println("---------------------------");
				
				for (DeptDTO dto : list) {
					System.out.println(dto);
				}
			
			} else if (num.equals("2")) {
				System.out.println("부서의 번호는?");
				String deptno = scan.nextLine();
				System.out.println("부서의 이름은?");
				String dname = scan.nextLine();
				System.out.println("부서의 위치는?");
				String loc = scan.nextLine();

				DeptServiceImpl service =  new DeptServiceImpl();
				int n=0;
				try {
					n = service.insert(new DeptDTO(Integer.parseInt(deptno), dname, loc));
				} catch (DuplicatedDeptnoException e) {
					System.out.println(e.getMessage());
				}
				System.out.println(n + "개가 정상적으로 저장되었습니다.");
			} else if (num.equals("3")) {
				System.out.println("부서의 번호는?");
				String deptno = scan.nextLine();
				System.out.println("부서의 이름은?");
				String dname = scan.nextLine();
				System.out.println("부서의 위치는?");
				String loc = scan.nextLine();
				
				DeptServiceImpl service =  new DeptServiceImpl();
				int n=0;
				try {
					n = service.update(new DeptDTO(Integer.parseInt(deptno), dname, loc));
				} catch (RecordNotFoundException e) {
					System.out.println(e.getMessage());
				}
				System.out.println(n + "개가 정상적으로 수정되었습니다.");
			} else if (num.equals("4")) {
				System.out.println("삭제할 부서번호를 입력하세요");
				String deptno = scan.nextLine();
				DeptServiceImpl service = new DeptServiceImpl();
				int n = 0;
				try {
					n = service.delete(Integer.parseInt(deptno));
				} catch (RecordNotFoundException e) {
					System.out.println(e.getMessage());
				}
				System.out.println(n + "개가 삭제되었습니다.");
			}
		}
	}
}

```

### 4. Service 패키지

- Service.java
  - 각 쿼리를 실행하는 service 메서드의 인터페이스를 담은 파일

```java
package com.service;

import java.util.List;

import com.dto.DeptDTO;
import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;

public interface DeptService {
	
	public abstract List<DeptDTO> findAll() ;
	public int insert(DeptDTO dto) throws DuplicatedDeptnoException;
	public int update(DeptDTO dto) throws RecordNotFoundException;
	public int delete(int deptno) throws  RecordNotFoundException;
}

```

- ServiceImpl.java

  - Dao와 Main을 이어주는 역할

  - DTO Pattern에서는 connection을 생성해서 Dao에 넘겨준 후, 객체를 받아 처리했지만 여기서는 session을 생성 후, 이를 넘겨주어 처리한다.
  - session을 `.close()`해주는 걸 잊지 말자

```java
package com.service;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.dao.DeptDAO;
import com.dto.DeptDTO;
import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;

public class DeptServiceImpl implements DeptService {
	
	/////////////////////////////////////
	// Connection 역할의 SqlSession을 얻기 //
	// 프로그램 실행시 static 블럭이 실행된다.  //
	/////////////////////////////////////
	static SqlSessionFactory sqlSessionFactory;
	
    // 프로그램 실행시 초기화 블록이 실행된다.
	static {
		String resource = "com/mybatis/Configuration.xml";	// 설정 파일이 들어간다.
		InputStream inputStream = null;
		try {
			inputStream = Resources.getResourceAsStream(resource);
		} catch (IOException e) {
			e.printStackTrace();
		}
		sqlSessionFactory =
		  new SqlSessionFactoryBuilder().build(inputStream);
	}
	
	// 일관된 형태의 반복
	/*
		SqlSession session = sqlSessionFactory.openSession();
		try {
			
		} finally {
			session.close();
		}	 
	*/
    
	@Override
	public List<DeptDTO> findAll() {
		// 아래 있는 session이 JDBC의 Connection 역할
		SqlSession session = sqlSessionFactory.openSession();
		List<DeptDTO> list = null;
		try {
			DeptDAO dao = new DeptDAO();
			list = dao.findAll(session);
		} finally {
			session.close();
		}
		return list;
	}
	
	
	@Override
	public int insert(DeptDTO dto) throws DuplicatedDeptnoException {
		SqlSession session = sqlSessionFactory.openSession();
		int n = 0;
		try {
			DeptDAO dao = new DeptDAO();
			n = dao.insert(session, dto);
			// mybatis는 jdbc와 달리 명시적으로 commit이 필요하다.
			session.commit();
		} catch(Exception e) {
			throw new DuplicatedDeptnoException(dto.getDeptno() + "가 중복되었습니다.");
		} finally {
			session.close();
		}
		return n;
	}
	
	@Override
	public int update(DeptDTO dto) throws RecordNotFoundException {
		SqlSession session = sqlSessionFactory.openSession();
		int n = 0;
		try {
			DeptDAO dao = new DeptDAO();
			n = dao.insert(session, dto);
			// mybatis는 jdbc와 달리 명시적으로 commit이 필요하다.
			if (n == 0) {
				// 출력은 기본적으로 다 main에서
				throw new RecordNotFoundException(dto.getDeptno() + "번호가 없습니다.");
			}
			session.commit();
		} finally {
			session.close();
		}
		
		return n;
	}
	
	@Override
	public int delete(int deptno) throws RecordNotFoundException{
		SqlSession session = sqlSessionFactory.openSession();
		int n = 0;
		try {
			DeptDAO dao = new DeptDAO();
			n = dao.delete(session, deptno);
			// mybatis는 jdbc와 달리 명시적으로 commit이 필요하다.
			if (n == 0) {
				// 출력은 기본적으로 다 main에서
				throw new RecordNotFoundException(deptno + "번호가 없습니다.");
			}
			session.commit();
		} finally {
			session.close();
		}
		return n;
	};
}

```

### 5. DeptDAO 패키지

- 단순해진다.
- 첫 번째 인자로 service에서 session을 넘겨받은 후, 두 번째 인자부터 쿼리에 집어넣는다.

```java
package com.dao;	// com.repository로 줄 수도

import java.util.List;

import org.apache.ibatis.session.SqlSession;

import com.dto.DeptDTO;

import com.exception.DuplicatedDeptnoException;;

public class DeptDAO {
	
	public List<DeptDTO> findAll(SqlSession session) {
		
		// 1) crud
		// . 뒤에틑 crud를 설정했던 태그명이 들어간다.
		// int n = session.insert("mapper의 id값", parameter");
		// int n = session.delete(null, session);
		// int n = session.update(null, session);
		
		// 2) selectList
		// 결과가 여러개 => 자동으로 list에 담겨 반환
		// resultType이 <>에 들어간다.
		// List<DeptDTO> list = session.selectList("id값");
		// List<DeptDTO> list = session.selectList("id값", 파라미터);
		// List<DeptDTO> list = session.selectList("id값", 파라미터, RowBounds);
		
        // 3) select
		// 결과가 하나
		// DeptDTO dto = session.selectOne("id값");
		// DeptDTO dto = session.selectOne("id값", 파라미터);
		
		List<DeptDTO> list = session.selectList("com.dept.DeptMapper.findAll");
		
		return list;
		
	}
	
	// 발생하는 에러가 다 런타임계열이기에, throws를 할 필요가 없다. => 자동으로 상위로 넘어간다.
	public int insert(SqlSession session, DeptDTO dto) {
		int n = session.insert("com.dept.DeptMapper.insert", dto);
		return n;
	}
	
	public int update(SqlSession session, DeptDTO dto) {
		int n = session.update("com.dept.DeptMapper.update", dto);
		return n;
	}
	
	public int delete(SqlSession session, int deptno) {
		int n = session.update("com.dept.DeptMapper.delete", deptno);
		return n;
	}
}

```



### 6. Exception 패키지

- 예외처리를 위한 패키지

```java
package com.exception;

public class DuplicatedDeptnoException extends Exception {
	// generate constructors from superclass로 이어받아 생성
	public DuplicatedDeptnoException(String message) {
		super(message);
	}
	
}

```

```java
package com.exception;

public class RecordNotFoundException extends Exception {

	public RecordNotFoundException(String message) {
		super(message);
	}

}

```



## 2. 동적 sql

### 1. 설정 패키지

- Configuration
  - 별 차이 없다.

- Mapper
  - 동적인 sql를 적용하기 위해서, if 역할을 하는 `<if test="">`와 `<choose> - <when test =""> - <otherwise>`를 사용한다.
  - if를 사용할 때와 마찬가지로, 조건문 통과는 주의해야 한다.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.dept.DeptMapper">
  <!-- 1. selectDynamicDeptno -->
  <!-- parameterType에 들어갈 형식 컨벤션은 공식 사이트에서 구할 수 있다. -->
  <select id="selectDynamicDeptno" 
  		  parameterType="hashmap"
  		  resultType="com.dto.DeptDTO">
	  select deptno, dname, loc 
	  from dept
	  <!-- 만약 x가 존재하면, if태그 안에 있는 쿼리가 추가로 붙어서 실행된다. -->
	  <if test="x != null">where deptno = #{x}</if>
  </select>
  <!-- 2. selectDynamicChoose -->
  <select id="selectDynamicChoose" 
  		  parameterType="hashmap"
  		  resultType="com.dto.DeptDTO">
  	   SELECT deptno, dname, loc
  	   FROM dept
  	   <!-- if와 비슷한 형식으로 들어가게 된다. -->
  	   <!-- 순서를 주의하자, 먼저 해당 조건에 걸리면 if와 마찬가지로 뚫고 들어간다.-->
  	   <choose>
  	     <when test="dname != null and loc !=null">
 	       where dname = #{dname} and loc = #{loc}
 	     </when>
 	     <when test="loc != null">
 	       where loc = #{loc}
 	     </when>
 	     <when test="dname != null">
 	       where dname = #{dname}
 	     </when>
 	     <otherwise>
 	       order by deptno desc
 	     </otherwise>
	   </choose>
  </select>
</mapper>
```

### 2. DTO 패키지

- 차이 없다.

### 3. Main 패키지

```java
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

import com.dto.DeptDTO;
import com.service.DeptService;
import com.service.DeptServiceImpl;

import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;


public class DeptMain {

	public static void main(String[] args) {
		// 0. 공용으로 사용할 service 선언
		DeptService service = new DeptServiceImpl();
		
		// 1. selectDynamicDeptno ==> 반드시 컬렉션 또는 DTO에 저장해야 된다.
		// 아래 두 쿼리중에 동적으로 사용한다.
		/* 
		 * 1)
		 * select deptno, dname, loc
		 * from dept
		 * where deptno = 값;
		 * 
		 * 2)
		 * select deptno, dname, loc
		 * from dept;
		 * 
		 */
		
		int deptno = 20;
		HashMap<String, Integer> map = new HashMap<>();
		// 1)
		// 키에 Mapper에서 체크할 동적 인자가 들어간다.
		// map.put("x", deptno);
		// 2)
		map.put("deptno", null); //=> where이 없을때
		List<DeptDTO> list = service.selectDynamicDeptno(map);
		System.out.println(list);
		System.out.println("=========================================");
		
		
		// 2. selectDynamicChoose
		// 값을 검색하는데, 아래의 경우 중 하나로 찾는다.
		/*
	    select deptno,dname,loc
	    from dept
	    where dname = 값;   
	
	    select deptno,dname,loc
	    from dept
	    where loc = 값;
	
	    select deptno,dname,loc
	    from dept
	    where loc = 값 and(or) dname=값;
		*/
		HashMap<String, String> map2 = new HashMap<>();
		map2.put("loc", "dsfs");
		map2.put("dname", "삼진");
		List<DeptDTO> list2 = service.selectDynamicChoose(map2);
		System.out.println(list2);
		System.out.println("=========================================");
	}
}	


```



### 4. Service 패키지

- Service.java

```java
package com.service;

import java.util.HashMap;
import java.util.List;

import com.dto.DeptDTO;
import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;

public interface DeptService {
	
	public List<DeptDTO> selectDynamicDeptno(HashMap<String, Integer> map);
	public List<DeptDTO> selectDynamicChoose(HashMap<String, String> map);
}

```

- ServiceImpl.java

```java
package com.service;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import com.dao.DeptDAO;
import com.dto.DeptDTO;
import com.exception.DuplicatedDeptnoException;
import com.exception.RecordNotFoundException;

public class DeptServiceImpl implements DeptService {
	
	/////////////////////////////////////
	// Connection 역할의 SqlSession을 얻기 //
	// 프로그램 실행시 static 블럭이 실행된다.  //
	/////////////////////////////////////
	static SqlSessionFactory sqlSessionFactory;
	
	static {
		String resource = "com/mybatis/Configuration.xml";
		InputStream inputStream = null;
		try {
			inputStream = Resources.getResourceAsStream(resource);
		} catch (IOException e) {
			e.printStackTrace();
		}
		sqlSessionFactory =
		  new SqlSessionFactoryBuilder().build(inputStream);
	}
	
	public List<DeptDTO> selectDynamicDeptno(HashMap<String, Integer> map){
		
		SqlSession session = sqlSessionFactory.openSession();
		List<DeptDTO> list = null;
		try {
			DeptDAO dao = new DeptDAO();
			list = dao.selectDynamicDeptno(session, map);
		} finally {
			// session도 닫아주는 것을 잊지 말자!
			session.close();
		}	 
		
		return list;
	}
	
	public List<DeptDTO> selectDynamicChoose(HashMap<String, String> map) {
		SqlSession session = sqlSessionFactory.openSession();
		List<DeptDTO> list = null;
		try {
			DeptDAO dao = new DeptDAO();
			list = dao.selectDynamicChoose(session, map);
		} finally {
			session.close();
		}
		return list;
	}
}

```

### 5. DeptDAO 패키지

- 역시 별 차이 없다.

```java
package com.dao;	// com.repository로 줄 수도

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.session.SqlSession;

import com.dto.DeptDTO;

import com.exception.DuplicatedDeptnoException;;

public class DeptDAO {
	
	// 1. selectDynamicDeptno
	// map
	public List<DeptDTO> selectDynamicDeptno(SqlSession session, HashMap<String, Integer> map){
		List<DeptDTO> list = session.selectList("com.dept.DeptMapper.selectDynamicDeptno", map);
		return list;
	}
	
	// 2. selectDynamicChoose
	// map
	public List<DeptDTO> selectDynamicChoose(SqlSession session, HashMap<String, String> map) {
		List<DeptDTO> list = session.selectList("com.dept.DeptMapper.selectDynamicChoose", map);
		return list;
	}
}

```

### 6. Exception 패키지

- 별 차이 없다.