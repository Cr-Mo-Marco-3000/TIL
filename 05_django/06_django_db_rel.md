# 데이터베이스 관계

## 1. Foreign Key

> Foreign Key 개념

- 외래 키(외부 키)
- 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 속성(필드)에 해당하고, 이는 참조되는 테이블의 **기본 키(Primary Key)**를 가리킴
- 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응됨
  - 이 때문에 참조하는 테이블에서 참조되는 테이블의 존재하지 않는 행을 참조할 수 없음
- 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있다.
- 1:N 관계에서, 외래 키는 N을 담당하는 테이블이 가지고 있다.
  - 참조 하는 테이블(댓글: N), 참조 되는 테이블(글: 1)

> Foreign Key 예시

- 게시글(Article)과 댓글(Comment)간의 모델 관계 설정
- 참조하는 모델(Comment)에서 외래 키는 참조되는 모델의 기본 키(Primary Key)를 가리킴



> Foreign Key 특징

- 키를 사용하여 부모 테이블의 **유일한 값**을 참조(참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함(단 유일한 값을 보장하는 필드가 일반적으로 기본 키일 뿐)

- 참고: 참조 무결성
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
  - 외래 키가 선언된 테이블의 외래 키속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함



> ForeignKey field(1/3)

- A many-to-one relationship
- 2개의 위치 인자가 **반드시 필요**
  - 예시: `article = models.For
  - 참조하는 model class
  - on_delete 옵션
- migrate 작업 시 필드 이름에 **_id를 추가**하여 데이터베이스 열 이름을 만듦

- 참고: 재귀 관계(자신과 1:N)



> ForeignKey field(2/3)

- comment 모델 정의하기

- **일반적으로 1:N의 관계에서는, 참조되는 모델의 단수형 소문자로 작성을 한다.**

```python
class Comment(models.Model):
    # 일반적으로 1:N의 관계에서는, 참조되는 모델의 단수형 소문자로 작성을 한다
    # 작성을 앞에 해도, 실제 생성되는 테이블에서는 마지막 필드로 작성된다
    # 변수명 앞에 _id를 달면 안 된다!!! 자동으로 달린다!!! ForeignKey field(1/3) 참조
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



> ForeignKey arguments - 'on_delete'

- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정
- on_delete 옵션에 사용 가능한 값들
  - CASCADE: 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
  - 이외에도 총 7개의 옵션(PROTECT, SET_NULL 등)을 제공



> 참고: 데이터 무결성

- 2. **참조 무결성**



> Migration

- 생성된 필드 article_id
  - _id는 **자동**으로 붙는다.
  - 1:N 관계에서는, M:N관계와 구분하기 위해 필드 앞에 참조하는 모델의 이름을 단수형 소문자로 쓴다.



> 데이터베이스의 ForeignKey 표현

- 만약 Foreign Key 인스턴스를 abcd로 생성했다면 abcd_id로 만들어짐

- 하지만 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)으로 작성하는 것이 바람직함(1:N)

articles_comment: 시험에 나올듯

> 객체 조작

- 아래 방식 둘 다 가능하다

- comment.article_id = article.pk
  - 필드를 직접 명시한다면, 객체를 넣을 수 없고 필드를 명시해 넣어주어야 한다.
- comment.article = article

​	

> 1:N관계 related manager

- 역참조 (**.comment_set**)
  - Article(1) => Comment(N)
  - article.comment 형태로는 사용할 수 없고, `article.comment_set` manager가 생성됨
  - 게시글에 몇 개의 댓글이 작성 되었는지 Django ORM이 보장할 수 없기 때문
    - article은 comment가 있을 수도 있고, 없을 수도 있음
    - **실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음** 
      - 참조는 간단하지만(댓글로 글 조회), 역참조는 어려움
      - Article 모델은, Comment 모델에 대해 어떤 정보도 갖고 있지 않기 때문

