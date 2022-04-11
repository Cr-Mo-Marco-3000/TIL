## Handling HTTP requests

> Intro

- Django에서 HTTP 요청을 처리하는 방법
  1. Django shortcut functions
  2. View decorators





> Django shortcuts functions

- django.shortcuts 패키지는 개발에 도움 될 수 있는 여러 함수와 클래스를 제공
- views.py 내부의 `from django.shorcuts import render, redirect`
- 종류
  - render()
  - redirect()
  - get_object_or_404()
  - get_list_or_404()

- 만약 render()가 없었다면, template을 따로 로드 후 컨텍스트와 함께 return해야 한다.



> get_object_or_404()

- 모델 manager인 objects에서 get()을 호출하지만, 해당 객체가 없을 경우 DoesNotExist 예외 대신 HTTP 404 를 raise
  - 발생 예외가 바뀜
- get()의 경우 조건에 맞는 데이터가 없을 경우에 예외를 발생 시킴
  - 코드 실행 단계에서 발생한 예외 및 에러에 대해서 브라우저는 http status code 500으로 인식함
- 상황에 따라 적절한 예외처리를 하고 클라이언트에게 올바른 에러 상황을 전달하는 것 또한 개발의 중요한 요소 중 하나





Django View decorators

- Django는 다양한 HTTP기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터르 ㄹ제공
- Decorator
  - 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장 해주는 함수
  - 즉, 원본 함수를 수정하지 않으면서 추가 기능만을 구현할 때 사용
  - 동작 방법 => 데코레이터를 단 함수가 데코레이터 함수의 인자로 들어가게 됨



- Allowed HTTP methods
  - 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
  - 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed를 return(405 Method Not Allowed)
    - 기존의 구현 방식으로는, Client가 왜 접근이 불가능한지 알 수 없음
  - require_http_methods()
    - view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터
  - require_POST()
    - view 함수가 POST method 요청만 승인하도록 하는 데코레이터
  - require_safe()
    - view 함수가 GET 및 HEAD method만 허용하도록 요구하는 데코레이터
    - django는 require_GET 대신 require_safe를 사용하는 것을 권장
    - 필요한 예시 페이지들
      - index, detail 페이지 등
  - require_GET()
    - django에서 권장하지 않음



> Media File

- 미디어 파일
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드 한 모든 정적 파일



> Model field

- ImageField()
  - 이미지 업로드에 사용하는 모델 필드
  - FileField를 상속받는 서브 클래스이기 때문에 FileFiedl의 모든 속성 및메 서드를 사용 가능하며, 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함
  - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음
  - **주의!** 사용하려면 반드시 Pillow 라이브러리가 필요
- FileField()
  - 파일 업로드에 사용하는 모델 필드
  - 2개의 선택 인자를 가지고 있음
    1. upload_to
    2. storage



> ImageField 작성

- upload_to='images/'
  - 실제 이미지가 저장되는 경로를 지정
- blank=True
  - 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드 할 수 있도록)



> upload_to





blank와 null



이미지 등은 request.POST가 아니라 request.FILES로 받는다.