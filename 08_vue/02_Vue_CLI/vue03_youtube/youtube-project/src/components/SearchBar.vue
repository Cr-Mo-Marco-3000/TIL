<template>

    <div class="search-bar" :style="{ margin: videos-length ? '0' : '40vh 0'}" >
      <input @keypress.enter="onInputKeyword" type="text" placeholder="Search" >
    </div>

</template>

<script>

export default {
  name:'SearchBar',
  props: {
    videoLength: {
      type: Number,
    }
  },
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-search', event.target.value)
    }
  },
}

</script>

<style>

.search-bar > input {
  width: 100%; /* 가로 너비를 화면 전체 사용 */
  padding: 0.5 rem;
  font-size: 2rem;
}

</style>