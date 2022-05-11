<template>
  <!-- template는 구역 설정 -->
  <!-- template 안에는 반드시 하나의 Element만 있어야 한다. -->
  <!-- 그냥 h1, p 따로따로 나누어주면 문제가 된다. -->
  <!-- 일단 div를 하나 만들어놓고 시작 => 넣어주자 -->
  <div>
    <h1>{{ myMessage }}</h1>
    <p>아하! div는 하나구나!</p>
    <!-- <input type="text" v-model="childInputData" @keyup.enter="childInputEnter"> -->
    <!-- 엔터 키가 눌렸다 올라가면 childInputEnter 메서드 실행 -->
    <input type="text" v-model="childInputData" @keyup.enter="childInputEnter">
  </div>
</template>

<script>
export default {
  name: 'TheAbout',

  // 부모가 자식에게 넘기는 데이터는 props
  
  props: {
    myMessage: String,
  },
  data : function () {
    return {
      childInputData: ''
    }
  },
  methods: {
    childInputEnter: function () {
      // console.log('Enter!!', this)
      // 부모(조상이 아님) 컴포넌트에게 1번 인자 라는 이름의 이벤트를 발생 + 2번인자 데이터를 보냄
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>