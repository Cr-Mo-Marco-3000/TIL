<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    
    
    <!-- 3. 보여주기(print) -->
    <!-- 아래의 두 케이스 모두 vue가 인식한다. 단, 아래가 더 범용적이다. -->
    <!-- 카멜 케이스 -->
    <!-- <input type="text" v-model="myMessage"> -->
    
    <!-- 자식 컴포넌트에 보낼 데이터 선언 -->
    <!-- 앞의 부분은 자식 컴포넌트의 props에서 선언하는 부분, 뒤의 부분은 data -->
    <!-- hard typing이 아니라 데이터를 바인딩 해주기 위해서 v-bind를 묶어준다.  -->
    <TheAbout 
    :my-message="parentData" 
    v-on:child-input-change="parentListenChange" />
    <!-- boss라는 이벤트를 듣고 있어야 한다. => 들으면 method 실행 -->


    <!-- 케밥 케이스 -->
    <!-- <the-about :my-message="parentData"></the-about> -->
  
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
      parentData: 'This is parent data from app.vue to child component'
    }
  },
  methods: {
    parentListenChange: function (inputData) {
      console.log('들리는군', inputData)
    }
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