- 참조('article')
  - Comment(N) => Article(1)
  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로, comment.article과 같이 접근할 수 있음
  - 실제 ForeignKey 또한 Comment 클래스에서 작성됨



> ForeignKey arguments - 'related_name'

- 역참조 시 사용할 이름('model_set' manager)을 변경할 수 있는 옵션
- 아래와 같이 변경하면 article.comment_set은 사용 불가 하고 대신 article.comments로 대체됨
- 주의: 역참조 시 사용할 이름 수정 후, migration 과정 필요
- **주의: 1:N 관계에서는 이름을 바꾸는 것을 권장하지 않음!** 
  - M:N관계에서는 본 기능을 필수로 사용해야 하기 때문에, 나중에 둘 중 어떤 관계인지 구분하기 어렵기 때문!

```python
# articles/model.py

class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
        ...
```



## 2. Comment CREATE

> CommentForm 작성

```python
from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
```



> 댓글 작성 로직

```python
# views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # commit=False => 저장은 안하고 인스턴스는 만들어줌
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)
```



> The save() method

- save(commit=False)
  - Create, but don't save the new instance
  - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
  - **저장하기 전**에 객체에 대한 **사용자 지정 처리를 수행**할 때 유용하게 사용



## Customizing authentication in Django



## 1. Substituting a custom User Model

> User 모델 대체하기

- **앞으로 프로젝트를 진행하기 전 필수사항!!!**

- 일부 프로젝트에서는 Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
  - ex) username 대신 email을 식별 토큰으로 사용하는 것이 더 적합한 사이트
- Django는 User를 참조하는데 사용하는 AUTH_USER_MODEL 값을 제공하여, default user model을 재정의(override) 할 수 있도록 함

- Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 **강력하게 권장(highly recommended)**
  - 단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함



> AUTH_USER_MODEL 

- user를  나타내는데 사용하는 모델
- 프로젝트가 **진행되는 동안 변경할 수 없음**
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함
- 기본 값: 'auth.User' (auth 앱의 User 모델)
- 참고: 프로젝트 중간(mid-project)에 AUTH_USER_MODEL 변경하기
  - 보델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요
  - 즉, 중간 변경은 권장하지 않으므로 초기에 설정하는 것을 권장



> Custom User 모델 정의하기(1/4)

- 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스인 AbstractUser를 상속받아 새로운 User 모델 작성

```python
#accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



> Custom User 모델 정의하기(2/4)

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```



> Custom User 모델 정의하기(4/4)

- 프로젝트 중간에 진행했기 때문에 DB를 초기화 한 후 마이그레이션 진행
- 초기화 방법
  1. db.sqlite3 파일 삭제
  2. migrations 파일 모두 삭제(파일명에 숫자가 붙은 파일만 삭제)



> get_user_model

- 현재 장고 프로젝트에서 **활성화되어** 있는 사용자 모델(active user model)을 반환
  - User 모델을 커스터마이징한 상황에서는 Custom User 모델을 반환
- 이 때문에 Django는 User 클래스를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 참조해야 한다.
- **결코 User를 직접 참조하지 않음!**



1:N 관계 설정

User-Article(1:N)

- 모델에서의 User 모델 참조는 함수로 하지 않는다!!!



> User 모델 참조하기

- 두 가지 방법은 return이 다르다

1. `settings.AUTH_USER_MODEL`
   - **return이 str형식**
   - User 모델에 대한 외래 키 또는 다대다 관계를 정의 할 때 사용해야 함
   - models.py에서 User 모델을 참조할 때**만** 사용
2. `get_user_model()`
   - **return이 object**
   - 현재 활성화(active)된 User 모델을 반환
     - 커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
     - User를 직접 참조하지 않는 이유
   - **models.py가 아닌 다른 모든 곳**에서 유저 모델을 참조할 때 사용

- 참고: 대략적으로 장고에서 app이 실행되는 순서
  1. INSTALLED_APP에서 순차적으로 APP IMPORT
  2. 각 앱의 model을 import