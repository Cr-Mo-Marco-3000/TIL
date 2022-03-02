# Django



## Web Framework란 무엇인가?

- Web

  - World Wide Web
  - 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간




- Web의 4가지 키워드

  - 클라이언트

    - 네트워크를 통해 서버가 제공하는 데이터를 얻기 위해 요청

  - 서버

    - 네트워크를 통해 정보, 서비스를 제공하는 컴퓨터 시스템
    - 이를 구축하는 웹 프레임워크 중 하나가 django

  - 요청

    > 네이버 서버로 요청 보냄
    >
    > 네이버 메인페이지를 줘!

  - 응답

    > 한 장의 html 파일을 준다
    >
    > 브라우저가 이를 해석해서 보여줌



- Static web page(정적 웹 페이지)

  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
  - 모든 상황에서 모든 사용자에게 동일한 정보를 표시
  - 일반적으로 HTML, CSS, javaScript로 작성됨
  - flat page라고도 함

  



- Dynamic web page(동적 웹 페이지)
  - 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
  - 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
  - 서버 사이드 프로그래밍 언어(Python, Java, C++ 등)가 사용되며, 파일을 처리하고 **데이터베이스와의 상호작용이 이루어짐**



- Framework
  - 간단하게, 서버를 만들어주는 도구, 일종의 골조
  - 프로그래밍에서 특정 운영체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
  - 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
  - Application framework라고도 함




- Web framework
  - 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함
  - 동적인 웹 페이지나, 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종



- Django를 사용해야 하는 이유
  - 검증된 **Python 언어 기반 Web framework**
  - 대규모 서비스에도 안정적이며 오랫동안 세계적인 기업들에 의해 사용됨
  - Spotify, Instagram, Dropbox, Delivery Hero 등 



- Framework Architecture
  - **왜 필요하지? 계속 생각해야 한다.**
  - MVC Design Pattern(model-view-controller)
  - 소프트웨어 공학에서 사용되는 디자인 패턴 중 하나
  - 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
  - Django는 MTV Pattern이라고 함




- MTV Pattern
  - Model
    - 응용프로그램의 **데이터** 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
  - Template(View)
    - 파일의 구조나 레이아웃을 정의
    - 실제 내용을 **보여주는 데** 사용(presentation)
  - View(Controller) - **관리자** 느낌: 가장 중요한 부분
    - Model과 Template의 관리/소통 + 알파
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김

