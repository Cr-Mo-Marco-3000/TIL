<template>
  <div id="app">
    <img src="./assets/logo.png" alt="Vue logo">
    <PracticeFor my-message="This is prop data" :parent-data="parentData"></PracticeFor>
    <PracticeFor second-message="Second data"></PracticeFor>
  </div>
</template>

<script>
import PracticeFor from './components/PracticeFor.vue'

export default {
  name: 'App',
  components: {
    PracticeFor,
  },
  data: function () {
    return {
      parentData: 'This is parent Data by v-bind'
      }
  }
}
</script>

<style>

</style>
