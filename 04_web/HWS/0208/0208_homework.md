# 0208_homework

## 1.

```css
/* 4가지가 있다. */

.class {
    display: flex;
    /* 좌 -> 우 */
    flex-direction: row; 
    /* 상 -> 하*/
    flex-direction: column:
    /* 우 -> 좌 */
    flex-direction: row-reverse;
	/* 하 -> 상 */
    flex-direction: column-reverse;
}
```



## 2. 

```html
<div class="flex-row flex-column flex-row-reverse flex-column-reverse"
```



## 3.

```css
.class {
    /* cross axis 방향으로 쭉 늘인다. */
    align-items: stretch;
    /* cross axis 시작 방향으로 붙인다. */
    align-items: flex-start;
    /* cross axis 끝 부분에 붙인다. */
    align-items: flex-end;
    /* cross axis 중앙으로 모은다. */
    align-items: center;
    /* baseline도 잊어버리지 마세요! */
}

```



## 4.

```css
(1)
/* flex-flow의 경우, flex-direction, flex-wrap을 묶어 설정할 때 쓴다. */
```



## 5.

```html
(a): container
(b): row
```



## 6.

```html
<!--
(c): sm, md, lg, xl, xxl등이 들어간다.
이는 small, medium, large, x-large, xx-large의 약자로서,
각자 화면이 어떤 크기 이상일 때, column이 몇 개 보일 것인가를 뜻한다.

(d): 숫자가 들어간다. 이는 c번과 합쳐서 특정 화면 크기일 때 화면에 column이 몇 개 보일 것인가를 의미한다.




-->
```

