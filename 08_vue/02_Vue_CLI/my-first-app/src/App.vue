<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기(print) -->

    <!-- 아래의 두 케이스 모두 vue가 인식한다. 단, 아래가 더 범용적이다. -->
    <!-- 카멜 케이스 -->
    <!-- <TheAbout :my-message='parentData'/> -->

    <!-- 케밥 케이스 -->
    <the-about :my-message="parentData"></the-about>
  
  </div>
</template>


<script>
// 1. 불러오기(import)
// Vue에서 import는 python에서 as의 역할 => ~라고 부르겠다.

import TheAbout from './components/TheAbout.vue'
export default {
  name: 'App',
  // 2. 등록하기(register)
  components: {
    TheAbout,
  },
  // data 안을 함수로 만들어주는 이유 => 참조 문제 때문
  data: function () {
    return {
      parentData: 'This is parent data to child component',

    }
  },
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
