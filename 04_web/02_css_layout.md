# CSS Layout



## float



- 박스를 왼쪽 또는 오른쪽으로 이동시켜 **텍스트 및 인라인 요소들이** 주변을 wrapping하도록 함

- 요소가 position: absolute, position: fixed처럼 normal flow를 벗어나도록 함

- float는 왼쪽에서 오른쪽으로 쌓인다.

- 기존에는 레이아웃을 구성하기 위해 필수적으로 사용되었지만, 최근엔 Flexbox, Grid 등장과 함께 사용도가 낮아졌다.

- float 종류

  - `float: none;` 기본값(적용안됨)
  - `float: left;` 요소를 왼쪽으로 띄움
  - `float: right`; 요소를 오른쪽으로 띄움

  

- 예시

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .box {
        width: 10rem;
        height: 10rem;
        border: 1px solid black;
        background-color: aqua;
        margin-right: 30px;
      }

      .left {
        float: left;
      }

      .right {
        float: right;
      }
    </style>
  </head>
  <body>
    <h1>float</h1>
    <div class="box left"></div>
    <div class="box right"></div>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias
      consequuntur, dolorum, consectetur saepe dicta blanditiis tempore dolore
      delectus voluptate sunt enim quibusdam? Soluta similique, nam obcaecati
      doloremque exercitationem, nulla illo ipsum iusto nobis quia reiciendis
      error non, consequuntur distinctio dolor repellendus optio deserunt
      tenetur? Totam aperiam praesentium vitae illo, veniam a reiciendis
      corrupti officia minus veritatis neque! Illum accusamus ipsum aliquid
      velit voluptas deleniti, rerum dolorem minus quis eius tempora mollitia
      illo nam nisi perspiciatis itaque optio saepe, debitis consequatur alias
      ipsam odio veritatis? Sequi qui velit nemo mollitia blanditiis, distinctio
      ducimus iure ratione dolores fugit quia adipisci, repudiandae quaerat.
      Ratione voluptatem dolore porro optio error, quaerat recusandae
      voluptatibus reprehenderit corrupti ut ipsa blanditiis nam impedit
      explicabo vitae! Illum labore explicabo cupiditate voluptates adipisci
      recusandae quam suscipit ad libero ipsum incidunt animi natus vel autem
      quisquam a repellendus hic dolore veritatis mollitia tempore magni, nisi
      blanditiis. Laborum eveniet similique consequuntur ut alias odio
      voluptatum necessitatibus, unde officia amet mollitia nemo qui odit
      quibusdam rem. Esse fuga, quisquam placeat eos deleniti alias, delectus
      quidem quam, vero eum incidunt voluptates repellendus neque velit voluptas
      modi. Quidem expedita distinctio laborum exercitationem dicta, magnam
      possimus quisquam eaque, dolor laudantium nam aperiam illo natus in amet
      repudiandae quis inventore dignissimos culpa minus ab iste. Repellendus,
      quae numquam tenetur, iure at eligendi recusandae et, quidem error cum
      voluptatibus repudiandae optio? Impedit sed illum aperiam repellat, dolore
      earum similique, voluptatem id ipsa vero voluptate dolor! At illo cumque
      architecto facilis vitae nobis fugit saepe necessitatibus aut omnis, iste
      earum voluptatem a nostrum amet commodi sed suscipit! Placeat facilis amet
      recusandae iure sint, eveniet quos praesentium error nemo fugit sunt
      natus. Porro cumque perspiciatis cupiditate veritatis earum, assumenda sit
      exercitationem harum voluptatem facere accusantium est consequatur alias,
      omnis iste! Nostrum ipsam expedita architecto eveniet provident rem est
      nam!
    </p>
  </body>
</html>

```



- 아래와 같은 경우, 문제가 생긴다.

- 둥둥 떠서, 부모 요소가 둘레를 감쌀 때 문제가 생긴다. 

  => 부모도 높이를 인식 못 하는 것이다.

  

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .box1 {
        width: 10rem;
        height: 10rem;
        border: 1px solid black;
        background-color: aqua;
      }

      .box2 {
        width: 20rem;
        height: 10rem;
        border: 1px solid black;
        background-color: crimson;
      }

      .left {
        float: left;
      }
    </style>
  </head>
  <body>
    <div class="box1 left">box 1</div>
    <div class="box2">box 2</div>
  </body>
</html>

```

