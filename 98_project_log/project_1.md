# 3반 사람들이 약속을 정하는 프로젝트

[toc]

## 1. 상세정보

### 구성원

- 김현영, 김영훈, 이동준, 조혜림



## 2. 일자별 로그

### 1. 2022-04-12

#### 1. 내가 구현한 부분

##### 1. forms

- 나중에 css 파일에 직접 작성하는 방법이 편할 것 같아서, 마진과 레이아웃 부분은 CDN을 통해 불러온 bootstrap으로 처리해 주었고, 다른 부분은 css파일을 만들어서 해결했다.

- 전체적으로 레이아웃의 균일성을 위해 input의 width를 100%로 균일하게 맞춰주었다.
  - form의 넓이를 따라 input들이 배치된다.
- 각 태그들에 들어갈 attribute값들을 box_class, 또는 large_box_class로 묶어줌으로써, 여러 개의 태그에 같은 class들을 적용할 수 있게 했다.
  - 직접 적어주는 방법도 있다 => 이럴 때는 'class': 'w-100 my-2' 이렇게 적어주어야 한다.
- 내가 작성한 부분은 아닌데, 각각 Field나 widget을 정확히 작성하는 데 그치지 않고, attrs 안의 type까지 작성해 주어야 완성된 형태의 input이 나온다.
- time의 step은 초단위로 설정할 수 있기 때문에, 30분인 1800초로 설정하였다.
- people_limit는 음수로 표현되면 안 되기 때문에, min attribute를 0으로 설정해 주었다.
- 전체 form의 넒이는 description의 넓이, 즉 Textarea의 col 넓이에 따라 변한다.

```python
# plans/forms.py

from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    # 전체적으로 보기 좋게 하기 위해 넓이는 form의 길이에 맞춘다.
    box_class = 'w-100 my-2'
    large_box_class = 'w-100 my-2'

    title = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
            attrs={
                'class': box_class
                
            }
        )
    )

    date = forms.DateField(
        widget= forms.DateInput(
            attrs={
                'class': box_class,
                'type': 'date',
            }
        )
    )

    time = forms.TimeField(
        widget= forms.TimeInput(
            attrs={
                'class': box_class,
                'type': 'time',
                # step은 30분 단위로 설정
                'step': '1800',
            }
        )
    )

    people_limit = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                'placeholder': '몇 명?',
                'min': 0,
                'class': box_class,
            }
        )
    )

    place = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
            attrs={
                'class': box_class,
            }
        )
    )

    description = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder': '어떤 모임인지 자세히 작성해 주세요.',
                'cols': 40,
                'rows': 10,
                'class': large_box_class,
            }
        )       
    )
    


    class Meta:
        model = Plan
        fields = '__all__'

```



##### 2. templates

> base.html

- 각 html 문서별로 css파일을 넣기 위해, style 블록을 넣어주었다.

```django
<!-- base.html -->
<!-- ... -->

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Document</title>
    {% block style %}
    
    {% endblock style %}
</head>

<!-- ... -->
```



> plan_create.html

- static 파일을 사용하기 위해, `{% load static %}`를 달아주었다.
- `{% block style %} {% endblock style %}` 사이에 css파일을 읽어주는 부분을 추가하였다.
- 아래 부분은 `{{ form.as_p }}`을 사용하여 통째로 불러오는 방법도 있겠지만, 추후 레이아웃 구성을 쉽게 하기 위해 하나씩 뽑아서 적어주었다.

```django
<!-- plans/templats/plan_create.html -->

{% extends 'base.html' %}
{% load static %}

{% block style %}
<link rel="stylesheet" href="{% static 'plans/plan_create.css' %}">
{% endblock style %}
{% block content %}
  <div class='d-flex flex-column justify-content-evenly align-items-center'>
    <h1 class='my-4'>약속을 잡아봅시다!</h1>
    <form class='d-flex flex-column justify-content-evenly' action="{% url 'plans:plan_create' %}" method="POST">
      {% csrf_token %}
      <label for="id_title">모임의 이름을 적어주세요</label>
      <p>{{ form.title }}</p>
      <label for="id_date">만나는 날짜가 언제인가요?</label>
      <p>{{ form.date }}</p>
      <label for="id_time">몇 시에 만나나요?</label>
      <p>{{ form.time }}</p>
      <label for="id_people_limit">몇 명까지 만날 수 있나요?</label>
      <p>{{ form.people_limit }}</p>
      <label for="id_place">어디서 만나나요?</label>
      <p>{{ form.place }}</p>
      <label for="id_title">어떤 만남인가요?</label>
      <p>{{ form.description }}</p>
      <button type="submit" class="btn">제출</button>
    </form>
  </div>
{% endblock content %}
```



