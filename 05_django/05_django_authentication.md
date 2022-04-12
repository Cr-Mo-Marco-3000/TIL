# Django - Authentication System

[toc]

## 1. The Django Authentication System

> The Django Authentication System

- Django 인증 시스템은 django.contrib.auth에 Django contrib module로 제공
- 필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS 설정에 나열된 아래 두 항목으로 구성됨
  1. django.contrib.auth
     - 인증 프레임워크의 핵심과 기본 모델을 포함
  2. django.contrib.contenttypes
     - 사용자가 생성한 모델과 권한을 연결할 수 있음

- 장고 인증 시스템은 인증과 권한 부여를 함게 제공(처리)하며, 이러한 기능이 어느 정도 결합되어 일반적으로 인증 시스템이라고 함



> 인증과 권한

- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정



> 로그인 앱 생성

- `$ python manage.py startapp accounts`
- app 이름이 반드시 accounts일 필요는 없지만, auth와 관련해 Django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 되도록이면 accounts로 지정하는 것을 권장
  - 만약 다르게 할 경우 추가적인 설정이 필요해져서 귀찮아짐
- 이후 INSTALLED_APPS 등록 및 url 설정 필요



## 2. 쿠키와 세션

> HTTP

- Hyper Text Transfer Protocol
  - HTML 문서와 같은 리소스(자원, 데이터) 들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - 클라이언트 - 서버 프로토콜이기도 함



> HTTP 특징

- 비연결지향
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
- 무상태
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  - 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적임
- **클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재**



> 쿠키의 개념

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치(placed-on)되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 쿠키를 로컬에 Key-value의 데이터 형식으로 저장
  - 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재 요청 시 저장된 쿠키를 함께 전송
    - e.g. 로그인 되었다는 상태를 서버에 알려주기 위해 클라이언트가 매 요청마다 쿠키를 붙여 요청
- 참고: 소프트웨어가 아니기 때문에 프로그램처럼 실행될 수 없으며 악성코드를 설치 할 수 없지만, 사용자의 행동을 추적하거나 쿠키를 훔쳐서 해당 사용자의 계정 접근 권한을 획득할 수도 있음
- **HTTP 쿠키는 상태가 있는 세션을 만들어 줌**
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문
- **정리: 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함게 전송**



> 쿠키의 사용 목적

1. **세션 관리**
   - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화
   - 사용자 선호, 테마 등의 설정
3. 트래킹
   - 사용자 행등을 기록 및 분석

- 참고: 시크릿 모드
  - 쿠키를 저장하지 않는 모드



> 쿠키를 사용한 장바구니 예시

- 쿠팡 - 개발자 도구 - Network 탭 - cartView.pang 확인
  - 서버는 응답과 함께 Set-Cookie 응답 헤더를 브라우저에게 전송
  - 이 헤더는 클라이언트에게 쿠키를 저장하라고 전달
  - Cookies 탭에서 쿠키 데이터 자세히 확인
- 메인 페이지 이동 - 장바구니 유지 상태 확인
  - 이제 서버로 전송되는 모든 요청과 함께, 브라우저는 Cookie HTTP 헤더를 사용해 서버로 이전에 저장했던 모든 쿠키들을 함께 전송
- 개발자 도구 - Application 탭 - Cookies - 마우스 우측 버튼 - Clear 후 새로고침
  - 빈 장바구니로 변경 확인



> 세션(Session)

- 사이트와 특정 브라우저 사이의 상태('state')를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 발급받은 session id를 쿠키에 저장
  - 클라이언트가 다시 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
- ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장함
  - 로그아웃을 세션을 삭제하는 과정




> 세션을 이용한 Gitlab 예시

- Gitlab 로그인 - 개발자 도구 - Application 탭

  - Gitlab 서버로부터 받아 저장된 session 쿠키(_gitlab_session) 확인

- session 삭제 후 페이지 새로고침

  - 로그아웃 상태 변경 확인

  

> 쿠키의 수명(lifetime)

- 쿠키의 수명은 두 가지 방법으로 정의할 수 있음

1. Session cookies

   - 현재 세션이 종료되면 삭제됨

   - 브라우저가 현재 세션(current session)이 종료되는 시기를 정의
     - 참고: 일부 브라우저는 다시 시작할 때 세션 복원을 사용해 세션 쿠키가 오래 지속될 수 있도록 함


2. Persistent cookie(Permanent cookie)
   - Expires 속서에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제



> Session in Django

- Django의 세션은 미들웨어를 통해 구현됨
- Django는 database-backed sessions 저장 방식을 기본 값으로 사용
  - 참고: 설정을 통해 cached, file-based, cookie-based 방식으로 변경 가능
  - 설정을 통해 cached, file-based, cookie-based 방식으로 변경 가능

- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄
  - 세션 정보는 Django DB의 django_session 테이블에 저장됨
- 모든 것을 세션으로 사용하려고 하면 사용자가 많을 때 서버에 부하가 걸릴 수 있음



> Authentitcation System in MIDDLEWARE

- settings.py에서
- SessionMiddleware
  - 요청 전반에 걸쳐 세션을 관리
- AuthenticationMiddleware
  - 세션을 사용하여 사용자를 요청과 연결



> Middleware

