# Django

[toc]

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
  - View(Controller) - **중간관리자** 느낌: 가장 중요한 부분
    - Model과 Template의 관리/소통 + 알파
    - HTTP 요청을 수신하고 HTTP 응답을 반환
    - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
    - template에게 응답의 서식 설정을 맡김

![img](https://mdn.mozillademos.org/files/13931/basic-django.png)

- MTV Pattern 도식화
  - HTTP Request: 요청이 들어옴 -> 2. URLS: 처음으로 요청을 받음: view안의 연결된 함수가 호출 -> 3. View: 들어온 요청을 수신하고  -> 4. 그대로 Response하거나, 사용자에게 보여줄 Template이 있다면 이를 불러와서 응답하거나(렌더링:보여지는 것), Model로부터 데이터를 뽑아와 응답함
  - 기본적인 도식을 익히자



## Django Intro



> **참고:코드 작성 순서**
>
> - URL
> - View
> - Template
>
>   - 데이터의 흐름에 따라서

> **참고: 장고 사용 순서**
>
>- 가상환경 생성
>- 가상환경 활성화
>- 장고 설치
>- 프로젝트 생성
>- 서버 활성화 => 로켓 확인하기
>- 앱 생성
>- 앱 등록



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

  - **Request object** 

    > https://docs.djangoproject.com/en/3.1/ref/request-response/#module-django.http

    - 요청 간의 모든 정보를 담고 있는 변수
    - 페이지가 요청되면 Django는 요청에 대한 메타 데이터를 포함하는 `HttpRequest` 객체를 만들고
    - 그런 다음 Django는 적절한 view 함수를 로드하고 `HttpRequest`를 뷰 함수의 첫 번째 인수로 전달. 
    - 그리고 각 view는 `HttpResponse` 개체를 반환한다.

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
  - 이 설정이 적용 되려면 USE_I18N이 활성화되어 있어야 함
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
- 사용하는 built-in-system
  - Django template language(DTL)




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
  - view.py 에서 return 할 때 render()의 **세 번째 인자(주로 context라고 한다)**로 {'key': value}와 같이 딕셔너리 형태로 넘겨주며**(view에서 넘겨줄 때)**, 여기서 정의한 key에 해당하는 문자열이 **template에서** 사용 가능한 변수명이 됨
  - 새로고침 하면, name 부분이 변수화 됨!

```python
# views.py

from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Alice',
        }
    context = {
    # 일반적으로 key:value 이름을 맞춰준다.
    # template에 왼쪽의 키 값을 입력해 접근하는 것!
    'foods': foods,
    'info': info,
}
    return render(request, 'greeting.html', context)
```

```html
# tamplate.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>안녕하세요 저는 {{ info.name }} 입니다.</p> <<!--안녕하세요 저는 Alice 입니다.-->>
  <p>제가 가장 좋아하는 음식은 {{ foods }} 입니다.</p> <<!--['apple', 'banana', 'coconut']-->>
    <<!--리스트에 인덱스로 접근-->>
  <p>저는 사실 {{ foods.0 }}를 가장 좋아합니다.</p> <<!--저는 사실 apple를 가장 좋아합니다.-->>
</body>
</html>
```



- DTL Syntax(2/4) - Filters
  - `{{ variable|filter }}`
  - 표시할 변수를 수정할 때 사용
  - 예시
    - name 변수를 모두 소문자로 출력: `{{ name|lower }}`
  - 60개의 built-in template filters를 제공
  - filter는 variable 안에도, tag 안에도 사용이 가능하다.
  - chained가 가능하며 일부 필터는 인자를 받기도 함
    - `{{ variable|truncatewords:30 }}`
  
  



- DTL Syntax(3/4) - Tags
  - `{% tag %}`
  
  - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  
  - 일부 태그는 시작과 종료 태그가 필요
  
  - 약 24개의 built-in template tags를 제공
  
    - for나 end같은 경우, python과 다르게 endfor와 endif로 닫아줘야 함에 유의!!! 
    - 다시 말하지만, filter는 variable 안에도, tag 안에도 사용이 가능하다.
    - {{ }} 안에 ''로 묶은 문자열을 넣고, 필터를 쓸 수 있다. 변수를 넣어 쓰려면 ''를 뺀다
  
    ```django
      <h3>1. for</h3>
      {% for food in foods %}
        <p>{{ food }}</p>
      {% endfor %}
      <hr>
    
      {% for food in foods %}
        <p>{{ forloop.counter }} {{ food }}</p>
      {% endfor %}
      <hr>
    
      {% for user in empty_list %}
        <p>{{ user }}</p>
      {% empty %}
        <p>지금 가입한 유저가 없습니다.</p>
      {% endfor %}
      <hr>
    
    
      <h3>2. if</h3>
      {% if '짜장면' in foods %}
        <p>짜장면엔 고추가루지 !</p>
      {% endif %}
      <hr>
    
      {% for food in foods %}
        {% if forloop.first %}
          <p>짜장면+고추가루</p>
        {% else %}
          <p>{{ food }}</p>
        {% endif %}
      {% endfor %}
      <hr>
    
      <p>3. length filter 활용</p>
      {% for fruit in fruits %}
        {% if fruit|length > 5 %}
          <p>이름이 너무 길어요.</p>
        {% else %}
          <p>{{ fruit }}, {{ fruit|length }}</p>
        {% endif %}
      {% endfor %}
      <hr>
    
      <h3>4. lorem ipsum</h3>
      {% lorem %}
      <hr>
      {% lorem 3 w %}
      <hr>
      {% lorem 4 w random %}
      <hr>
      {% lorem 2 p %}
      <hr>
    
      <h3>5. 글자 관련 필터</h3>
      <p>{{ 'ABC'|lower }}</p>
      <p>{{ my_sentence|title }}</p>
      <p>{{ foods|random }}</p>
      <hr>
    
      <h3>6. 연산</h3>
      <p>{{ 4|add:6 }}</p>
      <hr>
    
      <h3>7. 다양한 날짜 표현</h3>
      {% now "DATETIME_FORMAT" %}<br>
      {% now "SHORT_DATETIME_FORMAT" %}<br>
      {% now "DATE_FORMAT" %}<br>
      {% now "SHORT_DATE_FORMAT" %}
      <hr>
      {% now "Y년 m월 d일 (D) h:i" %}
      <hr>
      {% now "Y" as current_year %}
      Copyright {{ current_year }}
      <hr>
    
      <a href="/index/">back</a>
    ```
  
    



- DTL Syntax(4/4) - comments
  - `{# #}`
  - django template에서 라인의 주석을 표현하기 위해 사용
  - 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있ㅇ므
  - 한 줄 주석에만 사용할 수 있음
  - 여러 줄 주석은 {% comment %} {% endcomment %} 사이에 입력
- DTL Syntax 실습



### 9. Template inheritance(템플릿 상속)

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음.'

- `{% extends 'base.html(base template 이름)' %}`

  - 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
  - 반드시 템플릿 최상단에 작성 되어야 함

- `{% block content(이름) %} {% endblock  %}`

  - 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
  - 즉, 하위 템플릿이 채울 수 있는 공간

  



## HTML form



- HTML 'form' element
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, checkbox, file, hidden, image, password, radio, reset, submit)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당.
  - 핵심 속성(attribute)
    - **action**: 입력 데이터가 전송될 URL 지정
    - **method**: 입력 데이터 전달 방식 지정

  