- 아래와 같이, clearfix라는 일종의 트릭을 만들어서 해결할 수 있다.

- 굳이 이름을 clearfix로 할 필요는 없지만, 일반적으로 그렇게 한다.

- 단계는 다음과 같다.

  1) div를 만들어 float요소의 부모로 만든다.

  2. ```clearfix::after {content:""; display:block; clear:both;}```

     본 클래스를 만들어 float 요소의 부모에 적용한다.

- ::after => 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성

  보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용



```html
<!--해결방법-->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .box1 {
        width: 10rem;
        height: 10rem;
        border: 1px solid black;
        background-color: aqua;
      }

      .box2 {
        width: 20rem;
        height: 10rem;
        border: 1px solid black;
        background-color: crimson;
      }

      .left {
        float: left;
      }

      .clearfix::after {
        content: "";
        display: block;
        clear: both; 
          /*이 성질이 없을 때 1. 부모요소 높이가 0 => 자식 float 
          2. box2 공간을 채움  
          => 부모가 자식의 높이만큼 가져갈 수 있도록 clearing함*/
      }
    </style>
  </head>
  <body>
    <!-- clearfix
    1. float 요소의 부모로 div!
    2. 부모에게 .clearfix -->
    <div class="clearfix">
      <div class="box1 left">box 1</div>
    </div>
    <div class="box2">box 2</div>
  </body>
</html>
```

- 개별적으로 clear:left;를 주어 해결할 수 있을 것 같아 보이지만, 

  만약 부모가 있다면 자식이 float되어 부모가 인식을 못 하는 문제가 발생한다.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .box1 {
        /* 10rem => 160px (root -> 16px) */
        width: 10rem;
        height: 10rem;
        border: 1px solid black;
        background-color: crimson;
      }

      .box2 {
        /* 10rem => 160px (root -> 16px) */
        width: 20rem;
        height: 10rem;
        border: 1px solid black;
        background-color: cornflowerblue;
      }

      .left {
        float: left;
      }

      .clear-left {
        clear: left;
      }

      .news-container {
        border: 10px solid hotpink;
      }

      /* .news-container::after {
            content: "";
            display: block;
            clear: both;
        } */

      .required::after {
        content: "*";
        color: crimson;
      }
    </style>
  </head>
  <body>
    <div class="news-container">
      <div class="box1 left">A일보</div>
      <div class="box1 left">B일보</div>
      <div class="box1 left">C일보</div>
    </div>
    <!-- 아래 clear-left class를 넣어 비교해보자 -->
    <div class="box2">추천 블로그</div>

    <label for="username" class="required">username</label>
    <input type="text" id="username" required />
    <label for="university">학교</label>
    <input type="text" id="university" />
  </body>
</html>

