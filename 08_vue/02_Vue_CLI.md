



## Vue CLI

### 1. Node.js

- 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경
  - JavaScript Runtime Environment
  - 브라우저 밖을 벗어 날 수 없던 자바스크립트 언어의 태생적 한계를 해결
- Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
- 즉, 단순히 브라우저만 조작할 수 있던 자바스크립트를 SSR 아키텍처에서도 사용할 수 있도록 함



### 2. NPM(Node)

- 자바스크립트 언어를 위한 패키지 관리자

npm은 pip과는 다르게 특정 프로젝트에 패키지를 설치하는 게 기본이다.

컴퓨터 전체에 설치할 때는 -g 옵션을 붙여주어야 한다.

단, -g는 위험하다. => 설치 문서에 -g로 설치하라고 써 있는 경우에만 쓰자!





- props 컨벤션

props 안에서는 카멜 케이스(자식 컴포넌트의 props: {} 안에 작성할 때는 camelCase)



- html에서는 케밥 케이스(html 태그 안에서: `<ChildComponeet :kebab-case="" 등으로 넘길 때/>`)
  - html은 자동 소문자 변환이 되기 때문
  - {{}} 안에는 케밥 케이스로 써 주지 말고 props로 받은 데이터 이름 그대로 써 주어야 한다!
  - 근데 그냥 둘 다 camel case로 작성해 주자

이렇게 해도 인식



### 3. 단방향 데이터 흐름

- 모든 props는 하위 속성과 상휘 속성 사이의 단방향 바인딩을 생성
- 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안 됨
  - 자식 요소가 의도치 않게 부모 요소의 상태를 변경하여 앱의 데이터 흐름을 이해하기 어렵게 만드는 일을 방지
- 부모 컴포넌트가 업데이트 될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트됨



### 4. Emit event

- Listening to Child Components Events
- `$emit(eventName)`
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달
  - 정리: 부모(조상이 아님) 컴포넌트에게 1번 인자 라는 이름의 이벤트를 발생 + 2번인자 데이터를 보냄
    - 보낼 데이터가 여러 개 라면 묶어서 전달하는 게 좋다.
  - 받는 부모의 이벤트가 발생시키는 메서드의 첫 번째 인자로, emit으로 보낸 두 번째 인자가 전달된다.
- 무조건 자신의 부모에게만 이벤트 발생!
- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취 (v-on을 이용한 사용자 지정 이벤트)



### 5. Event 이름 컨벤션

- 컴포넌트 및 props와는 달리, 이벤트는 자동 대소문자 변환을 제공하지 않음
- HTML의 대소문자 구분을 위해 DOM 템플릿의 v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 v-on:myEvent는 자동으로 v-on:myevent로 변환
- 이러한 이유로 이벤트 이름에는 항상 kebob-case를 사용하는 것을 권장
- 어떤 이벤트를 발생시키는 메서드를 정의할 때는 camel case를 쓰지만, 올려보낼 이벤트 정의시에는 kebab-case



## Vue Router

### 1. Vue Router

- Vue.js 공식 라우터
- 라우트(route)에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할 지 알려줌
  - 컴포넌트와 주소를 매핑함
  - url을 통해 이동한 척 한다. => 한 페이지 안에서 component를 준비시켜 놓았다 url은 변화시키며 보여줌.
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- [참고] router
  - 위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치



### 2. Vue Router가 이것저것 바꿔줌

`<router-link>`: anchor같은 역할: 근데 **컴포넌트임**

`<router-view/>`가 component가 들어가는 자리: 얘도 컴포넌트

### Named Routes

- python에서의 url_patterns에서 이름 공간을 형성해 주는 것과 비슷함
- 다음과 같이 작성 `<router-link :to="{ name: 'home'}">`



### 프로그래밍 방식 내비게이션

a tag와 같은 방식인 router-link 말고 button 등을 이용해서도 같은 동작을 할 수 있음

`  <button @click="moveToHome"></button>`

메소드 내부에 `moveToHome() { this.$router.push({ name: 'home' })}` 함수를 작성해서 구현



### Dynamic Route matching

쿼리스트링을 넘길 때는 query(url에)

variable routing등을 넘길 때는 params를 같이 넘겨준다.



### History mode

