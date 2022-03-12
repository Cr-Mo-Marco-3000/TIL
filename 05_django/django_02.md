# Django 2



## 1. Model

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- Django는 model을 통해 데이터에 접속하고 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

- 웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구

> Database

- 데이터베이스
  - 체계화된 데이터의 모임
- 쿼리
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - Query를 날린다 == DB를 조작한다

- 스키마
  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

- 테이블

  - 열(컬럼/필드/속성)와 행(레코드/튜플/값)의 모델을 사용해 조직된 데이터 요소들의 집합.

  - SQL 데이터베이스에서는 테이블의 관계라고도 한다.

    

- 열(Column), 컬럼: 각 열에는 고유한 데이터 형식이 지정된다.

- 행(row), 레코드: 테이블의 테이터는 행에 저장된다.

- PK(Primary Key: 기본키)

  - 각 행(레코드)의 **고유값**으로 PRimary Key로 불린다. 반드시 설정하여야 하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.



## 2. ORM

> ORM

- Object-Relational_mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Django - SQL) 데이터를 변환하는 프로그래밍 기술
- 장점
  - SQL을 잘 알지 못해도 DB 조작이 가능
  - SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- **현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(생산성)**



- 왜 ORM을 사용할까?
  - 우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용한다.

```python
# appname/models.py

class Appname(models.Model):
	title = models.CharField(max_length=10)
    content = models.TextField()
    
# 요런 식으로 설정
# title과 content는 각 column을 나타냄
# = 이후는 필드의 속성
```



## 3. Migrations

> Migrations 

- Django가 model에 생긴 변화를 DB에 반영하는 방법

- 명령어들

  1. makemigrations
     - model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)를 만들 때 사용
     - `$ python manage.py makemigrations`


  2. migrate
     - 마이그레이션을 DB에 반영하기 위해 사용
     - 설계도를 실제 DB에 반영하는 과정
     - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
     - `$ python manage.py migrate`

  3. sqlmigrate
     - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
     - 마이그레이션이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음
     - `$ python manage.py sqlmigrate app_name 0001`
  4. showmigrations
     - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
     - 마이그레이션 파일들이 migrate 됐는지 여부를 확인할 수 있음
     - `python manage.py showmigrations`

- 순서(3단계까지는 반드시 기억할것!!!)

  1. models.py => 테이블/속성 정의

  2. makemigrations => 설계도(DB에 반영되지 않은 상태)
  3. migrate => DB 반영
  4. sql migrate => SQL명령어를 보는 명령어
  5. showmigrations => DB반영여부

- models.py가 바뀌면 무조건 설계도부터 다시 만들어줘야 한다!!!

## 4. Database API



> DB API

- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
- Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
- database-abstract API 혹은 database-access API라고도 함



> DB API 구문

- `Article.objects.all()`
- Class Name. Manager(매니저).QuerySet API(도구) 순서
- 본 명령은 DB에게 class(table)에 저장된 모든 데이터를 달라는 의미

- Manager
  - Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  - 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가

- QuerySet - 유사 리스트
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

  

> Django Shell

- 일반 python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
- 그래서 장고 프로젝트 설정이 load 된 Python Shell을 활용해 DB API 구문 테스트 진행

- 기본 Django Shell보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행
- ipython, django-extensions 라이브러리를 설치 후
- django_extensions를 앱에 등록 후
- `$ python manage.py shell_plus`로 실행



## 5. CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 다음을 일컫는 방법
  - Create
  - Read
  - Update
  - Delete

> Create

```bash
# shell_plus에서

# 1.인스턴스 생성 후 인스턴스 변수 설정

# 인스턴스 선언
$ article = Article()

# 인스턴스 변수들에 값을 할당
$ article.title = '첫 번째 제목'
$ article.content = '첫 번째 내용'

# save를 하지 않으면 DB에 값이 저장되지 않기 때문에, 필수적으로 해줘야 함!
$ article.save()

# 2. 초기 값과 함께 인스턴스 생성

$ article = Article(title='두 번째 제목', content='두 번째 내용')
$ article.save()

# 3.QuertSet API - create() 사용
# 얘는 save() 필요 없음

$ Article.objects.create(title='세 번째 제목', content='세 번째 내용')


```