- HTML 'input' element

  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type 속성에 따라 동작 방식이 달라짐
  - 핵심 속성(attribute)
    - name
      - 어떤 박스에 담아서 던질지 결정
      - name의 값은 박스의 이름을 의미한다

    - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
    - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
    - GET 방식에서는 URL에서 ?key=value&key=value 형식으로 데이터를 전달함'




- HTML 'label' element

  - 사용자 인터페이스 항목에 대한 설명(caption)을 나타냄

  - label을 input 요소와 연결하기

    1. input에 id속성 부여

    2. label에는 input의 id와 동일한 값의 for 속성 부여




- HTTP
  - HyperText Transfer Protocol(protocol: 규약)
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - 주어진 리소스가 수행 할 작업을 나타내는 request methods를 정의
  - HTTP request method 종류
    - GET, POST, PUT, DELETE



- HTTP request method - 'GET'

  - 서버로부터 **정보**를 **조회**하는 데 사용

  - 데이터를 가져올 때만 사용해야 함

  - 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송

  - 우리는 서버에 요청을 하면 HTML 문서 파일 한 장을 받는데, 이때 사용하는 요청의 방식이 GET

    

- HTML input element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type 속성에 따라 달라짐



> App URL mapping
>
> Including other URLconfs
>
> variable routing
>
> 등은 `00_django_intro.md`를 참조
>





