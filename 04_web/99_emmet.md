# Emmet

- HTML & CSS를 작성할 때, 효과적이고 빠른 마크업을 위한 오픈소스 플러그인
- 단축키와 약어등을 사용한다.
- 대부분의 텍스트 에디터에, 물론 vs code에도 기본으로 탑재되어 있다.
- 기본 사용법

```HTML
<!-- vs code -->

<!-- ul li 3개 -->
ul>li*3

<!-- 
이렇게 나옴

<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>
-->

<!-- fruit-list 아이디를 ul에 지정, fruit-list 클래스를 li 3개에 지정 -->
ul#fruit-list>li.fruit-list*3

<!-- 
이렇게 나옴

<ul id="fruit-list">
  <li class="fruit-list"></li>
  <li class="fruit-list"></li>
  <li class="fruit-list"></li>
</ul>
-->


<!--테이블-->
table>(thead>tr>th*3)+(tbody>tr>td*3)+(tfoot>tr>td*3)

<!-- 
이렇게 나옴

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tfoot>
</table>
-->

<!--태그 안 글씨-->
h1{Text in Tag}

<!--
<h1>Text in Tag</h1>
-->


```

- 이외의 사용법은 [치팅시트 ](https://docs.emmet.io/cheat-sheet/)참조