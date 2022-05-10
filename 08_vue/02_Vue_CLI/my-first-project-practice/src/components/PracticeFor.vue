<template>
  <div>
    <h1>PracticeFor</h1>
    <h2>{{ myMessage }}</h2>
    <p>{{ secondMessage }}</p>
    <p>{{ secondMessage }}</p>
    <p>{{ secondMessage }}</p>
    <p>{{ secondMessage }}</p>
    <p>{{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'PracticeFor',
  props: {
    myMessage: String,
    secondMessage: String,
    parendDaga: String,
  }
  
}
</script>

<style>

</style>