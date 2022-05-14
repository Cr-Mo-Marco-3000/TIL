<template>
  <div>
    <input v-model="todoTitle" type="text" @keyup.enter="createTodo">
    <button @click="createTodo">ADD</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        completed: false,
      }
      // this.$store.commit('CREATE_TODO', todoItem) // Mutation 사용했던 것
    if (todoItem.title) {
      this.$store.dispatch('createTodo', todoItem)
    }
    this.todoTitle = ''
    }
  }
}
</script>

<style>

</style>