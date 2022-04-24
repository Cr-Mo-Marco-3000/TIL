# 04. 장고에서 CSS 적용이 안 될때 

## 1. 이유

- 브라우저에서 css파일을 캐시에 저장하기 때문이다.



# 2. 해결방법

1. 브라우저 기록 삭제에서 캐시된 이미지 및 파일을 삭제한다.

2. 새로고침 할 때 ctrl + F5를 통해 새로고침한다.

3. 보다 근본적으로는, `<link rel="stylesheet" href="/static/css/mycss.css?{% now "U" %}"/>`식으로 css파일을 불러오는 마지막에 `?{% now 'U' %}` 코드를 붙인다.

   - 아래와 같이 쓸 수도 있다.

   - `<link rel="stylesheet" href="{% static 'plans/plan_coming.css' %}?{% now "U" %}">`
   - `<script src="{% static 'js/polls/polls.js' %}?version=1"></script>`