- HTTP 요청과 응답 처리 중간에서 작동하는 시스템(hooks)
- Django는 HTTP 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는 view로 연결해주고, HTTP 응답 역시 미들웨어를 거쳐서 내보냄
- 주로 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 담당



## 3. 로그인

> 로그인

- **로그인은 session을 Create하는 로직과 같음**
- Django는 우리가 session의 메커니즘에 생각하지 않게끔 도움을 줌
- 이를 위해 인증에 관한 built-in-funcion을 제공



> AuthenticationForm

- `from django.contrib.auth import AuthenticationForm`
- 사용자 로그인을 위한 **form**
  - forms.Form을 상속한다.
  - 첫 번째 인자로는 request를 받고, 다음 인자부터 Form의 인자를 똑같이 받는다.
  - 즉, `form = AuthenticataionForm(requuest, request.POST)` 요렇게 받는다.

- 유효성 검사를 해 주는 form이고, 실제 로그인 시켜주는 함수는 아니다!
- 로그인은 DB를 작성, 수정, 삭제하지 않는다!
- request를 첫번째 인자로 취함
  - DB에 값을 건드리지 않으므로 모델 폼이 아님!
  - 일반 ModelForm은 인자로 request.POST 를 받음
  - `article = ArticleForm(request.POST)`




> login 함수

- AuthenticationForm을 통과한다면 실제로 로그인을 시켜주는 함수

- `from django.contrib.auth.forms import login as login`

  - login은 view.py의 함수 이름으로 쓰였으므로 as login을 붙여준다.
- `login(request, user, backend=None)`

  - 현재 세션에 연결하려는 인증된 사용자(form을 통과한 사용자)가 있는 경우 login() **함수**가 필요
    - 인증된 사용자는 form에 저장되어 있다.
    - AuthenticationForm의 form.get_user()라는 인스턴스 메소드를 통해 반환된 사용자 객체를 두 번째 인자로 받는다.
  - 사용자를 로그인하며 view 함수에서 사용 됨
  - HttpRequest 객체와 User 객체가 필요
  - Django의 session framework를 사용하여 세션에 user의 ID를 저장
    - 로그인을 의미
    - 로그인 후 브라우저와 Django dB에서 Django로부터 발급받은 sessionid 확인

> get_user()

- AuthenticationForm의 인스턴스 메서드
- user_cache는 인스턴스 생성 시에 None으로 할당되며, 유효성 검사를 통과했을 경우 로그인 한 사용자 객체로 할당 됨
- 인스턴스의 유효성을 먼저 확인하고, 인스턴스가 유효할 때만 user를 제공하려는 구조

```python
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        # 위와 같은 코드 == form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('article:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```



## 4. Authentication data in templates

> Authentication data in templates

- context processors
  - 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록
  - 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함됨

- Users
  - context_processors
  - 템플릿 RequestContext를 렌더링할 때, 현재 로그인한 사용자를 나타내는 auth.User 인스턴스(또는 클라이언트가 로그인하지 않은 경우 AnonymousUser 인스턴스)는 템플릿 변수 {{ user }}에 저장됨

- Built-in template context processors

  - django.contrib.auth.context_processors.auth
  - 등등

  

## 5. 로그아웃

> 로그아웃

- 로그아웃은 session을 Delete하는 로직과 같음
- logout(request)
  - httpRequest 객체를 인자로 받고 반환 값이 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 현재 요청에 대한 session data를 DB에서 완전히 삭제하고, 클라이언트의 쿠키에서도 sessionid가 삭제됨
  - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 
    **이전 사용자의 세션 데이터에 엑세스하는 것을 방지하기 위함**



## 6. 로그인 사용자에 대한 접근 제한

- 로그인 사용자에 대한 엑세스 제한 2가지 방법

1. The raw way
   - is_authenticated attribute

2. The login_required decorator



> is_authenticated 속성

- User model의 속성(attribute)중 하나
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 일반적으로 request.user에서 이 속성을 사용하여, 미들웨어의 `'django.contrib.auth.middleware.AuthenticationMiddleware'`를 통과했는지 확인
  - context processor에서, 모든 request객체를 template에서 쓸 수 있도록 django가 설정해줌

- 단, 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음

```python
# views.py

@require_http_methods(['GET', 'POST'])
def login(request):
    # 인증된 사용자는 login에 접근할 수 없도록 앞에 붙여줌
    if request.user.is_authenticated:
        redirect('article:index')
        ...
 
@require_POST
def logout(request):
    # 인증된 사용자만 logout에 접근할 수 있도록 앞에 붙여줌
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('articles:index')
```

```html
```



> login_required decorator

- 사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 REDIRECT함
  - LOGIN_URL의 기본 값은 '/accounts/login/'
  - login을 담당하는 앱 이름을 accounts로 했던 이유 중 하나
- 사용자가 로그인되어 있으면 정상적으로 view 함수를 실행
- 인증 성공 시 사용자가 redirect 되어야 하는 경로는 'next'라는 쿼리 문자열 매개 변수에 저장됨
  - 예시: `/accounts/login/?next=/articles/create`



> 'next' query string parameter

- 로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect 하기 위해 주소를 keep 해주는 것
- 단, 별도로 처리 해주지 않으면 우리가 view에 설정한 redirect 경로로 이동하게 됨(처리되면 return까지 가게 되니까)

```python
# accounts/views.py

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        redirect('article:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 
            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

```

