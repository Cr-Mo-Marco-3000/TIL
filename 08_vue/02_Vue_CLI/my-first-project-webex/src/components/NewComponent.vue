<template>
  <div>
    <h2>New Component!!</h2>
    <h2>New Component!!</h2>
    <h2>{{ message }}</h2>
  </div>
</template>

<script>
export default {
  name: 'NewComponent!!', // vue devtool에서 보이는 이름 설정
  props: {
    message: String,
  }
}
</script>

<style>

</style>