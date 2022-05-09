# Web & HTML & CSS



## 들어가며

웹 파트는, 극초반의 이론적인 부분을 제외하면 실습 위주로 진행되며,  
html 태그 작성 및 css도 많이 써보고 익숙해지는 방법으로 접근하여야 한다.

본 문서에서는 모든 사항을 서술하기 보다는 돌아오는 시험을 대비하여 
복습할 때 주의깊게 볼 부분 위주로 작성하도록 하겠다.



## html

### html의 기본 구조

- html: 문서의 최상위 요소

- head: 문서 메타데이터 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

  - `<title>, <meta>, <link>, <script>, <style>`등

- body: 문서 본문 요소

  - 실제 화면 구성과 관련된 내용



---



### DOM트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
  - 차후 javascript 파트에서 다룰 예정



### TAGS

- 태그를 모두 암기하는 것은 불가능하다.

- 시험을 대비해서, 내용이 없는 태그들(여는 태그와 닫는 태그로 이루어지지 않은 태그들)의 종류만 기억하자
  - br, hr, img, input, link, meta
- 태그별로 활용할 수 있는 attribute는 다르다.



### Semantic Tags

- HTML5에서 의미론적 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
  - header
  - nav
  - aside
  - section
  - article
  - footer
- 개발(가독성, 협업)에 유용할 뿐 아니라 검색엔진에 정보를 제공하는 데에도 중요하다.
- 텍스트 요소 tag들 중에도 `<b></b>`와 `<strong></strong>`, `<i></i>`와 `<em></em>`이 다른데, 이것 또한 semantic한가의 여부(후자가 semantic)에 의해 결정된다.



### form

- form은 정보를 서버에 제출하기 위한 영역
- form의 기본 attribute
- action: form을 처리할 서버의 URL
- method: form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
- enctupe: method가 post인 경우 데이터의 유형
  - application/x-www-form-rulencoded : 기본값
  - multipart/form-data : 파일 전송시(input type이 file인 경우)
- `<form></form>` 사이에 input들이 들어간다.



### input

- 주의할 점: label에 `for` attribute는 input의 id에 맞춰야 한다!
- input 태그에서, name attribute와 value attribute는 각각 key:value등의 형태로 전송된다.
- 즉, python의 자료형으로 치면 dictionary형태로 전송된다는 것이다.
- type="checkbox"나 type="radio"등에서 여러 input들을 묶을 때는, `name` attribute를 통일해줘야 한다.
- placeholder, autofocus 등의 attribute도 확인해보자.





## CSS

- Cascading Style Sheet

- 선택자(Selector)와 속성(Property), 값(Value)로 이루어져 있다.
- 인라인, 내부참조, 외부참조 방식이 있는데, 외부참조 방식이 디버깅이 편하고 재사용성을 높여 가장 바람직한 방법이다.



### 선택자

- 요소(element) 선택자
  - HTML 태그를 직접 선택

- 클래스 선택자
  - 마침표(.)문자로 시작, 해당 클래스가 적용된 항목을 선택

- 아이디 선택자
  - `#` 문자로 시작, 해당 아이디가 적용된 항목을 선택
  - 하나의 문서에 한번만 사용, 여러 번 사용해도 동작하지만, 한번만 사용하기로 약속
  - 아이디 선택자는 js를 통한 

- 선택자의 우선순위

  - !important > inline > 아이디 선택자 > 클래스, 속성, pseudo-class 선택자 > 요소 선택자, pseudo-element > 소스 순서

  

### CSS 상속

- 기본적으로, 눈에 보이는 시각적인 효과들은 상속된다고 보면 된다.
  - Text관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 것들은, box및 position 관련한 것들이 있다. 얘들이 상속되면 난리나기 때문
  - width, height, margin, padding, border, box-sizing, display, position, top, right, bottom left, z-index 등



### 크기 단위

- px
  - 픽셀 
  - 고정 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
  - 부모요소를 기준으로 변환
  
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음 
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - html의 기본 폰트 크기는 16px이므로, 이를 기준으로 함
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw(view width), vh(view height)
    -  viewport를 100으로 할 때, 1만큼의 넓이와 높이
  - vmin, vmax
    - viewport의 가로와 세로 중 작은 걸 기준으로 1/100이 vmin, 큰 걸 기준으로 1/100이 vmax
    - 예를 들어 가로가 1000px, 세로가 800px이라면 vmin은 8px, vmax는 10px이 된다.



### 색상 표시

- 색상 키워드
  - 대소문자를 구분하지 않음
  - red, blue, black 과 같이 특정 색을 직접 글자로 나타냄
- RGB
  - `# + 16` 진수 표기법 `p {color: #000000;}`
  - `rgb()` 진수 표기법 `p {color: rgb(0, 0, 0);}`

 - HSL 색상
   - 색상, 채도, 명도
   - `p {color: hsl(120, 100%, 0);}`
   - hsla의 경우, 투명도(alpha)까지
   - `p {color: hsla(120, 100%, 0, 0.5);}`

- 위 예시들은 모두 black!



### 글씨 스타일

- font-weight: 글씨의 굵기를 조정
- font-style: 글씨의 스타일(이탤릭체 등)을 조정

- font-family: 글씨체를 조정
- font-size: 글씨크기 조정

> 이외에도 여러 property등이 있다.





### Selectors 심화

---

#### 결합자

- 자손 결합자
  - selector A **하위**의 모든 selector B 요소
  - `div span {} `  형식으로 씀
- 자식 결합자
  - selector A **하위**의 모든 selector B 요소
  - `div > span {}` 형식으로 씀