##### 3. css

> plan_create.css

- css파일을 만들어서 각각 구현해 주었다.
- input은 모바일 앱들에서 입력 받는 양식들과 비슷하게, 사방의 모서리 중 아래만 남겨 주었다.

```css
/* plans/static/plans/plan_create.css */

/* 구글 폰트를 통해 폰트를 적용하려 했는데 실패했다. 추후 구현이 필요하다. */
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,400;0,700;1,500&display=swap');

h1 {
  color: #2159B0;
  font-family: 'Jua', sans-serif;
}


label {
  color: black;
}

input {
  border: 0;
  border-bottom: 2px solid #2159B0;
}

input::placeholder {
  color: gray;
  opacity: 0.8;
}

textarea {
  border: 2px solid #2159B0;
}

textarea::placeholder {
  color: gray;
  opacity: 0.8;
}

button {
  background-color: #F7E85F !important;
}
```



#### 2. 새로 써본 기능

> css

- `::placeholder`

  - input의 양식 안 placeholder의 속성을 정할 수 있다.

  - 나는 opacity를 통해 투명함을 부여하는 식으로 구현하였다.

    

#### 3. 차후 구현해야 하는 부분

##### 1. html and form

- 약속 시간과 최대 몇 명까지 모일 수 있는지 설정하는 input에서, step과 min값을 각각 30분 단위, 0명 이상으로 설정해 주었다. 설정해 준 값과 다르게 저장되지는 않지만, 사용자가 직접 입력하거나 할 때는 1분 단위와 -1명 단위로도 입력은 가능했다. 이 부분은 차후  javascript로 구현을 해 주어야 할 것 같다.

##### 2. css

- 버튼의 색을 바꾸어주려 했는데, 부트스트랩의 btn 클래스 때문인지 적용에 실패했다. 임시로 !important로 적용시켜 놓긴 했지만, 차후 이를 제거하고 다른 방식으로 구현하도록 하자!!!
- 구글 폰트를 사용해서 폰트를 적용하려 했는데, 어떤 이유에서인지 실패했다. 디자인의 기본은 폰트다. 구현하자!!!



---

### 2022-04-24

#### 주요하게 구현한 부분

##### 1. 30일 이후의 약속을 보는 plan_coming.html 페이지를 생성

##### 1. plan_coming.css

```python

# css 부분은 index.css의 것을 그대로 가져왔다

```



##### 2. plan_comings.html

```python

# 이 부분도 별로 변한 건 없다.

```



##### 3. views.py

- index를 만들 때 구현한 부분에서 filter 부분을 지금보다 30일 이후로 바꾸었다.
- annotate 기능과 value 기능을 이해하자 => DB를 조정하는 게 아니라 쿼리셋을 조정하는 기능이다!

```python

def plan_coming(request):
    # 그 이후의 약속 조회
    startdate = date.today()
    interval = 30
    enddate = startdate + timedelta(days=interval)
    print(startdate)

    plan_cnt = Plan.objects.filter(date__gt=enddate).values('date').annotate(total=Count('date')).order_by('date')
    print(plan_cnt)

    # new 만들려고 한 거니 그대로 가져오면 된다
    endtime = datetime.now()
    starttime = endtime - timedelta(hours=24)
    plan_new = Plan.objects.filter(created_at__range=[starttime, endtime]).values_list('date', flat=True)

    context = {
        "plan_cnt": plan_cnt,
        'plan_new': plan_new,
    }

    return render(request, 'plans/plan_coming.html', context)

```





#### 마이너하게 구현한 부분

> plans/index.html

- 일정들이 나열되어 있을 때, 마지막에 여분의 공간이 있어야 이쁠 것 같아서 margin을 넣어 주었다.

```django
<!-- 이전 -->
<div class="container d-flex flex-column align-items-center justify-content-evenly">


<!-- 이후 -->
<div class="container d-flex flex-column align-items-center justify-content-evenly mb-5">
```



> base.css

- 팀원인 동준이의 말에 따라서, navbar의 각 버튼의 구획 부분을 33%로 조절하였다.

```css

.nav_button {
  min-width: 33%;
  display: flex;
  justify-content: center;
}

```