- save() method

  - Saving objects
  - 객체를 데이터베이스에 저장함
  - 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
    - ID값은 Django가 아니라 DB에서 계산되기 때문
  - 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save()가 필요

- str method

  - 표준 파이썬 클래스의 메소드인 str()을 정의하여 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음
  - 작성 후 반드시 shell_plus를 재시작해야 반영됨

  ```python
  # appname/models.py
  
  class Appname(models.Model):
  	title = models.CharField(max_length=10)
      content = models.TextField()
  
      def __str__(self):
          return self.title
  ```

  - 예를 들어, str method를 적용 전에는
  - Shell_plus에서 Article.objects.all()을 입력했을 때
    - <QuerySet [<Movie: Movie object (1)>, <Movie: Movie object (2)>, <Movie: Movie object (5)>, <Movie: Movie object (7)>]> 이렇게 뜬다면
  - 적용 후에는
    - <QuerySet [<Movie: 반지의 제왕>, <Movie: sdfs>, <Movie: asdsa>, <Movie: 반지의 제왕>]> 이런 식으로, 제목으로 구분할 수 있게 뜬다!

> Read

- QuerySet API method를 사용해 다양한 조회를 하는 것이 중요
- QuerySet API는 크게 2가지로 분류
  - Methods that return new querysets
    - all()
      - 현재 QuerySet의 복사본을 반환
      - `Article.objects.all()`
    - filter()
      - 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 queryset을 반환
      - `Article.objects.filter(content='~~~')`
  - Methods that do not return querysets
    - get()
      - 주어진 lookup매개변수와 일치하는 객체를 반환
      - 객체를 찾을 수 없으면 DoewNotExist 예외를 발생시키고 둘 이상의 객체를 찾의면 MultipleObjectsReturned 예외를 발생시킴
      - 즉, primary key(pk)와 같이 고유성을 보장하는 조회에서 사용해야 함
      - `article = Article.objects.get(pk=1)`

> update

- get 등으로 객체를 불러와 변수에 할당한 후, create와 같은 식으로 변경하면 됨
- `article = Article.pbjects.get(pk=1)`
- `article.title = '제목 수정'`
- `article.content = '내용 수정'`
- `article.save()`

> delete

- QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환
- `article = Article.objects.get(pk=1)`
- `article.delete()`



> Field lookups

- 조회 시 특정 검색 조건을 지정
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정됨
- 사용 예시
  - Article.objects.filter(pk**__gt=2**)
  - Article.objects.filter(content**__contains='ja'**)



## 6. Admin Site

> Automatic admin interface

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
- Model class를 admin.py에 등록하고 관리
- django.contrib.auth 모듈에서 제공됨
- record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음



### 순서

> admin 생성

- `$ python manage.py createsuperuser`
- 관리자 계정 생성 후 서버를 실행한 다음 `/admin`으로 가서 관리자 페이지 로그인
  - 계정만 만든 경우 Django 관리자 화면에서 아무 것도 보이지 않음
- 내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록
- auth에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 없음에 유의!



> admin 등록

```python
# appname/admin.py

from django.contrib import admin
from .models import Classname

# admin site에 register 하겠다.
admin.site.register(Classname)

```

- admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것
- model.py에 정의한 `__str__`의 형태로 객체가 표현됨



> ModelAdmin options

- list_display
  - models.py에서 정의한 각각의 속성(컬럼)등릐 값(레코드)를 admin 페이지에 출력하도록 설정함
  - list_filter, list_displat_links 등 다양한 ModelAdmin options 참고

```python
from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')

admin.site.register(Movie, MovieAdmin)
```



## 7. CRUD with View

- 직접 실습하면서 진행!



## 8. 총정리

- Model
  - 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
- Database
  - 체계화 된 데이터의 모임(집합)
- Migrations
  - Django가 model에 생긴 변화(필드를 추가, 모델 삭제 등)를 반영하는 방법
- ORM
  - OOP 언어를 사용하여 데이터베이스와 OOP 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
- Database API
  - DB를 조작하기 위한 도구(QuerySet API, CRUD)
- Admin Site
  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
