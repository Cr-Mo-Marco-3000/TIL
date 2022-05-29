<template>
  <div id="app">
    <h1>오늘 내가 할 일</h1>
    <TodoList />
    <TodoForm /> 
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'
// import { mapMutations } from 'vuex'

export default {
  name: 'App',
  components:{
    TodoList,
    TodoForm,
  },
  // state나 getters에서 불러오는 값은 data가 아니라 computed에 매핑해야 한다!
  // data를 state에 매핑하면 변동될 때 state와 연동되어 같이 꼬이기 때문이다.
  computed: {
    todos() {
      return this.$store.state.todos
    }
  },
  // methods: {
  //   ...mapMutations(['LOAD_TODOS'])
  // },
  // created() {
  //   this.LOAD_TODOS()
  // }
  
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