- 일반 형제 결합자
  - selector A의 형제 요소 중 **뒤에 위치**하는(태그가 닫힌 뒤) selector B 요소를 **모두 선택**
  - `p ~ span {}` 형식으로 씀
- 인접 형제 결합자
  - selector A의 형제 요소 중 **바로 뒤에 위치**하는 selector B **요소를 선택**
  - `p + span {}` 형식으로 씀



#### pseudo-selector

- :nth-child(n)
  - 특정 단계 영역의 n번째 요소를 찾아 거기에 특성을 적용한다.
  - 만약 단계 영역의 n번째 목록이 해당 selector가 아니라면, 적용하지 않는다.

```html
    <div id="ssafy">
      <h2>어떻게 선택 될까?</h2>
      <h2>둥둥</h2>
      <p>둥둥</p>
      <p>둥둥</p>
      <p>둥둥</p>
    </div>
```

```css
#ssafy > p:nth-child(2) {
  color: red;
}
/* 아무것도 변하지 않는다. ssafy 하위 영역의 두 번째 tag가 p가 아니기 때문이다. */

#ssafy > p:nth-child(3) {
  color: red;
} 
/* 이렇게 하면 첫 번째 p 색이 변한다. */
```

- :nth-of-type()
  - 특정 단계의 요소의 tag들 중 n번째 항목에 특성을 적용한다.

```html
    <div id="ssafy">
      <h2>어떻게 선택 될까?</h2>
      <h2>둥둥</h2>
      <p>둥둥</p>
      <p>둥둥</p>
      <p>둥둥</p>
    </div>
```

```css
#ssafy > p:nth-of-type(2) {
  color: red;
}
/* 두 번째 p가 변한다. */

```



## Box

### Box model

- 모든 요소는 네모이고, 좌측 상단부터 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다.

- 요소들은 block과 inline요소로 나뉜다.

- 하나의 box는 네 부분으로 나누어진다.

  - content

    - 내용, 구성물

  - padding

  - margin

    - margin과 padding은 `margin-top: value`, `margin-right:value` 등과 같이 value를 줄 수 있다.
    - `margin: 2px`등과 같이 한 번에 표현도 가능하다.
    - shorthand 순서는, 1개일때는 모든 방향, 2개일때는 상하 좌우, 3개일때는 상, 좌우, 하, 4개일때는 상 우 하 좌 순서이다.

  - border

    - 상하좌우 설정 순서는 margin, padding과 동일하다.
    - border-width, border-style(solid만 쓸거다), border-color등의 property를 줄 수 있다.

    

### Box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box이다.
- 즉 지정한 사이즈는 padding안쪽 content의 사이즈가 되는 것이다.
- 일반적으로 우리가 하듯이 border까지의 사이즈를 기준으로 하기 위해서는 
  `box-sizing: border-box`로 설정해야 한다.



### Display

- 모든 요소는 네모(박스모델)이고, 좌측 상단에 배치.

- display에 따라 크기와 배치가 달라진다.

- display: block

  - 줄 바꿈이 일어나는 요소

  - 화면 크기 전체의 가로 폭을 차지한다.

  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.

  - 대표적인 블록 레벨 요소
    - div / li ul ol / p / hr / form 등
    
    

- display: inline

  - 줄 바꿈이 일어자지 않는 행의 일부 요소

  - **content 너비**만큼 가로 폭을 차지한다.

  - **width, height, margin-top, margin-bottom을 지정할 수 없다.**

  - 상하 여백은 line-height로 지정한다.

  - img도 inline이기 때문에 딱 붙이고 싶다면 font-size=0으로 지정하면 된다.

  - 대표적인 인라인 레벨 요소

    - span / a / img / input, label (form의 내부 - input은 닫는 태그가 없지만 label은 있다! 주의!) / b, em, i, strong (텍스트 요소) 등

    - **단, img는 특이하게도 width, height를 가진다!!**
    
      

- display: inline-block

  - block과 inline 레벨 요소의 특징을 모두 가짐

  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

  - 근데 잘 안쓴다. flexbox를 쓰지.

    

- display: none

  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

  

- 속성에 따른 수평 정렬
  - margin-right: auto == text-align: left == 좌측 정렬
  - margin-left: auto == text-align: right == 우측 정렬
  - margin-right: auto; & margin-lift: auto; == text-align: center; == 중앙 정렬



### Position

- static
  - 모든 태그의 기본값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

  
  
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative
  - absolute
  - fixed
  - sticky

  
  
- relative

  - 상대 위치
  - **자기 자신의 static 위치**를 기준으로 이동(normal flow **유지**)
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 **같음**
  - 즉 다른 요소들은 relative한 요소의 기본 위치를 기준으로 영향을 받음

  

- absolute

  - 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 **벗어남**)
  - **static이 아닌** 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 body를 기준으로 함)
  - 

- fixed

  - 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 즉 스크롤 시에도 항상 같은 곳에 위치

- sticky

  - 끈적 위치... 는 아니고 고정 위치
  - fixed와 같이 화면에 고정되어 위치하지만, normal flow에서 벗어나지 않아 다른 요소들과 겹치지 않는다.
  - 다른 sticky 요소와 만나는 순간 position이 변하는 특징이 있다고 하는데, 차후 구현해 봐야 알 수 있을 것 같다.

  

### 정리: CSS 원칙

- 모든 요소는 네모(박스모델), 좌측상단에 배치
- display에 따라 크기와 배치가 달라짐
- position으로 위치의 기준을 변경
  - relative: 본인의 원래 위치
  - absolute: 특정 부모의 위치
  - fixed: 화면의 위치