![img](https://mdn.mozillademos.org/files/13931/basic-django.png)

- MTV Pattern 도식화
  - HTTP Request: 요청이 들어옴 -> 2. URLS: 처음으로 요청을 받음 -> 3. View: 들어온 요청을 수신하고  -> 4. 그대로 Response하거나, 사용자에게 보여줄 Template이 있다면 이를 불러와서 응답하거나, Model로부터 데이터를 뽑아와 응답함
  - 기본적인 도식을 익히자



## Django Intro



##### 참고:코드 작성 순서

- URL

-  View

- Template

  - 데이터의 흐름에 따라서

  

##### 참고: 장고 사용 순서

- 가상환경 생성
- 가상환경 활성화
- 장고 설치
- 프로젝트 생성
- 서버 활성화 => 로켓 확인하기
- 앱 생성
- 앱 등록



### 1. 가상 환경 생성

```bash
# 가상 환경 설정
$ python -m venv venv

# 가상 환경 활성화
$ source venv/Scripts/activate

# 가상 환경 활성화 확인
$ pip list

# 가상 환경 비활성화
$ deactivate

```



### 2. 호환성을 위한 패키지 설치

- 호환성과 협업을 위해 최신 버전 프레임워크 등을 사용하기보다는, LTS 등의 안정적인 버전을 사용하는 것이 좋다.
- 설치 후 ctrl + shift + p 입력 => Python: select interpreter에서 LTS 버전을 고른 후 터미널을 재실행한다.

##### 참고: LTS

- Long Term Support(장기 지원 버전)
- 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
- 컴퓨터 소프트웨어의 제품 수명주기 관리 정책
- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함
- 즉 개발할 때는 LTS 버전으로 하는 것이 좋다.
- django의 최신 LTS 버전은 3.2.12이다.

```bash
# django 설치

$ pip install django==3.2.12

```



### 3. 프로젝트 생성

```bash
$ django-admin startproject [프로젝트명] .


# .을 붙이지 않으면, 설정한 프로젝트명으로 명칭된 폴더를 하나 더 들어가서 같은 이름의 프로젝트가 만들어지게 된다.
```



### 4. 서버 시작하기

```bash
$ python manage.py runserver

# python manage.py는 자주 쓰게 될 것이다.
# 이후 띄워진 url로 들어가 로켓을 확인한다.
```



- 생성된 파일 알아보기
  - `__init__.py`
    - python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - `asgi.py`
    - Asynchronous Server Gateway Interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
  - `settings.py`
    - 애플리케이션의 모든 설정을 포함
    - 많이 들어오게 될 것
  - `urls.py`
    - 사이트의 url과 적절한 views의 연결을 지정
    - 얘도 많이 쓸 것
  - `wsgi.py`
    - Web Server Gateway Interface
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - `manage.py`
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  
  ```bash
  $ python manage.py <command> [options]
  ```
  
  



### 5. Application 생성

- articles가 앱의 이름

- 일반적으로 Application명은 복수형으로 하는 것을 권장

  ```bash
  $ python manage.py startapp articles
  ```

- 구성 파일들

  - admin.py
    - 관리자용 페이지를 설정 하는 곳
  - apps.py
    - 앱의 정보가 작성된 곳
  - models.py
    - 앱에서 사용하는 Model을 정의하는 곳
  - tests.py
    - 프로젝트의 테스트 코드를 작성하는 곳
  - views.py
    - view 함수들이 정의 되는 곳



- Project & Application
  - Project
    - Project는 Application의 집합
    - 프로젝트에는 여러 앱이 포함될 수 있음
    - 앱은 여러 프로젝트에 있을 수 있음
    
  - Application
    - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
    
    - 하나의 프로젝트는 여러 앱을 가짐
    
    - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
    
    - 왜 아까 앱 이름을 articles로 만들었을까?
    
      - 게시판을 만들 것이기 때문
    
      

- 앱 등록
  - 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야 함

  - INSTALLED_APPS
    - Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록
    
  - 앱 생성 시 주의 사항
    - **반드시 생성 후 등록!!!**
    - INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음
    
  - 장고가 권장하는 앱 등록 순서
    - 상단 => # Local apps
    
    - 중단 => # Third party apps
    
    - 하단 => # Django apps
    
      

```python
INSTALLED_APPS = [
	# Local apps
    'articles',
    
    # Third party apps
    
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

##### 참고: Trailing Comma

- 어떤 항목의 위치가 마지막이더라도, 생산성을 위해 마지막에 ,를 붙이는 컨벤션이다.
- 장고에서는 사용하도록 권장하고 있다.



### 6. 요청과 응답

- URLs
  - http 요청(request)을 알맞은 view로 전달
  - runserver 후 나오는 url 뒤에 path 주소값을 붙이면 된다.

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    # django에서는 다른 프레임워크와 다르게 admin template을 기본적으로 제공한다.
    path('admin/', admin.site.urls),
    # path의 url은 상대경로, 절대경로등을 사용하지 않고 고유의 컨벤션을 따른다.
    # 즉 그냥 '기준 url 뒤에 붙는 경로명에 /를 붙인다.'
    # , 뒤에는 메소드처럼 사용함에도 뒤에 ()가 안 붙는다는 것 주의!
    path('index/', views.index)
]
```

- Views
  - http 요청을 수신하고 http 응답을 반환하는 함수 작성
  - Model을 통해 요청에 맞는 필요 데이터에 접근
  - Template에게 HTTP 응답 서식을 맡김

```python
# views.py
# 요건 써져 있다.
from django.shortcuts import render

# Create your views here.
# view함수가 무조건 받아야 하는 매개변수 request
# Http request 객체
# 역시 다른 이름으로 써도 되지만, 컨벤션 지키자!
def index(request):
    # return render(매개변수명, 'template명')
    # render는 템플릿을 렌더링해서 리턴하는 것
    return render(request, 'index.html')

```

- Templates
  - 실제 내용을 보여주는 데 사용되는 파일
  - 파일의 구조나 레이아웃을 정의(e.g. html)
  - Template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 지정되어 있음!!!

```html
<!-- articles/templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>만나서 반가워요!</h1>
</body>
</html>
```

- 이후 `http://127.0.0.1:8000/index/`로 접속해보자!



### 7. 추가 설정

- Language_code

  - 모든 사용자에게 제공되는 번역을 결정
  - language-identifiers 사이트에 들어가서 골라 쓰자
  - 단, 사이트에서와는 달리 소문자로 변경해서 쓰는 게 좋다
  - 'ko-kr' 등

  

- Time_zone

  - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
  - 'Asia/Seoul'

  

- USE_I18N(Internationalization 약자 - 사이 글자가 18자)

  - Django의 번역 시스템을 활성화해야 하는지 여부를 지정

  

- USE_L10N(Localization 약자)

  - 데이터의 지역화 된 형식을 기본적으로 활성화할지 여부를 지정
  - True일 경우, django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

  

- USE_TZ

  - datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
  - True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용

  

### 8. Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- 사용하는 built-in-system: Django template language(DTL)



#### Django template language(DTL)

- Django template에서 사용하는 built-in template system

- 조건 반복 변수 치환, 필터 등의 기능을 제공

- 단순히 Python이 HTML에 포함 된 것이 아니며, 

  프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것

- Python처럼 일부 프로그래밍 구조(if, for)를 사용할 수 있지만,

  이것은 해당 **Python 코드로 실행되는 것이 아님**

  => 사용자의 편의를 위해 비슷하게 지정했을 뿐!

- DTL Syntax

  1. Variable
  2. Filters
  3. Tags
  4. Comments

  

- DTL Syntax(1/4) - Variable
  - `{{ variable }}`
  - render()를 사용하여 **views.py에서 정의한 변수**를 **template 파일로 넘겨 사용**하는 것
  - 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없음
  - dot(.)을 사용하여 변수 속성에 접근할 수 있음
  - view.py 에서 return 할 때 render()의 **세 번째 인자**로 {'key': value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- DTL Syntax(2/4) - Filters
  - `{{ variable|filter }}`
  - 표시할 변수를 수정할 때 사용
  - 예시
    - name 변수를 모두 소문자로 출력: `{{ name|lower }}`
  - 60개의 built-in template filters를 제공
  - chained가 가능하며 일부 필터는 인자를 받기도 함
    - `{{ variable|truncatewords:30 }}`