```





- float 활용 전략 - normal flow에서 벗어난 레이아웃 구성
  - 원하는 요소들을 float로 지정하여 배치
  - 부모 요소에 반드시 clearing float를 하여 이후 요소부터 Normal Flow를 가지도록 지정



## flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis (메인 축)
  - cross axis (교차 축)
- 구성 요소
  - flex container(부모 요소)
  - flex item(자식 요소)

- 기본: flex-direction : row(메인 축이 가로)
- 부모 요소에 `display: flex;` 혹은 `display: inline-flex;`



- 왜 씀?

  수동 값 부여 없이

  1. 수직 정렬이 너무 힘들었다.
  1. 아이템의 너비와 높이 혹은 간격을 동일하게 배치하기 어려웠다.




- flex 속성

  - flex-direction: main axis 기준 방향 설정
    - row, row-reverse, column, column-reverse

    - 역방향의 경우 html 태그 선언 순서와 시각적으로 다르니 유의
    
      => (웹 접근성에 영향)
  
  - flex wrap(줄바꿈)
    - 아이템이 컨테이너를 벗어나는 경우, 해당 영역 내에 배치되도록 설정
    - 즉 기본적으로 컨테이너 영역을 벗어나지 않도록 함
    - wrap: 너비 120px, 개별 아이템 30px
    - nowrap(기본값)
  
  - flex-flow
    - flex-direction과 flex-wrap의 shorthand
    - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
    - e.g. `flex-flow: row nowrap;`
  
  
  - 공간 나누기
    - **justify-content(main axis)**
    - align-content(cross axis)
  
  - 정렬
    - **align-items(모든 아이템을 cross axis 기준으로)**
      - Cross axis를 기준으로 공간 배분 ( 아이템이 한 줄로 배치되는 경우 확인할 수 없음)
  
    - align-self(**개별 아이템에 적용**)
  
  - Flex에 적용하는 기타 속성(**얘들도 개별 아이템에 적용**)
    - flex-grow: 남은 영역을 아이템에 분배해서 자라게 함
    - order: 배치 순서
  



- [예시1](./flex_example/03_01_flex) [예시2](./flex_example/03_02_flex_layout) 참조





## 부트스트랩

- 반응형 웹을 편하게 만들기 위한 오픈소스 툴킷

- 라이브러리를 다운로드받아 사용할 수 있다.
- CDN(Content Delivery Network을 통해 js,css파일을 웹에서 받아 쓸 수 있다.

- 유틸리티, 컴포넌트, 그리드 시스템등을 지원한다.



- 사용법
  - head에 `<link>`태그를 달고, `</body>` 바로 위에 `<script>` 태그를 만든다.
  - 직접 파일을 연결하거나, 공식 사이트에서 따온다.



### class		

- 물론 다 외우는 것은 불가능하다.
- 중요한 것들 위주로 기억하고, Pure CSS와 어떻게 연계되는지 정도만 기억하자.



- spacing

  - .mt-1 == margin top 0.25rem
  - 1:0.25rem, 2: 0.5rem, 3: 1rem, 4: 1.5rem, 5: 3rem
  - .mx-0
    - .mx-0 {margin-right: 0px; margin-left: 0px;}
  - .mx-auto
    - .mx-auto {margin-right: auto; margin-left: auto;}



- colors

  - .bg-primary, text-primary 등으로 쓴다.
  - primary
  - secondary
  - success
  - info
  - 등등

  

- text-align

  - text-start
  - text-center
  - text-end

  

- font style

  - fw-bold
  - fw-normal
  - fst-italic

  

- display

  - d-inline
  - d-block
  - d-flex 등으로 쓴다.

  

- border
  - border-radius



- position

  - fixed-top

  

- flexbox
  - d-flex justify-content-start 등으로 쓴다.



## Responsive Web

- 반응형 웹
- 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장
- 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는 데 사용되는 용어
- 예시
  - Media Queries, Flexbox, Bootstrap Grid System, The viewpoint meta tag



### Bootstrap Grid System

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - Column: 실제 컨텐츠를 포함하는 부분
  - Gutter: 칼럼과 칼럼 사이의 공간(사이 간격)
  - Container: Column들을 담고 있는 공간.

- Bootstrap Grid System은 Flexbox로 제작됨

- container, row, column으로 컨텐츠를 배치하고 정렬

- 반드시 기억해야 할 2가지!

  - 12개의 column

    - 각자의 col에 class를 주는 법

      - class="col-md-3"
        - 768px 이상의 화면에서 12개 그리드 중 3개를 먹는다!
        - col 뒤에 아무것도 붙이지 않으면, 남는 자리를 알아서 분배해 먹는다.

    - row에 col을 주는 법

      - ```css
        <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
            <div class="col">Column</div>
            <div class="col">Column</div>
            <div class="col">Column</div>
            <div class="col">Column</div>
          </div>
        </div>
        ```

      - 576 이하에서는 column을 하나로 표시

      - 576~768에서는 2개로 표시

      - 768 이상에서는 4개로 표시

    - nesting

      - col 안에 col을 주는 것!

      - ```css
        <div class="row">
        	<div class="col-6">
        		<div class="row">
        			<div class="col-3"> 
        /* 이 라인부터는 기준이 전체 화면의 절반이 된다. 즉 6/12 * 3/12만큼 먹는다. */
        ```

        

  - 6개의 grid breakpoint

    - xs: < 576px

    - sm: >= 576px

    - md: >= 768px

    - lg: >= 992px

    - xl: >= 1200px

    - xxl: <= 1400px

      

- offset

  - e.g. col-4 offset-4 col-md-4 offset-md-0 col-lg-8 offset-lg-2
    - 768 이하일 때, offset-4 col-4
    - 768 ~ 992일 때, offset-0 col-4
    - 992 이상일 때, offset-2, col-8

  



- 기억해야 할 원칙
  - 어떤 스타일이 적용이 안 됐으면 클래스에 문제가 있는 것이다!

