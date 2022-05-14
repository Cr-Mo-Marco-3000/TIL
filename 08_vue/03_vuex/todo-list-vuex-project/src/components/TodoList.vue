<template>
  <div>
    <TodoListItem 
    v-for="todo in todos" 
    :key="todo.date"
    :todo="todo"
    />
    <!-- :todo="todo"를 붙이는 이유 => 결국은 todo를 props로 내려야 하기 때문에 -->
  </div>
</template>

<script>
import TodoListItem from './TodoListItem.vue'

export default {
  name: 'TodoList',
  computed: {
    todos: function () {
      return this.$store.state.todos
    }
  },
  components: {
    TodoListItem,
}
}

</script>

<style>

</style>