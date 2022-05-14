<template>
  <div>
    <div>
      <span :class="{ completed: todo.completed}" @click="updateTodoStatus">{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function () {
      // console.log('Todo 삭제')
      this.$store.dispatch('deleteTodo', this.todo)
    },
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)

    }
    
  }
}
</script>

<style>
 .completed {
   text-decoration: line-through;
 }
</style>