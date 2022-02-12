# Media query

### 웹 페이지 레이아웃의 종류



- 고정폭 레이아웃
  - 브라우저의 크기가 변화하더라도 컨텐츠가 변화하지 않음


- 유동적 레이아웃
  - 이미지 및 글씨 등 영역이 유동적으로 변화함


- 별도의 사이트
  - 디바이스에 따른 별도의 사이트(도메인)으로 구분됨


- 반응형 레이아웃

  - 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법

  - 미디어 쿼리를 활용하여 CSS를 작성함

  - 최근 많이 볼수 있는 경우




## 미디어 쿼리

- 미디어 쿼리는 CSS에서 @media 키워드를 활용하여 브라우저 및 디바이스 등 환경에 따라 CSS를 적용할 수 있는 방법

- 간단하게 말하면, 어떤 모드에서 특수하게 보이는 것을 말한다.

  - media-type: all, print, screen, speech
  - meida-feature-rule: orientation(방향), width, height 등

- bootstrap의 breakpoint도 본 기능을 활용하여 구현한 것이다.

  

- 대표적인 형태는 다음과 같다.

```css
/* 미디어 쿼리 예시는 다음과 같다. */
/* media-type일 때는 @media 다음에 타이핑 */
/* media-feature-rule일 때는 ()안에 타이핑 */

@media media-type and (media-feature-rule) {
  /* CSS rules go here */
}

```



- 다음은 다양한 활용방법들이다.

```css
/* Media Type: all, print, screen, speech  */

/* 인쇄 모드에서 검은색으로 출력(!important는 *의 우선순위가 떨어지기 때문에 붙여줌) */
/* 워터마크 등도 이런 식으로 구현 가능 */
@media only print {
  * {
    color:black !important;
  }
}

/* ------------------------------------------------------------------------------------------------------ */

/* Media-Feature-Rule*/

/* 가로 모드 (너비 > 높이) */
@media (orientation: landscape) {
  h1 {
    color: green;
  }
}

/* 세로 모드 (높이 > 너비) */
@media (orientation: portrait) {
  h1 {
    color: red;
  }
}

/* ------------------------------------------------------------------------------------------------------ */


/* 넓이가 300일 때  */
@media (width: 300px) {
  h2 {
    color: burlywood;
  }
}


/* 700px보다 클 때는 darkblue */
@media (min-width: 700px) {
  h3 { 
    color: darkblue;
  }
}


/* 600px보다 작을 때는 darkgoldenrod */
@media (max-width: 600px) {
  h3 {
    color: darkgoldenrod;
  }
}
/* 600~700px때는 검은색 => 본 예시는 breakpoint를 잘못 잡은 셈이다. */

/* ------------------------------------------------------------------------------------------------------ */

/* 다음처럼 하면 순차적으로 적용할 수 있다. */
/* 단, 순서를 바꾸면 안 된다. CSS는 뒤에 있는 게 우선 적용 되기 때문에 */
/* 500px이 맨 아래 있으면, 다 덮어버리게 된다. */

@media (min-width:500px) {
  h4 {color: red;
  }
}

@media (min-width:600px) {
  h4 {color: blue;
  }
}

@media (min-width:700px) {
  h4 {color: violet;
  }
}

@media (min-width:800px) {
  h4 {color: yellow;
  }
}

/* ------------------------------------------------------------------------------------------------------ */

/* 다중 조건 */
/* 두 조건이 모두 만족할 때: and */

@media (max-height: 500px) and (max-width: 500px) {
  h5 {
    color:pink;
  }
}

/* 두 조건 중 하나라도 만족할 때: ,(or 아님) */

@media (max-height: 500px) , (max-width: 500px) {
  p {
    color:palegreen;
  }
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./practice.css">
  <title>Document</title>
</head>
<body>
  <h1>Media Query</h1>
  <h2>width:300px</h2>
  <h3>min-width: 700px, max-width: 600px</h3>
  <h4>min-width: 500 600 700 800</h4>
  <h5>(max-height: 500px) and (max-width: 500px)</h5>
  <p>(max-height: 500px) , (max-width: 500px)</p>
</body>
</html>
```