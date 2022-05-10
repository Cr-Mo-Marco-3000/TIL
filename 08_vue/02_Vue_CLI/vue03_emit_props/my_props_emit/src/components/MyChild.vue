<template>
  <div>
    <h1>This is Child</h1>
    <p>ChildData:</p>
    <!-- 기본 input event가 발생했을 때마다, inputChildData 메소드를 실행 -->
    <input v-model="childData" type="text" @input="inputChildData">
    <p>ChildData: {{ childData }}</p>
    <p>AppData: {{ appData }}</p>
    <p>ParentData: {{ parentData }}</p>
  </div>
</template>

<script>
// 자식에서 부모로 올리는 것은 emit event => event를 만들어서 데이터를 실어 보냄
export default {
  name: 'MyChild',
    data : function () {
      return {
        childData: '',
      }
    },
  methods: {
    inputChildData: function () {
      // 본 메소드는 실행될 때 child-input이라는 이벤트를 발생시킴(이벤트 이름은 케밥 케이스로) => emit(신호 보내기)
      this.$emit('child-input', this.childData)
    }
  },
  props: {
    appData: String,
    parentData: String,
  },
}
</script>

<style>

</style>