<template>
  <div>
    <h1>This is Parent</h1>
    <p>ParentData: {{ parentData }}</p>
    <input v-model="parentData" type="text" @input="inputParentData">
    
    <p>AppData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <!-- my Child에는 App으로부터 맏은 appData와 MyParent에서 data 내부에서 만들고 v-Model로 작성해준 parentData를 다시 넘겨주어야 한다.  -->
    <MyChild :appData="appData" :parentData="parentData"
    @child-input="inputChildData"/>

  </div>
</template>

<script>
import MyChild from './MyChild.vue'
export default {
  name: 'MyParent',
  methods: {
    inputChildData: function (data) {
      this.childData = data
      console.log('!!! Text from child ~~~')
      this.$emit('child-input', this.childData)
    },
    inputParentData: function () {
      this.$emit('parent-input', this.parentData)
    }
  },
  props: {
    appData: String
  },
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  components: {
    MyChild,
  },
}
</script>

<style>

</style>