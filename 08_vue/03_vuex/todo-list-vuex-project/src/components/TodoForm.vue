<template>
  <div>
    TodoForm 
    <input type="text" 
    @keyup.enter="createTodo" 
    v-model.trim="todoTitle" >
    <button @click="createTodo">할 일 등록</button>
  </div>
</template>

<script>

export default {
  name: 'TodoForm',
  data: function() {
    return {
      todoTitle: ""
    }
  },
  methods:{ 
    createTodo: function () {
      const newTodo = {
        title : this.todoTitle,
        isCompleted: false,
        date: new Date().getTime()
      }
      // createTodo를 호출하며 두 번째 인자로 위의 newTodo를 넘김

      if (newTodo.title) {
        this.$store.dispatch('createTodo', newTodo)
      }
      this.todoTitle = ""
    },
  }
}
</script>

<style>

</style>