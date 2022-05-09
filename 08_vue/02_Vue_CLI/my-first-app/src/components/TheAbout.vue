<template>
  <!-- template는 구역 설정 -->
  <!-- template 안에는 반드시 하나의 Element만 있어야 한다. -->
  <!-- 그냥 h1, p 따로따로 나누어주면 문제가 된다. -->
  <!-- 일단 div를 하나 만들어놓고 시작 => 넣어주자 -->
  <div>
    <h1>{{ myMessage }}</h1>
    <p>아하! div는 하나구나!</p>
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
      console.log('Enter!!', this.childInputData)
      // 부모 컴포넌트에게 ???라는 이름의 이벤트를 발생시킨다.
      this.$emit('boss')
    }
  }
}
</script>

<style>

</style>