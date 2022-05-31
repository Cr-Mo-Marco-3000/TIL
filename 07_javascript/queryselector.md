# QuerySelector

- 특이한 형태의 QuerySelector
  - 쿼리 셀렉트를 할 때 []안에 속성을 바인딩
  - 만약 attribute에 숫자가 올 경우에는, queryselector 내부에 따옴표를 붙여 주어야 한다.

```js
// 클래스를 잡아 줄 때는 이렇게도 할 수 있다.
// 일반적으로는 그냥 ".asdf 이렇게 잡겠지만"
a = document.querySelector("[class=asdf]")

// div 중 data-key=asdf 특성을 가진 첫 번째
// even.keyCode가 숫자이므로, 그 주변에도 ""를 씌워 주어야 한다.
// 이 때, 내 외부의 따옴표가 같은 종류이면 안 된다!
document.querySelector("audio[data-key='36']")
```