### Namescape

- namescape 설정을 언제, 왜 하는지 구분하자
  - templates
    - django에서는, templates를 찾을 때 settings.py 안의 installed_app들의 내부 templates 폴더들을 모은 다음 순서대로 찾는다. 또는 settings.py 안의`'DIRS':` 경로를 만들었다면, 여기도 찾는다.
    - 즉, django 입장에서는 같은 이름의 template들이 서로 다른 templates 폴더들 안에 있어도, 이를 구분하지 못하는 것이다.
    - 따라서, views.py에서 template로 값을 넘길 때, 즉 render(request, 'asdf.html')를 쓸 때,
      appname/template_name.html로 넘기고, 
      template들을 만드는 경로를 templates/`<appname>`/`<template_name>`로 만들어 이름공간을 생성해준다.
  - url
    - 각 url에 name attribute를 붙일 때, 서로 다른 앱의 template로 가는 url임에도 name이 겹칠 수가 있다.
    - 예를 들어, articles 앱의 index와, pages 앱의 index가 각각 `name="index"`로 겹치는 경우가 있다.
    - 이럴 경우, 각 urls.py의 urlpatterns list 위에 `app_name="articles"` 이런 식으로 적어준다.
    - html에서 url tag 등을 사용하여 읽을 때, {% url "articles:index" %} 이렇게 불러올 수 있다.
    - form의 input에서, `action="{% url "articles:catch" %}"`이 부분도 주의하자!
  - staticfile
    - 





- templates namespace

render 내부의 템플릿 이름은 사실은 템플릿의 경로이다!

다만 우리가 장고와 templates 폴더 안에 있다고 약속했기 때문에 이름만 써주었을 뿐

base를 가져올 때도 마찬가지로, 경로이다.

장고는, 약속된 경로들 이후를 모아서 본다!

현재 장고와 약속된 templates 폴더는

app1/templates

app2/templates

Base/templates

3개인데, app1과 app2에 모두 인덱스가 존재하는 상황

templates를 모아서 보고 있으므로, 안에 물리적인 경로를 끼워놓자는 것

articles/templates/index.html

=>

articles/templates/articles(이름공간 역할)/index.html

장고는 인식하는 약속된 경로는 templates까지 

이제 첫번째 앱의 index 페이지를 가져오려면 articles/index.html을 써야 한다.



디버깅 => 현재 요청한 페이지부터 보자

그 다음에는 base로 가볼까?



- url namespace

{% url 'index' %}를 해도 계속 첫 번째 앱의 index url로만 간다.

이름으로도 한계가 있다. => 카테고리를 하나 더 붙이자.

어떤 앱의 url인지 말해주자





articles의 urls.py로 와준 후

urlpatterns 위에

정해진 변수명

app_name = 'articles(앱의 이름 작성)'



{% url 'articles:index' %}

수정해야 될 곳들이 많다.

특히 action부분 주의!



Static Files

웹 서버와 정적 파일

- 웹 서버는 특정 위치(URL)에 있는 자원(resource)를 요청()받아서 제공하는 응답을 처리하는 것을 기본 동작으로 함
- 이는 자원과 접근 가능한 주소가 정적으로 연결된 관계
  - 예를 들어, 사진 파일은 자원이고 파일 경로는 웹 주소라 함
- 즉 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

정적 파일

- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
- 예를 들어, 웹 서버는 일반적으로 이미지, 자바 스크



스태틱 파일 디렉토리

app / static

template와 유사, 따라서 이름 공간 추가를 해주어야 함



staticfields_dirs: templates 기본 경로 작성하는 것 처럼


static은 built in tag가 아님! 따라서 load 태그로 연결해주어야 함



STATIC_URL이 웹페이지에서 이미지를 띄울 때, 사용되는 URL
