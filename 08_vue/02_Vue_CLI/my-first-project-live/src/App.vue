<template>
  <div id="app">
    <!-- img, a 둘 다 인라인 => 인라인 === 글자 -->
    <img alt="Vue logo" src="./assets/logo.png">
    <a href="">글자가 무슨 색인가요?</a>
    <!-- 중간에 태그 같은 것 넣어서 위치를 파악하며 코딩하는 게 중요 -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <HelloWorld msg="메시지 내용 변경함!!!"/>
    <!-- 각각 같은 객체를 넘겨주는 게 아니라 다른 걸 넘겨준다. -->
    <!-- vue는 도장찍기를 하기 위해 존재 -->
    <NewComponent message="NewComponent app 앙녕?"/>
    <NewComponent />
    <!-- <abc/> -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// 1번 불러오기
import NewComponent from './components/NewComponent.vue'
// import abc from './components/NewComponent.vue'

export default {
  name: 'App',
  components: {
    // 등록하기
    HelloWorld,
    NewComponent,
    // abc,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
