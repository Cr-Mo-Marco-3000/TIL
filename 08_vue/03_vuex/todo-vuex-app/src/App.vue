<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos: {{ allTodosCount }}</h2>
    <h3>Completed Todos: {{ completedTodosCount }}</h3>
    <h3>Uncompleted Todos: {{ uncompletedTodosCount }}</h3>
    <TodoList />
    <TodoForm />

  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
import TodoForm from './components/TodoForm.vue'

export default {
  name: "App",
  components: {
    TodoList,
    TodoForm,
  },
  computed: {
    completedTodosCount: function () {
      return this.$store.getters.completedTodosCount
    },
    uncompletedTodosCount: function () {
      return this.$store.getters.uncompletedTodosCount
    },
    allTodosCount: function () {
      return this.$store.getters.allTodosCount
    }
    }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
