<template>
  <div>
    <!-- $store가 store 안의 index.js를 의미 -->

    <TodoItem v-for="(todo, idx) in todos" :key="idx" :todo="todo" />
  </div>
</template>

<script>
import TodoItem from './TodoItem.vue'

// 1. vuex 모듈에서 mapState 메서드만 가져옴


export default {
  name: 'TodoList',
  components: {
    TodoItem
  },
  computed: {
    todos: function () {
      return this.$store.state.todos
    },
    
  }
}
</script>

<style>

</style>